from django.shortcuts import render
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "encyclopedia/home.html"


class AllPages(TemplateView):
    template_name = "encyclopedia/all_pages.html"

