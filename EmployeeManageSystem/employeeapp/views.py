from django.shortcuts import render, redirect
from employeeapp.models import Employee


def add_employee(request):

    if request.method == "POST":
        nameemp = request.POST.get("name")
        emailemp = request.POST.get("email")
        departmentemp = request.POST.get("department")
        salaryemp = request.POST.get("salary")

        employee = Employee(
            name=nameemp, email=emailemp, department=departmentemp, salary=salaryemp
        )

        employee.save()

    return render(request, "add_employee.html")


def view_employee(request):
    employees = Employee.objects.all()

    return render(request, "view_employee.html", {"employees": employees})


def editemployee(request, emp_id):

    editemployee = Employee.objects.get(id=emp_id)

    return render(request, "edit_employee.html", {"edemp": editemployee})


def updateemployee(request, emp_id):

    if request.method == "POST":
        emp = Employee.objects.get(id=emp_id)

        emp.name = request.POST.get("name")
        emp.email = request.POST.get("email")
        emp.department = request.POST.get("department")
        emp.salary = int(request.POST.get("salary"))

        emp.save()
        return redirect("view_employee")

    else:
        return redirect("add_employee")


def deleteemployee(request, emp_id):

    delemp = Employee.objects.get(id=emp_id)

    delemp.delete()

    return redirect("view_employee")
