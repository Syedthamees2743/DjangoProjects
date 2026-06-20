from django.shortcuts import render

from mailapp.models import Studentmail

# Create your views here.

def home(request):
    return render(request,'add_mail.html')


def add_mail(request):
    if request.method == 'POST':
        studentid= request.POST.get('studentid')
        subject = request.POST.get('subject')
        mail = request.POST.get('mail')

    add_mail = Studentmail(studentid=studentid,subject=subject,mail=mail)
    add_mail.save()

    subject = "Job Application Response"
    message = "Dear Student, \n\nThank you for your job application. We have received your application and will review it shortly. We appreciate your interest in our company and will get back to you with further updates.\n\nBest regards,\nHR Team"
    


