from django.contrib import admin
from .models import Task, TaskTag, TaskSubject, TaskFile, Application, Review


class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ('id', 'author', 'implementer', 'admin_list_applicants', 'title',
                    'difficulty_stage_of_study', 'difficulty_course_of_study',
                    'admin_list_tags', 'subject', 'description', 'status',
                    'created_at', 'stop_accepting_applications_at', 'expires_at')

    fieldsets = (
        ('Task short info', {'fields': ('title', 'price')}),
        ('Author and implementer', {'fields': ('author', 'implementer',)}),
        ('Task info', {'fields': ('description', 'subject', 'tags', 'status',)}),
        ('Difficulty', {'fields': ('difficulty_stage_of_study', 'difficulty_course_of_study',)}),
        ("Dates", {"fields": ('stop_accepting_applications_at', 'expires_at',)}),
        ("Ratings", {"fields": ('author_rating', 'review_on_author', 'implementer_rating', 'review_on_implementer',)}))


class TaskTagAdmin(admin.ModelAdmin):
    model = TaskTag
    list_display = ('id', 'name',)


class TaskSubjectAdmin(admin.ModelAdmin):
    model = TaskSubject
    list_display = ('id', 'name',)


class TaskFileAdmin(admin.ModelAdmin):
    model = TaskFile
    list_display = ('filename', 'file',)

    # fields = [field.name for field in model._meta.fields if field.name != "id"]
    exclude = ('id',)


class ApplicationAdmin(admin.ModelAdmin):
    model = Application
    list_display = ('applicant', 'task', 'status', 'message', 'created_at', 'updated_at',)

    # fields = [field.name for field in model._meta.fields if field.name != "id"]
    exclude = ('id',)


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('reviewer',
                    'task',
                    'review_type',
                    'message',
                    'rating')


# Register your models here.
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskTag, TaskTagAdmin)
admin.site.register(TaskSubject, TaskSubjectAdmin)
admin.site.register(TaskFile, TaskFileAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Review, ReviewAdmin)
