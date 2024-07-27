from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Course
from .forms import CourseForm
from django.contrib import messages
from .messages import add_success_message, add_error_message


class CourseListView(ListView):
    model = Course
    template_name = 'my_app/course_list.html'
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'
    context_object_name = 'course'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        messages.success(self.request, add_success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, add_error_message)
        return super().form_invalid(form)

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course_form.html'
    success_url = reverse_lazy('course_list')
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def form_valid(self, form):
        messages.success(self.request, 'Course updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error updating course. Please check the form and try again.')
        return super().form_invalid(form)


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'my_app/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
    slug_url_kwarg = 'slug'
    slug_field = 'slug'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Course deleted successfully.')
        return super().delete(request, *args, **kwargs)



