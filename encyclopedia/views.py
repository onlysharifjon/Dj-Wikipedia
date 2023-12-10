from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from encyclopedia.forms import CreatePageForm
from .models import Page
from .utils import generate_captcha


class HomePage(TemplateView):
    template_name = "encyclopedia/home.html"


class AllPages(ListView):
    model = Page
    context_object_name = 'pages'
    template_name = "encyclopedia/all_pages.html"


class CreatePage(CreateView):
    model = Page
    template_name = "encyclopedia/create_page.html"
    form_class = CreatePageForm
    success_url = reverse_lazy("all_pages")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeletePage(DeleteView):
    model = Page
    success_url = reverse_lazy("all_pages")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)
