# GRom – Daily Self-Development Journal with AI Feedback

An academic prototype Django application for structured daily journaling with rule-based AI feedback. Designed for university projects and personal self-reflection tracking.

---

## 🎯 Project Overview

GRom helps users:
- **Track daily progress** through structured tasks and goals
- **Reflect deeply** using guided reflection questions
- **Monitor emotional patterns** with mood tracking
- **Receive personalized insights** via rule-based AI feedback

---

## ⚖️ ETHICAL FRAMEWORK

### 🔒 Data Privacy

- **No personal identification** collected or stored
- **No authentication system** – single-user, local prototype
- **No data transmission** – everything stays on your machine
- **SQLite database** – local file-based storage only
- **No third-party APIs** – all processing is internal

### 🏫 Academic Purpose

This is a **university foundation project** demonstrating:
- Django web framework fundamentals
- Database modeling best practices
- User interface design patterns
- Rule-based feedback systems (not machine learning)

### ⚠️ Limitations

**The AI feedback is NOT:**
- Medical or psychological diagnosis
- Mental health professional advice
- A substitute for professional help
- Based on machine learning or external services

**The AI feedback IS:**
- Pattern recognition based on keyword analysis
- Designed for journaling and self-reflection purposes only
- Rule-based and transparent (see `utils.py`)
- Informational and supportive in tone

---

## 🚀 Features

### 1. **Structured Daily Entry Form**
   - Goals (optional)
   - Task list
   - Three guided reflection questions
   - General reflection
   - Mood selection (Happy, OK, Sad, Stressed)

### 2. **Three Reflection Questions**
   - "What went well today?" – Highlights positives
   - "What challenged you today?" – Acknowledges difficulties
   - "What would you improve tomorrow?" – Builds growth mindset

### 3. **Rule-Based AI Feedback**
   Analyzes all inputs for patterns:
   - **Stress detection** → Suggests self-care
   - **Positivity detection** → Encourages continuation
   - **Growth mindset** → Recognizes improvement orientation
   - **Learning patterns** → Celebrates growth

### 4. **One Entry Per Day**
   - Unique date constraint prevents duplicates
   - Users can update today's entry multiple times
   - Historical entries persist in database

---

## 📋 Database Model

### DailyEntry
```
Field                    Type        Notes
─────────────────────────────────────────────
date                   DateField    Auto-set, unique per day
tasks                  TextField    Optional
reflection             TextField    Optional
mood                   CharField    (happy, ok, sad, stressed)
question_1_answer      TextField    "What went well?"
question_2_answer      TextField    "What challenged you?"
question_3_answer      TextField    "What would you improve?"
goals                  TextField    Optional
ai_feedback            TextField    Auto-generated analysis
```

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|------------|
| Framework | Django 5.2 |
| Database | SQLite3 |
| Frontend | Bootstrap 5, HTML, CSS |
| Environment | Python 3.x (venv) |
| Server | Gunicorn (production-ready) |
| WSGI | Django's built-in WSGI |

### Key Dependencies
- **asgiref** – ASGI/WSGI compatibility
- **Pillow** – Image processing
- **ReportLab** – PDF generation
- **Requests** – HTTP library
- **whitenoise** – Static file serving
- **python-dotenv** – Environment variables

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.8+ installed
- Git (optional)

### Steps

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd GRom
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv env
   .\env\Scripts\activate
   
   # macOS/Linux
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional, for admin panel)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Start development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main app: `http://localhost:8000/`
   - Admin panel: `http://localhost:8000/admin/` (if superuser created)

---

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
python manage.py test

# Run with verbose output
python manage.py test --verbosity=2

# Run specific test class
python manage.py test main.tests.DailyEntryModelTests

# Run with coverage (if coverage installed)
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

### Test Coverage Includes

- **Model Tests**: Creation, constraints, field validation
- **Unique Date Constraint**: Prevents duplicate entries
- **get_or_create() Behavior**: Returns same entry on duplicate calls
- **AI Feedback Tests**: Pattern detection logic
- **View Tests**: GET/POST requests, field persistence
- **Integration Tests**: Full user workflow

---

## 💭 AI Feedback Logic

### How It Works

The `analyse_reflection()` function analyzes user input for keywords:

```python
def analyse_reflection(reflection: str, q1: str = "", q2: str = "", q3: str = "") -> str:
    # Combines all text
    # Detects patterns: stress, positivity, growth, learning
    # Returns personalized feedback
```

### Keyword Categories

| Category | Keywords | Feedback |
|----------|----------|----------|
| **Stress** | stressed, anxious, pressure, overwhelmed | Suggests self-care |
| **Positivity** | happy, grateful, proud, accomplished | Encourages continuation |
| **Growth** | learned, realized, improve, growth | Celebrates development |
| **Improvement** | improve, next time, better, work on | Recognizes progress mindset |

