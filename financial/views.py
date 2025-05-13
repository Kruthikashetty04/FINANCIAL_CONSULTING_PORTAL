from django.shortcuts import render

def design(request):
    return render(request, 'Public/base/design.html')  # Ensure 'design.html' exists in templates


def home(request):
    return render(request, 'admin/home.html')  # Ensure 'home.html' exists inside your templates folder


def member_dashboard(request):
    return render(request, 'admin/member_dashboard.html')

