from django.shortcuts import render, redirect
from .forms import FirstNumberForm, SecondNumberForm, OperatorForm


def step1(request):
    if request.method == 'POST':
        form = FirstNumberForm(request.POST)

        if form.is_valid():
            request.session['first_number'] = form.cleaned_data['first_number']
            return redirect('step2')

    else:
        form = FirstNumberForm()

    return render(request, 'calculator/step1.html', {'form': form})


def step2(request):
    if request.method == 'POST':
        form = SecondNumberForm(request.POST)

        if form.is_valid():
            request.session['second_number'] = form.cleaned_data['second_number']
            return redirect('step3')

    else:
        form = SecondNumberForm()
    return render(request, 'calculator/step2.html', {
        'form': form,
        'first_number': request.session.get('first_number')
        })


def step3(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST)

        if form.is_valid():
            request.session['operator'] = form.cleaned_data['operator']
            return redirect('result')

    else:
        form = OperatorForm()

    return render(request, 'calculator/step3.html', {
        'form': form,
        'first_number': request.session.get('first_number'),
        'second_number': request.session.get('second_number')
        })


def result(request):
    a = request.session['first_number']
    b = request.session['second_number']
    op = request.session['operator']

    if op == 'add':
        result = a + b

    elif op == 'subtract':
        result = a - b

    elif op == 'multiply':
        result = a * b

    elif op == 'divide':
        result = a / b

    return render(request, 'calculator/result.html', {
        'first_number': a,
        'second_number': b,
        'operator': op,
        'result': result
    })


def reset(request):
    request.session.flush()
    return redirect('step1')