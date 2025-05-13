from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

def payment_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        # Allow staff and superusers to access without payment
        if request.user.is_staff or request.user.is_superuser:
            return view_func(request, *args, **kwargs)

        # Check if profile exists and if user has paid
        profile = getattr(request.user, 'profile', None)
        if not profile or not profile.has_paid:
            messages.warning(request, "Please make a payment to access blogs.")
            return redirect('administrator:membership-payment')

        return view_func(request, *args, **kwargs)
    return _wrapped_view
