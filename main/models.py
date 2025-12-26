from django.db import models

MOOD_CHOICES = [
    ('happy', 'Happy'),
    ('ok', 'OK'),
    ('sad', 'Sad'),
    ('stressed', 'Stressed'),
]

class DailyEntry(models.Model):
    """
    Daily journal entry for self-development tracking.
    
    ETHICS NOTICE:
    - No personal identification data collected
    - Single-user, local prototype for academic purposes
    - AI feedback is rule-based, not a medical/psychological diagnosis
    - Data stored locally; no external transmission
    """
    date = models.DateField(auto_now_add=True, unique=True)
    tasks = models.TextField(blank=True)
    reflection = models.TextField(blank=True)
    mood = models.CharField(max_length=20, choices=MOOD_CHOICES, default='ok')
    
    # Structured reflection questions
    question_1_answer = models.TextField(
        blank=True,
        help_text="What went well today?"
    )
    question_2_answer = models.TextField(
        blank=True,
        help_text="What challenged you today?"
    )
    question_3_answer = models.TextField(
        blank=True,
        help_text="What would you improve tomorrow?"
    )
    
    # Personal goals (optional)
    goals = models.TextField(blank=True, help_text="Your goals for today or this week")
    
    # AI-generated feedback
    ai_feedback = models.TextField(blank=True)
    ai_insights = models.TextField(
        blank=True,
        help_text="Structured AI insights: emotions, patterns, and daily summary"
    )

    class Meta:
        ordering = ['-date']
        verbose_name = 'Daily Entry'
        verbose_name_plural = 'Daily Entries'

    def __str__(self):
        return f"Entry for {self.date}"
