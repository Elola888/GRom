from datetime import date
from django.shortcuts import render, redirect
from .models import DailyEntry
from .utils import analyse_reflection, generate_insights


def index(request):
    """
    Display and handle daily entry form.
    
    - Retrieves or creates today's entry
    - Processes form submission with all reflection fields
    - Generates AI feedback based on all inputs
    """
    today = date.today()
    entry, created = DailyEntry.objects.get_or_create(date=today)

    if request.method == 'POST':
        entry.tasks = request.POST.get('tasks', '')
        entry.reflection = request.POST.get('reflection', '')
        entry.question_1_answer = request.POST.get('question_1_answer', '')
        entry.question_2_answer = request.POST.get('question_2_answer', '')
        entry.question_3_answer = request.POST.get('question_3_answer', '')
        entry.goals = request.POST.get('goals', '')
        entry.mood = request.POST.get('mood', 'ok')
        
        # Generate AI feedback and insights considering all inputs
        entry.ai_feedback = analyse_reflection(
            reflection=entry.reflection,
            q1=entry.question_1_answer,
            q2=entry.question_2_answer,
            q3=entry.question_3_answer
        )
        entry.ai_insights = generate_insights(
            reflection=entry.reflection,
            q1=entry.question_1_answer,
            q2=entry.question_2_answer,
            q3=entry.question_3_answer,
            mood=entry.mood
        )
        entry.save()
        return redirect('index')

    return render(request, 'index.html', {'entry': entry})

