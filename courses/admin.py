from django.contrib import admin
from .models import Category, Course, Module, Lesson, Enrollment, Progress

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'category', 'created_at', 'is_published']
    list_filter = ['is_published', 'category']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order']
    list_filter = ['course']
    search_fields = ['title', 'description']
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'module', 'order']
    list_filter = ['module']
    search_fields = ['title', 'content']

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'date_enrolled', 'is_completed']
    list_filter = ['is_completed']
    search_fields = ['student__username', 'course__title']

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['enrollment', 'lesson', 'completed', 'completed_at']
    list_filter = ['completed']
    search_fields = ['enrollment__student__username', 'lesson__title']
