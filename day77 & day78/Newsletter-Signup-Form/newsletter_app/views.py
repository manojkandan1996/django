# newsletter_app/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberModelForm, SubscriberManualForm
from .models import Subscriber

# ModelForm-based view
def subscribe_model_form(request):
    if request.method == 'POST':
        form = SubscriberModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully subscribed!")
            return redirect('subscribe-model')
    else:
        form = SubscriberModelForm()
    return render(request, 'newsletter_app/subscribe_model.html', {'form': form})

# Manual form-based view
def subscribe_manual_form(request):
    if request.method == 'POST':
        form = SubscriberManualForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            if Subscriber.objects.filter(email=email).exists():
                messages.error(request, "This email is already subscribed.")
            else:
                Subscriber.objects.create(name=name, email=email)
                messages.success(request, "Successfully subscribed!")
                return redirect('subscribe-manual')
    else:
        form = SubscriberManualForm()
    return render(request, 'newsletter_app/subscribe_manual.html', {'form': form})
