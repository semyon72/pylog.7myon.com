# Project: blog_7myon_com
# Package: 
# Filename: blog.py
# Generated: 2020 Oct 13 at 15:11 
# Description of <blog>
#
# @author Semyon Mamonov <semyon.mamonov@gmail.com>

from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, UpdateView, DetailView
from django.views.generic.base import ContextMixin
from django.forms import TextInput

from blog.forms.base.blog import BlogModelForm, BlogFilterForm
from blog.models import Blog

from sm_flexdata.views import FilteredListView
from sm_flexdata.model_helpers import model_to_data

from . import CommonGenericViewsAttributeMixin


class BlogView(ContextMixin, FilteredListView):
    template_name = 'blog/base/blog/list.html'
    default_filter_form = BlogFilterForm
    model = Blog
    per_page = 20

    def setup_autogenerated_filter_form(self, fields):
        super().setup_autogenerated_filter_form(fields)
        tagline = fields['tagline']
        tagline.widget = TextInput(attrs = tagline.widget.attrs)

    def get_context(self, queryset=None):
        context = super().get_context(queryset)
        context['form'] = context['filter_form']
        return context


class BlogCommonAttributeMixin(CommonGenericViewsAttributeMixin):
    model = Blog
    form_class = BlogModelForm


class BlogCreateView(BlogCommonAttributeMixin, CreateView):
    template_name = 'blog/staff/blog/edit.html'


class BlogDetailView(BlogCommonAttributeMixin, DetailView):
    template_name = 'blog/staff/blog/detail.html'


class BlogUpdateView(BlogCommonAttributeMixin, UpdateView):
    template_name = 'blog/staff/blog/edit.html'


class BlogDeleteView(BlogCommonAttributeMixin, DeleteView):
    template_name = 'blog/staff/blog/delete.html'
