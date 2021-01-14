# Django
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'core/landing_page.html'
    