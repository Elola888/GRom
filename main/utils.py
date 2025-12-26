"""
AI Feedback Analysis Module

ETHICS NOTICE:
- Rule-based analysis only (no machine learning or external APIs)
- Designed for self-reflection, not medical/psychological diagnosis
- Patterns detected are for journaling purposes only
- No data is transmitted externally
"""


def analyse_reflection(reflection: str, q1: str = "", q2: str = "", q3: str = "") -> str:
    """
    Analyse daily reflection and structured question answers.
    
    Args:
        reflection: General reflection text
        q1: Answer to "What went well today?"
        q2: Answer to "What challenged you today?"
        q3: Answer to "What would you improve tomorrow?"
    
    Returns:
        Personalized feedback string based on content analysis
    """
    
    # Combine all text for analysis
    all_text = f"{reflection} {q1} {q2} {q3}".lower()
    
    # Empty check
    if not all_text.strip():
        return "Write your reflections to receive personalized insights 🙂"
    
    # Detect patterns
    stress_keywords = ["stress", "stressed", "pressure", "anxious", "worried", "overwhelmed", "difficult", "hard"]
    positive_keywords = ["happy", "grateful", "thankful", "good day", "proud", "accomplished", "progress", "win"]
    improvement_keywords = ["improve", "next time", "better", "improve tomorrow", "work on", "practice"]
    growth_keywords = ["learned", "realized", "understand", "discovered", "growth", "challenge"]
    
    stress_found = any(w in all_text for w in stress_keywords)
    positive_found = any(w in all_text for w in positive_keywords)
    improvement_found = any(w in all_text for w in improvement_keywords)
    growth_found = any(w in all_text for w in growth_keywords)
    
    # Build feedback based on patterns
    feedback_parts = []
    
    # Stress pattern
    if stress_found:
        feedback_parts.append("I noticed you faced some challenges today. Remember to prioritize rest and self-care.")
    
    # Growth mindset pattern
    if improvement_found and growth_found:
        feedback_parts.append("Great reflection mindset! You're actively thinking about growth and improvement. 📈")
    elif improvement_found:
        feedback_parts.append("Excellent—you're thinking about how to improve tomorrow. That's a growth mindset!")
    
    # Positivity pattern
    if positive_found:
        feedback_parts.append("I see positive moments in your day. Keep building on these wins! 👏")
    
    # Challenge processing pattern (positive stress response)
    if q2 and len(q2) > 20 and improvement_found:
        feedback_parts.append("You're reflecting deeply on challenges and planning improvements. That's maturity.")
    
    # Text length indicator
    total_words = len(all_text.split())
    if total_words < 30 and feedback_parts:
        feedback_parts.append("(Consider writing more details for richer insights.)")
    
    # Default feedback if no patterns detected
    if not feedback_parts:
        return "Balanced reflection. Keep tracking your patterns—they reveal insights over time."
    
    return " ".join(feedback_parts)

