from django.shortcuts import render, redirect
from .models import Student

def home(request):
    return redirect('student_list')

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        address = request.POST.get('address')
        course = request.POST.get('course')
        image = request.FILES.get('image')

        student = Student(
            name=name,
            age=age,
            gender=gender,
            email=email,
            address=address,
            course=course,
            image=image,
        )
        print("Save Student data....")
        student.save()
        
        return redirect('student_list')
        
    return render(request, 'students/add_student.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def student_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'students/student_detail.html', {'student': student})

def update_student(request, id):
    student = Student.objects.get(id=id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.gender = request.POST.get('gender')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        student.course = request.POST.get('course')
        
        if 'image' in request.FILES:
            student.image = request.FILES.get('image')
            
        student.save()
        return redirect('student_list')
        
    return render(request, 'students/update_student.html', {'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')
