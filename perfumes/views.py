from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from perfumes.models import Perfume


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['perfumes'] = Perfume.objects.all()
        return context
