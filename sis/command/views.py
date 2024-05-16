from django.contrib.auth.decorators import login_required
from django.shortcuts import render

def index(req):
    return render(req, 'command/home.html')

def logout(req):
    pass

def students(req):
    return render(req, 'command/students.html')

def professors(req):
    return render(req, 'command/doctors.html')

def teaching_assistants(req):
    return render(req, 'command/ta.html')

def courses(req):
    return render(req, 'command/courses.html')

def withdraw_course(req):
    return render(req, 'command/withdraw.html')

def create_course(req):
    return render(req, 'command/create.html')

def report(req):
    return render(req, 'command/report.html')

