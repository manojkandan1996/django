from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ManualContactForm, ContactModelForm

def contact_manual(request):
    if request.method == 'POST':
        form = ManualContactForm(request.POST)
        if form.is_valid():
            messages.success(request, "Thanks for contacting us!")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ManualContactForm()
    return render(request, 'contact_app/contact_form.html', {'form': form})

def contact_modelform(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted!")
            return redirect('home')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = ContactModelForm()
    return render(request, 'contact_app/contact_form.html', {'form': form})
