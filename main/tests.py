from django.test import TestCase, Client
from django.utils import timezone
from datetime import date, timedelta
from .models import DailyEntry
from .utils import analyse_reflection, generate_insights


class DailyEntryModelTests(TestCase):
    """Test DailyEntry model functionality."""
    
    def test_create_daily_entry(self):
        """Test creating a new daily entry."""
        entry = DailyEntry.objects.create(
            date=date.today(),
            tasks="Task 1\nTask 2",
            mood="ok"
        )
        self.assertEqual(entry.date, date.today())
        self.assertEqual(entry.mood, "ok")
        self.assertEqual(entry.tasks, "Task 1\nTask 2")
    
    def test_unique_date_constraint(self):
        """Test that only one entry per day is allowed."""
        today = date.today()
        
        # Create first entry
        entry1 = DailyEntry.objects.create(
            date=today,
            tasks="First entry"
        )
        
        # Attempt to create second entry for same date
        with self.assertRaises(Exception):  # IntegrityError
            entry2 = DailyEntry.objects.create(
                date=today,
                tasks="Second entry"
            )
    
    def test_get_or_create_behavior(self):
        """Test that get_or_create returns same entry when called multiple times."""
        today = date.today()
        
        entry1, created1 = DailyEntry.objects.get_or_create(date=today)
        self.assertTrue(created1)
        
        entry2, created2 = DailyEntry.objects.get_or_create(date=today)
        self.assertFalse(created2)
        self.assertEqual(entry1.id, entry2.id)
    
    def test_default_mood_value(self):
        """Test that mood defaults to 'ok'."""
        entry = DailyEntry.objects.create(date=date.today())
        self.assertEqual(entry.mood, "ok")
    
    def test_reflection_questions_fields(self):
        """Test that all reflection question fields save correctly."""
        entry = DailyEntry.objects.create(
            date=date.today(),
            question_1_answer="Today was productive",
            question_2_answer="Had some difficult meetings",
            question_3_answer="Will focus more on breaks tomorrow"
        )
        
        self.assertEqual(entry.question_1_answer, "Today was productive")
        self.assertEqual(entry.question_2_answer, "Had some difficult meetings")
        self.assertEqual(entry.question_3_answer, "Will focus more on breaks tomorrow")
    
    def test_goals_field(self):
        """Test that goals field saves correctly."""
        entry = DailyEntry.objects.create(
            date=date.today(),
            goals="Complete project milestone\nExercise for 30 minutes"
        )
        self.assertEqual(entry.goals, "Complete project milestone\nExercise for 30 minutes")
    
    def test_str_representation(self):
        """Test string representation of entry."""
        entry = DailyEntry.objects.create(date=date.today())
        expected_str = f"Entry for {date.today()}"
        self.assertEqual(str(entry), expected_str)
    
    def test_blank_fields_allowed(self):
        """Test that optional fields can be blank."""
        entry = DailyEntry.objects.create(date=date.today())
        self.assertEqual(entry.tasks, "")
        self.assertEqual(entry.reflection, "")
        self.assertEqual(entry.question_1_answer, "")
        self.assertEqual(entry.question_2_answer, "")
        self.assertEqual(entry.question_3_answer, "")
        self.assertEqual(entry.goals, "")
        self.assertEqual(entry.ai_feedback, "")
        self.assertEqual(entry.ai_insights, "")
    
    def test_ai_insights_field(self):
        """Test that ai_insights field saves correctly."""
        entry = DailyEntry.objects.create(
            date=date.today(),
            ai_insights="Generated insights text"
        )
        self.assertEqual(entry.ai_insights, "Generated insights text")


