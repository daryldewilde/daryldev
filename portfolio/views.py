from django.shortcuts import render
from .models import Project, Skill, Experience, Certificate
from django.http import JsonResponse
from xhtml2pdf import pisa
import io
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView


def portfolio_view(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.order_by('-start_date')  # Order by start_date descending
    certificates = Certificate.objects.all()
    return render(request, 'portfolio/portfolio.html', {
        "year": 2024,
        "name": "daryldev",
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'certificates': certificates,
        "is_pwa": True,
    })


def render_pdf_view(request):
    # Fetching data from the models
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()

    # Define context with resume data
    context = {
        "year":2024,
        "name": "daryldev",
        "email": "nfoyedewilde@gmail.com",
        "phone": "+237 699255753",
        "skills": skills,
        "projects": projects,
        "experiences": experiences,
        "is_pwa": True,
    }

    # Render HTML template with context data
    template_path = 'portfolio/resume_template.html'
    html = render(request, template_path, context).content.decode()

    # Create a PDF file from the HTML
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="portfolio.pdf"'

    # Use pisa to convert HTML to PDF and save in the response object
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    
    return response


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


