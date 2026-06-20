from django.shortcuts import redirect, render

from formapp.forms import employeeforms
from formapp.models import Employee

# Create your views here.

def home(request):
    forms = employeeforms()
    return render(request, 'form_page.html', {'form': forms})

def add_employye(request):
    if request.method == 'POST':
        form = employeeforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


def show_employee(request):
    display = Employee.objects.all()
    return render(request, 'show_employee.html', {'display': display})


def edit_employee(request,pk):
    empl=Employee.objects.get(id=pk)
    detail=employeeforms(instance=empl)
    return render(request,'edit_employee.html',{'form':detail})
