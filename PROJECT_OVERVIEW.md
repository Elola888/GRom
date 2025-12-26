# GRom – Project Overview

## About the Project

**GRom** is a Django-based daily journaling and self-development application. It helps users track their daily tasks, reflect on their day, record their mood, and receive AI-powered feedback on their reflections.

### Key Features
- **Daily Entry Management**: Create or update one entry per day
- **Task Tracking**: Record daily tasks in a structured format
- **Reflection Journal**: Write reflections on how your day felt
- **Mood Tracking**: Track your emotional state with mood choices (Happy, OK, Sad, Stressed)
- **AI Feedback**: Automated feedback on reflections based on keyword analysis

---

## Project Structure

```
GRom/
├── GRom/                    # Django project configuration
│   ├── settings.py          # Project settings & configurations
│   ├── urls.py              # Main URL routing
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
│
├── main/                    # Django application (core functionality)
│   ├── models.py            # Data models (DailyEntry)
│   ├── views.py             # View logic (index view)
│   ├── urls.py              # App URL routing
│   ├── utils.py             # Utility functions (analyse_reflection)
│   ├── admin.py             # Django admin configuration
│   ├── migrations/          # Database migrations
│   └── tests.py             # Test files
│
├── templates/               # HTML templates
│   ├── base.html            # Base template (if used)
│   └── index.html           # Main daily entry interface
│
├── env/                     # Python virtual environment
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
└── requirements.txt         # Python dependencies
```

---

## Data Model

### DailyEntry
The main model storing user data:

| Field | Type | Description |
|-------|------|-------------|
| `date` | DateField | Entry date (auto-added, unique per day) |
| `tasks` | TextField | List of tasks for the day |
| `reflection` | TextField | User's reflection on the day |
| `mood` | CharField | Mood choice (happy, ok, sad, stressed) |
| `ai_feedback` | TextField | AI-generated feedback |

---

## Technology Stack

- **Framework**: Django 5.2
- **Database**: SQLite3
- **Frontend**: Bootstrap 5 + HTML
- **Python Version**: 3.x (with virtual environment)
- **Additional Libraries**:
  - Pillow (image processing)
  - Stripe (payment processing)
  - ReportLab (PDF generation)
  - Requests (HTTP library)
  - python-decouple, python-dotenv (environment variables)

---

## How It Works

### Flow
1. User visits the main page (`/`)
2. System retrieves or creates today's DailyEntry
3. User fills in:
   - Daily tasks
   - Reflection about their day
   - Mood selection
4. On form submission:
   - Data is saved to the database
   - `analyse_reflection()` function analyzes the reflection text
   - AI feedback is generated and stored
   - Page redirects back to show the updated entry

### AI Feedback Logic
The `analyse_reflection()` function:
- Checks for stress-related keywords → suggests self-care
- Checks for positive keywords → encourages continued tracking
- Checks reflection length → suggests more detailed writing
- Returns generic feedback for balanced days

---

## Installation & Setup

1. Activate the virtual environment:
   ```powershell
   .\env\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Access at `http://localhost:8000/`

---

## Development Notes

- The app currently uses a single daily entry per user (no multi-user support yet)
- Database is SQLite3 (suitable for development; consider PostgreSQL for production)
- DEBUG mode is enabled (remember to disable in production)
- CSRF protection is enabled for form submissions