def generate_insights(reflection: str, q1: str = "", q2: str = "", q3: str = "", mood: str = "") -> str:
    """
    Generate structured AI Insights analyzing emotions, patterns, and daily summary.
    
    This function provides detailed, explainable insights into:
    - Detected emotions (stress, positivity, calm, growth)
    - Behavioral patterns (growth mindset, improvement planning)
    - Daily insight summary
    
    Args:
        reflection: General reflection text
        q1: Answer to "What went well today?"
        q2: Answer to "What challenged you today?"
        q3: Answer to "What would you improve tomorrow?"
        mood: Selected mood (happy, ok, sad, stressed)
    
    Returns:
        Structured insights string with emotions, patterns, and summary
    """
    
    # Combine all text for analysis
    all_text = f"{reflection} {q1} {q2} {q3}".lower()
    
    # Empty check
    if not all_text.strip():
        return "No insights available. Complete your reflection to generate insights."
    
    # Define keywords for emotion detection
    emotion_keywords = {
        'stress': ["stress", "stressed", "pressure", "anxious", "worried", "overwhelmed", "frustrated", "tense"],
        'positivity': ["happy", "grateful", "thankful", "good day", "proud", "accomplished", "progress", "win", "excellent"],
        'calm': ["peaceful", "relaxed", "content", "serene", "calm", "balance", "steady", "composed"],
        'growth': ["learned", "realized", "understand", "discovered", "growth", "development", "improve", "challenge", "evolving"]
    }
    
    # Define keywords for behavioral patterns
    pattern_keywords = {
        'growth_mindset': ["improve", "next time", "better", "work on", "practice", "develop", "strengthen"],
        'improvement_planning': ["improve tomorrow", "plan to", "will focus", "strategy", "approach", "will try"],
        'challenge_awareness': ["challenged", "difficult", "obstacle", "struggle", "complex", "tough"],
        'self_reflection': ["realize", "understand", "see that", "notice", "aware", "recognize"]
    }
    
    # Detect emotions
    detected_emotions = []
    for emotion, keywords in emotion_keywords.items():
        if any(w in all_text for w in keywords):
            detected_emotions.append(emotion)
    
    # Detect behavioral patterns
    detected_patterns = []
    for pattern, keywords in pattern_keywords.items():
        if any(w in all_text for w in keywords):
            detected_patterns.append(pattern)
    
    # Build structured insights
    insights_parts = []
    
    # Section 1: Emotional State
    insights_parts.append("📊 EMOTIONAL ANALYSIS")
    insights_parts.append("─" * 40)
    
    if detected_emotions:
        emotion_text = ", ".join([e.replace('_', ' ') for e in detected_emotions])
        insights_parts.append(f"Emotions Detected: {emotion_text}")
    else:
        insights_parts.append("Emotions Detected: Neutral/Balanced")
    
    # Add mood context if provided
    if mood:
        mood_display = mood.capitalize()
        insights_parts.append(f"Reported Mood: {mood_display}")
    
    # Section 2: Behavioral Patterns
    insights_parts.append("\n💡 BEHAVIORAL PATTERNS")
    insights_parts.append("─" * 40)
    
    if detected_patterns:
        if 'growth_mindset' in detected_patterns:
            insights_parts.append("✓ Growth Mindset: You're oriented toward improvement and learning.")
        if 'improvement_planning' in detected_patterns:
            insights_parts.append("✓ Improvement Planning: You're actively planning concrete next steps.")
        if 'challenge_awareness' in detected_patterns:
            insights_parts.append("✓ Challenge Awareness: You're aware of obstacles and thinking them through.")
        if 'self_reflection' in detected_patterns:
            insights_parts.append("✓ Self-Reflection: You demonstrate deep introspection and self-awareness.")
    else:
        insights_parts.append("No strong behavioral patterns detected. Continue reflecting for pattern emergence.")
    
    # Section 3: Daily Insight Summary
    insights_parts.append("\n🎯 DAILY INSIGHT SUMMARY")
    insights_parts.append("─" * 40)
    
    # Generate summary based on emotion + pattern combination
    summary_text = _generate_summary(detected_emotions, detected_patterns, q2, q3)
    insights_parts.append(summary_text)
    
    return "\n".join(insights_parts)


def _generate_summary(emotions: list, patterns: list, challenge_answer: str = "", improvement_answer: str = "") -> str:
    """
    Generate a personalized daily summary based on detected emotions and patterns.
    
    Helper function for generate_insights().
    """
    summary = []
    
    # Analyze combination of emotions and patterns
    has_stress = 'stress' in emotions
    has_positivity = 'positivity' in emotions
    has_growth = 'growth' in emotions or 'growth_mindset' in patterns
    has_challenges = bool(challenge_answer) and len(challenge_answer) > 10
    planning_improvement = 'improvement_planning' in patterns
    
    # Build narrative summary
    if has_stress and planning_improvement:
        summary.append("You faced stressful moments today but are actively planning improvements.")
        summary.append("This resilience and forward-thinking approach is valuable for growth.")
    elif has_stress:
        summary.append("Stress was present today. Consider what areas need attention or support.")
        summary.append("Reflecting on these moments helps build resilience over time.")
    
    if has_positivity:
        summary.append("Positive moments were evident. Acknowledging these builds momentum and confidence.")
    
    if has_challenges and has_growth:
        summary.append("Your approach to challenges shows a learning orientation.")
        summary.append("This pattern supports continuous personal development.")
    elif has_challenges:
        summary.append("Challenges were present. How can you extract learning from these?")
    
    if has_growth:
        summary.append("You demonstrated growth mindset thinking today. Keep nurturing this perspective.")
    
    # Final encouragement if multiple patterns
    if len(patterns) >= 2:
        summary.append("\nYour reflections show thoughtful self-awareness. You're building strong habits.")
    elif not summary:
        summary.append("Balanced day. Patterns will become clearer with consistent journaling.")
    
    return " ".join(summary) if summary else "Balanced day. Patterns will become clearer with consistent journaling."