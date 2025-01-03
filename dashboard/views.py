from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Q


def dashboard_view(request):
    """
    Renders a single dashboard page for both customers and owners.
    """
    user = request.user
    # Initialise context variables
    context = {}

    # Check user type and populate context
    if user.user_type == 'customer':
        context['user_type'] = 'customer'
        context['upcoming_stays'] = []
        context['wishlist'] = []
        context['previous_stays'] = []
    elif user.user_type == 'owner':
        context['user_type'] = 'owner'
        context['requests'] = []
        context['caravans'] = []
        context['reviews'] = []
    else:
        return redirect('account_logout')
    
    return render(request, 'dashboard/dashboard.html', context)
