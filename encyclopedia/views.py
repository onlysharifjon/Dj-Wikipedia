from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from encyclopedia.forms import CreatePageForm, EditPageForm
from .models import Page
from .utils import get_random_page
from django.template.defaultfilters import slugify


class HomePage(TemplateView):
    template_name = "encyclopedia/home.html"


class AllPages(ListView):
    model = Page
    context_object_name = 'pages'
    template_name = "encyclopedia/all_pages.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        print(query)
        if query:
            return Page.objects.filter(title__icontains=query)
        else:
            return Page.objects.all()


class CreatePage(CreateView):
    model = Page
    template_name = "encyclopedia/create_page.html"
    form_class = CreatePageForm
    success_url = reverse_lazy("all_pages")

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.cleaned_data['title'])
        return super().form_valid(form)


class DeletePage(DeleteView):
    model = Page
    success_url = reverse_lazy("all_pages")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)


class EditPage(UpdateView):
    model = Page
    template_name = "encyclopedia/edit_page.html"
    form_class = EditPageForm
    success_url = reverse_lazy("all_pages")


class DetailPage(DetailView):
    model = Page
    template_name = "encyclopedia/detail_page.html"


class RandomPage(DetailView):
    model = Page
    template_name = "encyclopedia/detail_page.html"

    def get_object(self, queryset=None):
        random_page = get_random_page(Page.objects.all())
        if random_page is not None:
            return random_page
