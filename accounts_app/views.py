import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from administrator.models import MemberProfile 

User = get_user_model()  # Fetch the correct custom user model

@login_required(login_url='accounts_app:login')
def homepage(request):
    return render(request, 'admin/home.html')

def admin_home(request):
    return render(request, 'administrator/admin_home.html')

def registerpage(request):
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact')
        gender = request.POST.get('gender')
        aadhaar = request.POST.get('aadhaar')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate Age
        try:
            age = int(request.POST.get('age', 18))  # Set default to 18 if age not provided
        except ValueError:
            messages.error(request, "Invalid age! Please enter a valid number.")
            return redirect('accounts_app:register')

        # Aadhaar Validation (Exactly 12 digits)
        if not re.fullmatch(r'\d{12}', aadhaar):
            messages.error(request, "Aadhaar number must be exactly 12 digits.")
            return redirect('accounts_app:register')

        # Username validation
        if not username:
            messages.error(request, "Username is required!")
            return redirect('accounts_app:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('accounts_app:register')

        # Password match validation
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('accounts_app:register')

        # Aadhaar uniqueness validation (Check in MemberProfile, not User model)
        if MemberProfile.objects.filter(aadhaar=aadhaar).exists():
            messages.error(request, "Aadhaar number already registered!")
            return redirect('accounts_app:register')

        try:
            # Create User
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            # Create Member Profile
            MemberProfile.objects.create(
                user=user,
                contact_number=contact_number,
                gender=gender,
                aadhaar=aadhaar,
                age=age
            )

            messages.success(request, "Account created successfully! Please log in.")
            return redirect('accounts_app:login')

        except IntegrityError:
            messages.error(request, "An error occurred. Please try again later.")
            return redirect('accounts_app:register')

    return render(request, 'accounts/member/signup.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('login_username')  # updated field name
        password = request.POST.get('login_password')  # updated field name
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('administrator:member_dashboard')  # adjust redirect as needed
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('accounts_app:login')

    return render(request, 'accounts/member/login.html')

def logoutpage(request):
    logout(request)
    return redirect('accounts_app:login')

@login_required(login_url='accounts_app:login')
def member_list(request):
    members = MemberProfile.objects.all()
    return render(request, 'admin/member_list.html', {'members': members})

@login_required(login_url='accounts_app:login')
def toggle_status(request, member_id):
    member = get_object_or_404(MemberProfile, id=member_id)
    member.status = "inactive" if member.status == "active" else "active"
    member.save()
    
    status_msg = "activated" if member.status == "active" else "deactivated"
    messages.success(request, f"Member {member.user.username} {status_msg} successfully!")
    return redirect('accounts_app:member-list')
