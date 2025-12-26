# GRom – Quick Reference Guide

## 🚀 Quick Start

```bash
# Activate environment
.\env\Scripts\activate

# Run server
python manage.py runserver

# Run tests
python manage.py test main.tests --verbosity=2

# Create superuser (admin access)
python manage.py createsuperuser

# Apply migrations
python manage.py migrate
```

---

## 📊 Data Model at a Glance

**DailyEntry** (one per day):
```
date: DateField (auto_now_add=True, unique=True)
tasks: TextField (optional)
reflection: TextField (optional)
goals: TextField (optional) ← NEW
question_1_answer: TextField ← NEW (What went well?)
question_2_answer: TextField ← NEW (What challenged you?)
question_3_answer: TextField ← NEW (What would you improve?)
mood: CharField (choices: happy, ok, sad, stressed)
ai_feedback: TextField (auto-generated)
```

---

## 🔄 Data Flow

```
User Input (Form)
    ↓
POST to index view (main/views.py:index)
    ↓
Save all fields to DailyEntry model
    ↓
Call analyse_reflection() with all inputs
    ↓
Generate ai_feedback using keyword patterns
    ↓
Save entry to database (SQLite)
    ↓
Redirect to GET to display updated entry
    ↓
Template displays all saved data
```

---

## 🧠 AI Feedback Pattern Detection

**Stress Patterns**
```
Keywords: stress, anxious, pressure, overwhelmed, difficult, hard
→ Feedback: Suggests self-care and rest
```

**Positivity Patterns**
```
Keywords: happy, grateful, proud, accomplished, win, progress
→ Feedback: Encourages continuation of positive patterns
```

**Growth Patterns**
```
Keywords: learned, realized, discovered, growth, understand
→ Feedback: Celebrates development mindset
```

**Improvement Patterns**
```
Keywords: improve, better, next time, practice, work on
→ Feedback: Recognizes growth-oriented thinking
```

---

## 📝 File Organization

| File | Purpose | Key Content |
|------|---------|------------|
| `main/models.py` | Data model | DailyEntry + MOOD_CHOICES |
| `main/views.py` | Request handling | index view with form processing |
| `main/utils.py` | AI logic | analyse_reflection() function |
| `main/tests.py` | Testing | 19 unit tests |
| `main/admin.py` | Admin interface | DailyEntryAdmin with custom display |
| `templates/index.html` | UI | Form + display cards |
| `README.md` | Documentation | Comprehensive user guide |
| `ETHICS.md` | Ethics & privacy | Data practices and limitations |
| `PROJECT_OVERVIEW.md` | Architecture | Project structure overview |

---

## 🧪 Test Commands

```bash
# Run all tests
python manage.py test main.tests

# Run with verbose output
python manage.py test main.tests --verbosity=2

# Run specific test class
python manage.py test main.tests.DailyEntryModelTests
python manage.py test main.tests.AnalyseReflectionTests
python manage.py test main.tests.DailyEntryViewTests

# Run specific test method
python manage.py test main.tests.DailyEntryModelTests.test_create_daily_entry

# Run with keepdb (faster repeated runs)
python manage.py test main.tests --keepdb
```

---

## 🔧 Common Development Tasks

### Add a New Field to DailyEntry
```python
# 1. Edit main/models.py
class DailyEntry(models.Model):
    # ... existing fields ...
    new_field = models.TextField(blank=True)

# 2. Create migration
python manage.py makemigrations

# 3. Apply migration
python manage.py migrate

# 4. Update views.py if needed
# 5. Update templates/index.html if user input needed
# 6. Add tests in main/tests.py
```

### Modify AI Feedback Logic
```python
# Edit main/utils.py:analyse_reflection()
# 1. Add new keywords to detect
# 2. Add pattern combination logic
# 3. Update docstring with examples
# 4. Add tests in main/tests.py to verify

# Test it
python manage.py test main.tests.AnalyseReflectionTests
```

### Update the User Interface
```python
# Edit templates/index.html
# Uses Bootstrap 5 CSS framework
# Template variables available:
#   - entry.date
#   - entry.tasks
#   - entry.reflection
#   - entry.question_1_answer
#   - entry.question_2_answer
#   - entry.question_3_answer
#   - entry.goals
#   - entry.mood
#   - entry.ai_feedback
```

---

## 📋 Feedback Examples

| User Input | Keywords Detected | Generated Feedback |
|-----------|------------------|-------------------|
| "Had challenges but learned a lot" | growth, improvement | "Celebrates growth mindset" |
| "Felt stressed about deadline" | stress | "Suggests self-care" |
| "Great day, very grateful" | positivity | "Encourages continuation" |
| "Will improve by planning better" | improvement | "Recognizes progress mindset" |

