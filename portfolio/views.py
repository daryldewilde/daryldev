from django.shortcuts import render
from .models import Project, Skill, Experience, Certificate
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView


def portfolio_view(request):
    projects = Project.objects.order_by('-id') 
    skills = Skill.objects.all()
    experiences = Experience.objects.order_by('-start_date')  
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/portfolio.html', {
        "year": 2024,
        "name": "daryldev",
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'certificates': certificates,
    })


def contact_me_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        try:
            send_mail(
                'Contact Form Message',
                f'Email: {email}\n\nMessage:\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                ['nfoyedewilde@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


