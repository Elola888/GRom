from django.contrib import admin
from .models import DailyEntry


@admin.register(DailyEntry)
class DailyEntryAdmin(admin.ModelAdmin):
    """
    Admin interface for DailyEntry model.
    
    Provides convenient viewing and editing of daily entries in the Django admin panel.
    """
    
    list_display = ('date', 'mood', 'has_reflection', 'has_answers')
    list_filter = ('date', 'mood')
    search_fields = ('reflection', 'question_1_answer', 'question_2_answer', 'question_3_answer')
    readonly_fields = ('date', 'ai_feedback')
    ordering = ('-date',)
    
    fieldsets = (
        ('Date', {
            'fields': ('date',)
        }),
        ('Goals & Tasks', {
            'fields': ('goals', 'tasks')
        }),
        ('Reflection Answers', {
            'fields': (
                'question_1_answer',
                'question_2_answer',
                'question_3_answer'
            ),
            'description': 'Structured reflection questions answered by user'
        }),
        ('General Reflection & Mood', {
            'fields': ('reflection', 'mood')
        }),
        ('AI Generated Feedback', {
            'fields': ('ai_feedback',),
            'description': 'Automatically generated based on reflection content'
        }),
    )
    
    def has_reflection(self, obj):
        """Check if entry has reflection text."""
        return bool(obj.reflection)
    has_reflection.short_description = 'Has Reflection'
    has_reflection.boolean = True
    
    def has_answers(self, obj):
        """Check if entry has answers to reflection questions."""
        return bool(obj.question_1_answer or obj.question_2_answer or obj.question_3_answer)
    has_answers.short_description = 'Has Q&A'
    has_answers.boolean = True
