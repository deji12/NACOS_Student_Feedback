from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import StudentFeedback

class StudentFeedbackAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'subject',
        'type',
        'anonymous_message',
        'date_added',
        'addressed'
    ]

    search_fields = [
        'subject',
        'student_name',
        'student_matric_number' 
    ]

    list_filter = [
        'type',
        'addressed',
        'anonymous_message',
        'date_added'
    ]

admin.site.register(StudentFeedback, StudentFeedbackAdmin)