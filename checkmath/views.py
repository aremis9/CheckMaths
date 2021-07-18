from django.shortcuts import render
from calculations import sendemail


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not subject or not message:
            return render(request, 'main/contact.html', {
                'email': email,
                'name': name,
                'subject': subject,
                'message': message,
                'invalid': 'Subject and message is required!'
            })

        messageorig = message
        if name:
            message = message + '\n\n' + f'-{name}'

        success = sendemail(email, subject, message)
        
        if not success:
            return render(request, 'main/contact.html', {
                    'email': email,
                    'name': name,
                    'subject': subject,
                    'message': messageorig,
                    'invalid': 'Invalid email'
                })

        return render(request, 'main/contact.html', {
                'email': email,
                'name': name,
                'subject': subject,
                'message': messageorig,
                'invalid': False
            })

    else:
        return render(request, 'main/contact.html', {'invalid': ''})