### Example Feedback Patterns

**Input**: "Faced difficult meetings but will improve by planning better"
**Output**: "You're actively thinking about growth and improvement. That's a growth mindset!"

**Input**: "Stressed and anxious about deadlines"
**Output**: "I noticed you faced some challenges today. Remember to prioritize rest and self-care."

---

## 📁 Project Structure

```
GRom/
├── GRom/                          # Django project config
│   ├── settings.py               # Project settings
│   ├── urls.py                   # Main URL routing
│   ├── asgi.py / wsgi.py        # Server config
│   └── __init__.py
│
├── main/                         # Core application
│   ├── models.py                # DailyEntry model
│   ├── views.py                 # View logic
│   ├── urls.py                  # App routing
│   ├── utils.py                 # AI feedback analysis
│   ├── tests.py                 # Unit tests (30+ tests)
│   ├── admin.py                 # Admin configuration
│   ├── apps.py
│   ├── migrations/              # Database migrations
│   └── __init__.py
│
├── templates/
│   ├── index.html               # Main form and display
│   └── base.html                # Base template (if used)
│
├── db.sqlite3                   # Local SQLite database
├── manage.py                    # Django CLI
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── PROJECT_OVERVIEW.md          # Architecture overview
└── env/                         # Virtual environment (venv)
```

---

## 🔐 Security Considerations

### Development Mode ⚠️
- DEBUG = True (change to False for production)
- SECRET_KEY exposed (regenerate for production)
- ALLOWED_HOSTS = [] (configure before deployment)

### Production Checklist
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')  # Use environment variable
DATABASES = {...}  # Use PostgreSQL or MySQL
```

### CSRF Protection
- ✅ Enabled on all forms
- ✅ Token validation on POST requests

---

## 📚 Usage Guide

### Daily Workflow

1. **Open the app** at `http://localhost:8000/`
2. **Set today's goals** (optional but recommended)
3. **List your tasks** in the Tasks field
4. **Answer three reflection questions**:
   - What went well?
   - What challenged you?
   - What would you improve?
5. **Add general reflection** (optional)
6. **Select your mood**
7. **Click "Save / Update Entry"**
8. **Review the AI feedback** generated from your answers

### Pattern Recognition Over Time

To see patterns emerge:
- Track mood consistently
- Answer all three questions
- Review feedback regularly
- Note recurring themes

---

## 🤝 Contributing & Extending

### Ideas for Enhancement

**Within Academic Scope:**
- Export entries as PDF using ReportLab
- Add weekly summary view
- Implement history/timeline view
- Add mood statistics dashboard
- Create habit tracking

**Advanced Features:**
- Multi-user support with authentication
- Cloud storage (with proper privacy measures)
- Export to CSV for analysis
- Dark mode UI
- Mobile-responsive improvements

---

## 📝 License & Academic Use

This project is provided as-is for educational purposes. 

**Attribution**: If you use this project:
- Include this README
- Maintain ethical disclaimers about AI feedback
- Document any modifications
- Ensure local data privacy

---

## ❓ FAQ

**Q: Is this a real AI system?**
A: No. It uses keyword matching and pattern detection. It's rule-based, not machine learning.

**Q: Will my data be shared?**
A: No. All data stays local in SQLite. Nothing is transmitted externally.

**Q: Can this replace therapy?**
A: No. It's a journaling tool, not professional mental health support.

**Q: Can I use this for production?**
A: It's an academic prototype. For production: add authentication, use PostgreSQL, implement proper security, configure environment variables.

**Q: How do I backup my entries?**
A: Backup the `db.sqlite3` file. For CSV export, extend the views to generate exports.

---

## 🐛 Troubleshooting

### Issue: "No such table: main_dailyentry"
**Solution**: Run migrations
```bash
python manage.py migrate
```

### Issue: Port 8000 already in use
**Solution**: Use different port
```bash
python manage.py runserver 8001
```

### Issue: Database locked
**Solution**: Delete `db.sqlite3` and re-migrate (loses data)
```bash
rm db.sqlite3
python manage.py migrate
```

---

## 📞 Support

- Check `main/tests.py` for usage examples
- Review `main/utils.py` for feedback logic
- See `templates/index.html` for form structure
- Review `GRom/settings.py` for configuration options

---

## 📌 Version Info

- **Django**: 5.2
- **Python**: 3.8+
- **Status**: Academic Prototype
- **Last Updated**: December 2025

---

**Remember**: This tool is for self-reflection and journaling. It's not professional advice. Always seek qualified professionals for serious concerns.
