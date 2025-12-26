# Generated migration for AI Insights feature

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_add_reflection_questions_and_goals'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyentry',
            name='ai_insights',
            field=models.TextField(
                blank=True,
                help_text='Structured AI insights: emotions, patterns, and daily summary'
            ),
        ),
    ]
