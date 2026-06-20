from django.shortcuts import render
from django.core.mail import send_mail
from mail_app.models import Employeemail


def add_mail(request):

    if request.method == 'POST':
        employeeid = request.POST.get('employeeid')
        employeename=request.POST.get('employeename')
        subject = request.POST.get('subject')
        mail = request.POST.get('mail')

        record = Employeemail(
            employeeid=employeeid,
            employeename=employeename,
            subject=subject,
            mail=mail
        )
        record.save()

        message = f"""
Dear {employeename},

Your Registration is Successful.

Your Login Details:

Username : {employeename}{employeeid}
Password : {employeename}@1234

Thank You
"""
        send_mail(
    subject,
    message,
    'thameessyed2743@gmail.com',
    [mail]
)
        
        return render(request, 'add_mail.html', {'success': True})

    return render(request, 'add_mail.html')