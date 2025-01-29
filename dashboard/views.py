from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


@login_required
def dashboard_view(request):
    """
    Renders a single dashboard page for customers, owners, and superusers.
    """
    current_user = request.user
    context = {}
    # Add the username to the context
    context['username'] = current_user.username

    # Check if the user is a superuser
    if current_user.is_superuser:
        # Superuser-specific context
        context['user_type'] = 'superuser'
        # Add link to admin page
        context['admin_url'] = '/admin/'
        # Separate superuser dashboard template
        return render(request, 'dashboard/dashboard.html', context)

    # Regular users: Check for profile
    try:
        user_profile = current_user.profile
    except AttributeError:
        # Handle users without profiles
        return redirect('account_logout')

    # Check user type and populate context
    if user_profile.user_type == 'customer':
        context['user_type'] = 'customer'
        context['upcoming_stays'] = []
        context['wishlist'] = []
        context['previous_stays'] = []
    elif user_profile.user_type == 'owner':
        context['user_type'] = 'owner'
        context['requests'] = []
        context['caravans'] = []
        context['reviews'] = []
    else:
        return redirect('account_logout')

    return render(request, 'dashboard/dashboard.html', context)
