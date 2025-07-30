from django.shortcuts import render

# Create your views here.
def business_card(request):
    context = {
        'name': 'VANISHREE',
        'title': 'Full-Stack Developer',
        'bio': 'Passionate about building beautiful and scalable web applications.',
        'email': 'vani@example.com',
        'phone': '+1 234 567 8901',
        'location': 'New York, USA',
        'linkedin': 'https://linkedin.com/in/janedoe',
        'github': 'https://github.com/janedoe',
        'image': 'card/images/profile.jpg'
    }
    return render(request, 'card/card.html', context)