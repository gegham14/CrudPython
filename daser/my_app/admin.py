from django.contrib import admin
from .models import Course,Category


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'price', 'duration', 'created_at', 'updated_at')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'updated_at')


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
