from django.contrib.auth.decorators import login_required, authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponsePermanentRedirect


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
    else:
        # Return an 'invalid login' error message.

    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)