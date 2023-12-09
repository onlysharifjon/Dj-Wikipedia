from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from encyclopedia.forms import CreatePageForm
from .models import Page
from .utils import generate_captcha


class HomePage(TemplateView):
    template_name = "encyclopedia/home.html"


class AllPages(TemplateView):
    template_name = "encyclopedia/all_pages.html"


class CreatePage(CreateView):
    model = Page
    template_name = "encyclopedia/create_page.html"
    form_class = CreatePageForm
    success_url = reverse_lazy("all_pages")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['captcha'] = generate_captcha()
        return context

    def form_valid(self, form, **kwargs):
        captcha_answer = self.get_form_kwargs()
        correct_answer = eval(self.get_context_data(**kwargs)['captcha'])
        print(captcha_answer['data']['captcha'], correct_answer)
        if captcha_answer == correct_answer:
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
