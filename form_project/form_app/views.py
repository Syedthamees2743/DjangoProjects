"""
Views for form_app.

Flow:
  1. form_page  – display the empty form (GET) or validate & store in session (POST)
  2. display_page – read session data and show a read-only card
  3. edit_page  – re-populate the form with session data so the user can edit
  4. confirm_page – persist session data to the database and clear the session
"""

from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import UserDetailsForm
from .models import Submission


def form_page(request):
    """
    Page 1 — Input Form.
    GET:  Show a blank form (or pre-filled if coming from the Edit button).
    POST: Validate the form. If valid, store data in the session and
          redirect to Page 2. If invalid, re-render with errors.
    """
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            request.session['form_data'] = form.cleaned_data
            return redirect('form_app:display')
    else:
        stored = request.session.get('form_data')
        if stored:
            form = UserDetailsForm(initial=stored)
        else:
            form = UserDetailsForm()

    return render(request, 'form_app/form_page.html', {'form': form})


def display_page(request):
    """
    Page 2 — Display / Preview.
    Reads the form data from the session.
    """
    form_data = request.session.get('form_data')

    if not form_data:
        messages.warning(request, 'No data found. Please fill out the form first.')
        return redirect('form_app:form')

    return render(request, 'form_app/display_page.html', {'data': form_data})


def edit_page(request):
    """
    Handles the "Edit" button on Page 2.
    Redirects to Page 1. Because the session still holds the data,
    the form_page view will pre-fill the form.
    """
    return redirect('form_app:form')


def confirm_page(request):
    """
    Handles the "Confirm" button on Page 2.
    Reads data from the session, creates a Submission record,
    clears the session data, and shows a success page.
    """
    form_data = request.session.get('form_data')

    if not form_data:
        messages.warning(request, 'No data to confirm. Please fill out the form first.')
        return redirect('form_app:form')

    Submission.objects.create(
        name=form_data['name'],
        email=form_data['email'],
        phone=form_data['phone'],
        address=form_data['address'],
        additional_details=form_data.get('additional_details', ''),
    )

    del request.session['form_data']

    messages.success(request, 'Your information has been submitted successfully!')
    return render(request, 'form_app/display_page.html', {
        'data': form_data,
        'confirmed': True,
    })