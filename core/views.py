from django.shortcuts import render
from .models import Experience, Skill, Project, SocialLink, Education


def index(request):
    experiences = Experience.objects.all()
    skills = Skill.objects.all()

    skills_by_category = {}
    for skill in skills:
        cat = skill.get_category_display()
        skills_by_category.setdefault(cat, []).append(skill)

    projects = Project.objects.all()
    social_links = SocialLink.objects.all()
    educations = Education.objects.all()

    return render(request, 'core/index.html', {
        'experiences': experiences,
        'skills_by_category': skills_by_category,
        'projects': projects,
        'social_links': social_links,
        'educations': educations,
    })
