from django.shortcuts import render, redirect

from keyapp.models import Course, Student
from .forms import CourseForm


def home(request):

    return render(request, "keyapp/home.html")


def add_course(request):

    form = CourseForm()

    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("addcourse")

    context = {"form": form}

    return render(request, "keyapp/add_course.html", context)


def StudentPage(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "keyapp/add_student.html", context)


def AddStudent(request):

    if request.method == "POST":
        student_name = request.POST.get("student_name")

        student_email = request.POST.get("student_email")

        student_phone = request.POST.get("student_phone")

        student_address = request.POST.get("student_address")

        course_id = request.POST.get("course")

        if course_id:
            course = Course.objects.get(id=course_id)

            data = Student(
                student_name=student_name,
                student_email=student_email,
                student_phone=student_phone,
                student_address=student_address,
                course=course,
            )

            data.save()

        return redirect("home")

    return redirect("StudentPage")
