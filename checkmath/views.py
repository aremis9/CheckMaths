from django.shortcuts import render


def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not email or not subject or not message:
            return render(request, 'main/contact.html', {
                'email': email,
                'name': name,
                'subject': subject,
                'message': message,
                'invalid': True
            })

        return render(request, 'main/contact.html', {
                'email': email,
                'name': name,
                'subject': subject,
                'message': message,
                'invalid': False
            })

    else:
        return render(request, 'main/contact.html')