from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from courses.models import Course, Category

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_courses'] = Course.objects.filter(is_published=True)[:6]
        context['categories'] = Category.objects.all()[:8]
        return context

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ContactView(TemplateView):
    template_name = 'core/contact.html'
