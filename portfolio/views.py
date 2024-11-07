from django.shortcuts import render
from .models import Project, Skill, Experience
from django.shortcuts import render
from django.http import HttpResponse
from xhtml2pdf import pisa
import io




def portfolio_view(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'portfolio/portfolio.html', {
        "year":2024,
        "name": "daryldev",
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
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