class AnalyseReflectionTests(TestCase):
    """Test the AI feedback analysis function."""
    
    def test_empty_reflection(self):
        """Test feedback for empty inputs."""
        feedback = analyse_reflection("", "", "", "")
        self.assertIn("Write your reflections", feedback)
    
    def test_stress_pattern_detection(self):
        """Test that stress keywords trigger appropriate feedback."""
        feedback = analyse_reflection(
            reflection="",
            q1="",
            q2="Today was very stressed and overwhelming",
            q3=""
        )
        self.assertIn("challenges", feedback.lower())
        self.assertIn("self-care", feedback.lower())
    
    def test_positive_pattern_detection(self):
        """Test that positive keywords trigger encouraging feedback."""
        feedback = analyse_reflection(
            reflection="",
            q1="Had a great day, very grateful for good news",
            q2="",
            q3=""
        )
        self.assertIn("positive", feedback.lower())
    
    def test_improvement_mindset_pattern(self):
        """Test that improvement keywords trigger growth feedback."""
        feedback = analyse_reflection(
            reflection="",
            q1="",
            q2="Found it hard to focus",
            q3="I will improve by starting earlier and taking more breaks"
        )
        self.assertIn("growth", feedback.lower())
    
    def test_growth_and_improvement_combined(self):
        """Test feedback when both growth and improvement are detected."""
        feedback = analyse_reflection(
            reflection="",
            q1="",
            q2="Faced a technical challenge",
            q3="Learned a new approach and will practice it tomorrow"
        )
        # Should contain growth-related feedback
        self.assertTrue(len(feedback) > 20)
    
    def test_short_reflection_length_warning(self):
        """Test feedback for very short responses."""
        feedback = analyse_reflection(
            reflection="ok",
            q1="good",
            q2="",
            q3=""
        )
        # Should either suggest more detail or give balanced feedback
        self.assertTrue(len(feedback) > 10)
    
    def test_comprehensive_reflection(self):
        """Test feedback with comprehensive input."""
        feedback = analyse_reflection(
            reflection="Today was a mixed day with ups and downs",
            q1="I accomplished my main project milestone",
            q2="Had some stressed moments during the afternoon meeting",
            q3="I will improve by taking a short break before important meetings"
        )
        # Should provide meaningful feedback
        self.assertTrue(len(feedback) > 30)
        # Should not be generic default
        self.assertNotIn("Balanced reflection", feedback)


class GenerateInsightsTests(TestCase):
    """Test the AI Insights generation function."""
    
    def test_empty_insights(self):
        """Test insights generation with empty inputs."""
        insights = generate_insights("", "", "", "", "")
        self.assertIn("No insights available", insights)
    
    def test_emotion_detection_stress(self):
        """Test that stress emotions are detected."""
        insights = generate_insights(
            reflection="",
            q1="",
            q2="Today was very stressful and anxious",
            q3="",
            mood="stressed"
        )
        self.assertIn("EMOTIONAL ANALYSIS", insights)
        self.assertIn("stress", insights.lower())
        self.assertIn("Reported Mood: Stressed", insights)
    
    def test_emotion_detection_positivity(self):
        """Test that positive emotions are detected."""
        insights = generate_insights(
            reflection="",
            q1="Had a great day, feeling grateful and accomplished",
            q2="",
            q3="",
            mood="happy"
        )
        self.assertIn("positivity", insights.lower())
        self.assertIn("Reported Mood: Happy", insights)
    
    def test_emotion_detection_growth(self):
        """Test that growth emotions are detected."""
        insights = generate_insights(
            reflection="",
            q1="",
            q2="",
            q3="Learned from this challenge and will improve next time",
            mood=""
        )
        self.assertIn("growth", insights.lower())
    
    def test_behavioral_pattern_growth_mindset(self):
        """Test detection of growth mindset pattern."""
        insights = generate_insights(
            reflection="",
            q1="",
            q2="Had difficulty with focus",
            q3="I will improve by practicing better time management",
            mood=""
        )
        self.assertIn("BEHAVIORAL PATTERNS", insights)
        self.assertIn("Growth Mindset", insights)
    
    def test_behavioral_pattern_improvement_planning(self):
        """Test detection of improvement planning pattern."""
        insights = generate_insights(
            reflection="",
            q1="",
            q2="",
            q3="I will focus on delegating tasks and improving work-life balance",
            mood=""
        )
        self.assertIn("Improvement Planning", insights)
    
    def test_behavioral_pattern_self_reflection(self):
        """Test detection of self-reflection pattern."""
        insights = generate_insights(
            reflection="I realize today showed me the importance of asking for help",
            q1="",
            q2="",
            q3="",
            mood=""
        )
        self.assertIn("Self-Reflection", insights)
    
    def test_insights_contains_all_sections(self):
        """Test that comprehensive insights contain all sections."""
        insights = generate_insights(
            reflection="Today was challenging but I learned a lot",
            q1="Had some good moments",
            q2="Faced obstacles and stress",
            q3="Will improve by practicing patience",
            mood="ok"
        )
        # Should contain all three main sections
        self.assertIn("EMOTIONAL ANALYSIS", insights)
        self.assertIn("BEHAVIORAL PATTERNS", insights)
        self.assertIn("DAILY INSIGHT SUMMARY", insights)
    
    def test_insights_with_combined_patterns(self):
        """Test insights with multiple patterns."""
        insights = generate_insights(
            reflection="Mixed day with learning",
            q1="Accomplished a key milestone",
            q2="Had stressful moments but learning from them",
            q3="Will improve focus by taking more breaks",
            mood="ok"
        )
        # Should recognize multiple patterns
        self.assertIn("stress", insights.lower())
        self.assertIn("positivity", insights.lower())
        self.assertIn("growth", insights.lower())
        # Should mention resilience and momentum
        self.assertIn("resilience", insights.lower())
        self.assertIn("momentum", insights.lower())
    
    def test_insights_structured_format(self):
        """Test that insights are properly formatted with sections."""
        insights = generate_insights(
            reflection="Good day with lessons",
            q1="Learned something new",
            q2="",
            q3="",
            mood=""
        )
        # Should have section headers and separators
        self.assertIn("📊", insights)  # Emoji for emotional analysis
        self.assertIn("💡", insights)  # Emoji for patterns
        self.assertIn("🎯", insights)  # Emoji for summary


