from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class SimulationIndexView(TemplateView):
    """
    """
    template_name = 'pages/simIndex.html'


class SimulationView(TemplateView):
    """
    """
    template_name = 'pages/simulation.html'
