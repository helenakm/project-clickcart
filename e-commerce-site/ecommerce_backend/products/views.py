from django.shortcuts import render


#super user: Username: admin, Password: password

def home(request):
    return render(request, 'home.html', {})
