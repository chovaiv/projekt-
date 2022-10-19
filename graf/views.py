from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Test

# Creating views
class TestChartView(TemplateView):
    template_name = 'graf/chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Test.objects.all()
        return context