class DailyEntryViewTests(TestCase):
    """Test the view logic for daily entries."""
    
    def setUp(self):
        self.client = Client()
        self.url = '/'
    
    def test_index_view_get_request(self):
        """Test that GET request returns 200 and uses correct template."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_index_view_creates_entry_if_not_exists(self):
        """Test that view creates today's entry if it doesn't exist."""
        today = date.today()
        # Ensure no entry exists
        DailyEntry.objects.filter(date=today).delete()
        
        response = self.client.get(self.url)
        
        # Check that entry was created
        self.assertTrue(DailyEntry.objects.filter(date=today).exists())
    
    def test_post_saves_all_fields(self):
        """Test that POST request saves all form fields."""
        today = date.today()
        DailyEntry.objects.filter(date=today).delete()
        
        data = {
            'tasks': 'Test task 1\nTest task 2',
            'reflection': 'Test reflection',
            'question_1_answer': 'What went well answer',
            'question_2_answer': 'Challenge answer',
            'question_3_answer': 'Improvement answer',
            'goals': 'Test goals',
            'mood': 'happy'
        }
        
        response = self.client.post(self.url, data)
        
        # Check redirect
        self.assertEqual(response.status_code, 302)
        
        # Check that entry was saved with all fields
        entry = DailyEntry.objects.get(date=today)
        self.assertEqual(entry.tasks, 'Test task 1\nTest task 2')
        self.assertEqual(entry.reflection, 'Test reflection')
        self.assertEqual(entry.question_1_answer, 'What went well answer')
        self.assertEqual(entry.question_2_answer, 'Challenge answer')
        self.assertEqual(entry.question_3_answer, 'Improvement answer')
        self.assertEqual(entry.goals, 'Test goals')
        self.assertEqual(entry.mood, 'happy')
    
    def test_ai_feedback_is_generated(self):
        """Test that AI feedback is generated on POST."""
        today = date.today()
        DailyEntry.objects.filter(date=today).delete()
        
        data = {
            'question_1_answer': 'Very happy and grateful today',
            'question_2_answer': '',
            'question_3_answer': '',
            'mood': 'happy'
        }
        
        response = self.client.post(self.url, data)
        
        entry = DailyEntry.objects.get(date=today)
        # Feedback should be generated
        self.assertTrue(len(entry.ai_feedback) > 0)
    
    def test_ai_insights_are_generated(self):
        """Test that AI insights are generated on POST."""
        today = date.today()
        DailyEntry.objects.filter(date=today).delete()
        
        data = {
            'question_1_answer': 'Had a productive day with good progress',
            'question_2_answer': 'Faced some stress during meetings',
            'question_3_answer': 'Will improve by taking more breaks',
            'mood': 'ok'
        }
        
        response = self.client.post(self.url, data)
        
        entry = DailyEntry.objects.get(date=today)
        # Insights should be generated
        self.assertTrue(len(entry.ai_insights) > 0)
        # Insights should contain structured sections
        self.assertIn("EMOTIONAL ANALYSIS", entry.ai_insights)
        self.assertIn("BEHAVIORAL PATTERNS", entry.ai_insights)