---

## 🐛 Debug Tips

### Check Database State
```bash
# Django shell to query database
python manage.py shell

# Inside shell:
from main.models import DailyEntry
from datetime import date
entry = DailyEntry.objects.get(date=date.today())
print(entry.question_1_answer)
print(entry.ai_feedback)
```

### View SQL Queries
```python
# In settings.py, add:
LOGGING = {
    'version': 1,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
```

### Test Feedback Generation
```python
# In Django shell:
from main.utils import analyse_reflection

feedback = analyse_reflection(
    reflection="",
    q1="Had a great day today",
    q2="Faced some challenges",
    q3="Will improve by planning better"
)
print(feedback)
```

---

## 📊 Admin Interface

**Access**: `http://localhost:8000/admin/`

**Features**:
- View all entries ordered by date (newest first)
- Filter by date range or mood
- Search reflection content and answers
- Edit entry fields directly
- Admin-friendly display with boolean indicators

**Admin URL**: `/admin/main/dailyentry/`

---

## 🔐 Security Checklist

**Current Development**
- ✅ CSRF protection enabled
- ✅ Secret key protected (but hardcoded - fix for production)
- ⚠️ DEBUG = True (must be False for production)
- ⚠️ No authentication (single-user only)

**For Production**
- [ ] Set DEBUG = False
- [ ] Use environment variable for SECRET_KEY
- [ ] Configure ALLOWED_HOSTS
- [ ] Add authentication system
- [ ] Use PostgreSQL instead of SQLite
- [ ] Enable HTTPS/SSL
- [ ] Implement proper password hashing
- [ ] Add security headers
- [ ] Set up logging and monitoring

---

## 📚 Key Classes & Functions

### Models (main/models.py)
```python
class DailyEntry(models.Model):
    # Main data model for daily entries
    # Unique constraint on date field
    # Methods: __str__(), get_or_create()
```

### Views (main/views.py)
```python
def index(request):
    # GET: Display form and saved entry
    # POST: Save form data and generate feedback
```

### Utils (main/utils.py)
```python
def analyse_reflection(reflection: str, q1: str = "", q2: str = "", q3: str = "") -> str:
    # Rule-based pattern detection
    # Returns personalized feedback string
    # Keywords: stress, positive, growth, improvement
```

### Admin (main/admin.py)
```python
@admin.register(DailyEntry)
class DailyEntryAdmin(admin.ModelAdmin):
    # Custom admin interface
    # List display, filters, search, fieldsets
```

---

## 🚨 Common Errors & Solutions

**Error**: "No such table: main_dailyentry"
```bash
Solution: python manage.py migrate
```

**Error**: "Port 8000 already in use"
```bash
Solution: python manage.py runserver 8001
```

**Error**: Database IntegrityError on POST
```bash
Solution: Check that date is unique
# Or check that form POSTs to correct URL
```

**Error**: Tests fail with "ModuleNotFoundError"
```bash
Solution: Ensure all imports in tests.py are correct
# Check that main app is in INSTALLED_APPS
```

---

## 📱 Form Fields Reference

### HTML Form Fields
```html
<input type="hidden" name="date">                    <!-- Auto-set by model -->
<textarea name="goals">...</textarea>                 <!-- Optional -->
<textarea name="tasks">...</textarea>                 <!-- Optional -->
<textarea name="question_1_answer">...</textarea>     <!-- What went well? -->
<textarea name="question_2_answer">...</textarea>     <!-- What challenged? -->
<textarea name="question_3_answer">...</textarea>     <!-- Improve tomorrow? -->
<textarea name="reflection">...</textarea>            <!-- General reflection -->
<select name="mood">                                  <!-- happy, ok, sad, stressed -->
<button type="submit">Save / Update Entry</button>
```

---

## 🔄 Git Commands (if using version control)

```bash
# Check status
git status

# Stage changes
git add .

# Commit
git commit -m "Add reflection questions and AI feedback"

# View history
git log --oneline

# Create branch for new features
git checkout -b feature/export-to-pdf
```

---

## 🎯 Next Steps / Ideas

**To Extend GRom**:
1. Add weekly summary view
2. Export entries as PDF (ReportLab available)
3. Add mood statistics dashboard
4. Implement history/timeline view
5. Add habit tracking system
6. Create data export (CSV/JSON)
7. Add dark mode
8. Implement search functionality
9. Add multi-user support with authentication
10. Create API for mobile app

---

**Last Updated**: December 2025
**Version**: 1.0 (After Major Enhancement)
