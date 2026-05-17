from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventRegistrationForm

def register_event(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Registration Successful!</h2>")
    else:
        form = EventRegistrationForm()
        
    return render(request, 'events/register.html', {'form': form})