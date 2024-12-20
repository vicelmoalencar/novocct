from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from .models import Course, Lesson, Enrollment, Progress

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 12

    def get_queryset(self):
        queryset = Course.objects.filter(is_published=True)
        category = self.request.GET.get('categoria')
        if category:
            queryset = queryset.filter(category__name=category)
        return queryset

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['is_enrolled'] = Enrollment.objects.filter(
                student=self.request.user,
                course=self.object
            ).exists()
        return context

class LessonDetailView(LoginRequiredMixin, DetailView):
    model = Lesson
    template_name = 'courses/lesson_detail.html'
    context_object_name = 'lesson'

    def get_object(self):
        return get_object_or_404(
            Lesson,
            id=self.kwargs['lesson_id'],
            module__course__slug=self.kwargs['course_slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.object.module.course
        enrollment = get_object_or_404(Enrollment, student=self.request.user, course=course)
        
        # Marca a lição como concluída se ainda não estiver
        progress, created = Progress.objects.get_or_create(
            enrollment=enrollment,
            lesson=self.object,
            defaults={'completed': True, 'completed_at': timezone.now()}
        )
        
        # Obtém todas as lições do curso para navegação
        context['course'] = course
        context['module'] = self.object.module
        return context

class EnrollCourseView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=kwargs['slug'])
        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user,
            course=course
        )
        
        if created:
            messages.success(request, f'Você foi matriculado com sucesso no curso {course.title}!')
        else:
            messages.info(request, f'Você já está matriculado no curso {course.title}.')
        
        return redirect('courses:course_detail', slug=course.slug)

class MyCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'courses/my_courses.html'
    context_object_name = 'enrollments'
    paginate_by = 12

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user).select_related('course')
