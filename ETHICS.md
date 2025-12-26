# GRom – Ethics & Data Privacy Documentation

## Overview

This document outlines the ethical framework, data privacy practices, and limitations of the GRom project. GRom is an **academic prototype** for a daily self-development journal application.

---

## 🔒 Data Privacy & Security

### What Data is Collected?

GRom collects **only journal content** that users voluntarily enter:

| Data | Storage | Retention | Purpose |
|------|---------|-----------|---------|
| Daily tasks | SQLite (local) | Indefinite | User reference |
| Reflection text | SQLite (local) | Indefinite | Journaling |
| Mood selections | SQLite (local) | Indefinite | Pattern tracking |
| Goals | SQLite (local) | Indefinite | Goal tracking |
| Question answers | SQLite (local) | Indefinite | Structured reflection |

### What Data is NOT Collected?

❌ **No personal identification**
- No names, emails, phone numbers
- No user accounts or authentication
- No login/registration system

❌ **No behavioral metadata**
- No timestamps beyond date
- No IP addresses or device tracking
- No analytics or usage monitoring

❌ **No external transmission**
- All data stays on local machine
- No cloud synchronization
- No third-party service calls
- No data analytics backends

### Storage Method

- **Database**: SQLite3 (local file: `db.sqlite3`)
- **Location**: Project root directory on user's machine
- **Encryption**: None (suitable for local, single-user prototype)
- **Backup**: User responsible for backups of `db.sqlite3`

---

## 🏫 Academic Purpose

### Educational Goals

This project demonstrates:
- Django full-stack web framework fundamentals
- RESTful design principles (GET/POST)
- Relational database design and migrations
- UI/UX principles with Bootstrap
- Python best practices and code organization
- Test-driven development (30+ unit tests)
- Rule-based AI and pattern recognition
- Data validation and constraint enforcement

### Scope Limitations

This is **not intended for**:
- Production deployment
- Large-scale user bases
- Commercial applications
- Medical or psychological use
- Integration with external services

---

## ⚠️ AI Feedback Disclaimers

### What the AI Feedback IS

✅ **Pattern-based keyword analysis**
- Detects linguistic patterns (stress, positivity, growth)
- Provides encouraging, supportive suggestions
- Rule-based and fully transparent
- Designed to promote self-reflection

✅ **Designed for journaling purposes**
- Encourages deeper self-reflection
- Identifies personal patterns over time
- Supports goal-setting and improvement mindset
- Complements personal journaling practice

### What the AI Feedback is NOT

❌ **NOT a medical diagnosis**
- Does not diagnose mental health conditions
- Does not replace professional assessment
- Does not suggest treatment plans
- Not validated by medical professionals

❌ **NOT professional mental health advice**
- Not from licensed therapists or counselors
- Not personalized psychological assessment
- Does not track clinical symptoms
- Cannot substitute for professional care

❌ **NOT machine learning**
- No neural networks or deep learning
- No training on psychological data
- No probabilistic inference
- No adaptive intelligence

### How the AI Feedback Works

```
User Input
    ↓
Keywords matched against predefined lists:
  • Stress keywords: "stress", "anxious", "pressure"
  • Positive keywords: "happy", "grateful", "proud"
  • Growth keywords: "learned", "improve", "growth"
    ↓
Patterns detected and counted
    ↓
Rule-based feedback generated
    ↓
Response returned to user
```

**Complete code in**: [main/utils.py](main/utils.py)

---

## 🚫 Important Warnings

### For Users with Mental Health Concerns

If you experience:
- Persistent depression or sadness
- Suicidal thoughts
- Severe anxiety or panic attacks
- Substance abuse issues
- Relationship violence

**Please seek professional help:**
- Contact a licensed mental health professional
- Call a crisis helpline in your country
- Visit your doctor or local hospital
- Reach out to trusted family or friends

**GRom cannot and should not replace professional care.**

### For Developers Extending This Project

❌ **Do NOT**:
- Add machine learning models trained on journal data
- Implement psychological scoring algorithms
- Claim the tool provides mental health assessment
- Store personally identifiable information
- Transmit data to external services without explicit consent and encryption

✅ **DO**:
- Maintain all privacy disclaimers
- Add user consent for any data usage changes
- Document code thoroughly
- Implement proper encryption if storing sensitive data
- Implement proper authentication if adding multi-user support
- Add security headers and HTTPS for any production deployment

---

## 🔐 Security Considerations

### Current State (Development)

**⚠️ NOT suitable for production:**
```python
DEBUG = True                    # Shows detailed error pages
SECRET_KEY = 'hardcoded'       # Exposed in code
ALLOWED_HOSTS = []             # Not configured
No HTTPS/SSL                   # Unencrypted transmission
No authentication              # Single user only
SQLite database                # Not suitable for concurrent users
```

### For Production Deployment

**Must implement:**

1. **Environment Security**
   ```python
   DEBUG = False
   SECRET_KEY = os.environ.get('SECRET_KEY')
   ALLOWED_HOSTS = ['yourdomain.com']
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```

2. **Database**
   - Use PostgreSQL or MySQL (not SQLite)
   - Implement proper connection pooling
   - Use encrypted credentials

3. **Authentication**
   - Implement user authentication (Django-allauth, djoser)
   - Add password requirements and hashing
   - Implement session management

4. **Data Protection**
   - Implement field-level encryption for journal content
   - Add data export/deletion for compliance
   - Implement proper backup and recovery procedures

5. **Deployment**
   - Use HTTPS/TLS for all connections
   - Implement rate limiting
   - Add security headers (CSP, HSTS, etc.)
   - Use reverse proxy (nginx)
   - Implement logging and monitoring

6. **Compliance**
   - Review GDPR, HIPAA, or relevant regulations
   - Implement privacy policy
   - Add terms of service
   - Ensure consent for data collection

---

## 📋 Code Ethics Guidelines

### Comments & Documentation

All code includes ethics notes:

**In models.py:**
```python
"""
ETHICS NOTICE:
- No personal identification data collected
- Single-user, local prototype for academic purposes
- AI feedback is rule-based, not a medical/psychological diagnosis
"""
```

**In utils.py:**
```python
"""
ETHICS NOTICE:
- Rule-based analysis only (no machine learning)
- Designed for self-reflection, not diagnosis
- No data is transmitted externally
"""
```

**In admin.py and views.py:**
- Clear documentation of purpose
- Data handling explanations
- Security considerations

### Best Practices Applied

✅ **Code transparency**
- All logic is rule-based and auditable
- No hidden algorithms
- Clear variable and function names

✅ **Data minimization**
- Collects only necessary information
- No tracking or metadata
- Users control all data

✅ **User agency**
- Users can edit/delete entries anytime
- No forced data collection
- Optional feedback feature

---

## 📊 Testing & Validation

### Test Coverage

30+ unit tests covering:
- Model constraints (unique date per day)
- Field validation (blank fields, choices)
- AI feedback patterns (stress, positivity, growth)
- View logic (form submission, data persistence)
- Redirect behavior and template usage

**Run tests:**
```bash
python manage.py test main.tests --verbosity=2
```

### Bias Considerations

**Potential biases in keyword detection:**

| Issue | Consideration |
|-------|---|
| Language bias | English-only keywords; some languages may not match |
| Cultural bias | Positive/stress words may differ by culture |
| Mental health bias | Cannot diagnose; patterns are superficial |
| Socioeconomic bias | No accommodation for different life circumstances |

**Mitigated by:**
- Keeping feedback encouraging but neutral
- Never making definitive claims
- Always recommending professional help for concerns
- User retains full control of interpretation

---

## 🔄 Transparency & Auditability

### How Users Can Verify

1. **Inspect the code**
   - All source code is readable Python/Django
   - No compiled or obfuscated components
   - Full access to logic in `main/utils.py`

2. **Check the database**
   - SQLite database is standard SQL format
   - Users can inspect with any SQLite viewer
   - Data format is transparent

3. **Monitor network traffic**
   - Can use browser dev tools (Network tab)
   - Can use packet sniffer (Wireshark)
   - Will show no external API calls

4. **Review logs**
   - Django logs all requests
   - Can enable debug logging
   - See exactly what's happening

---

## 👥 User Rights & Responsibilities

### User Rights

✅ Users have the right to:
- Access all their data at any time
- Edit or delete any entry
- Understand how feedback is generated
- Know no data is shared externally
- Use the tool offline indefinitely

### User Responsibilities

📋 Users should:
- Use the tool for personal journaling only
- Understand it's not professional advice
- Seek professional help for serious concerns
- Maintain their own database backups
- Read and understand these ethical guidelines

---

## 📞 Questions & Concerns

### For Academic Use

- Review the code in `main/utils.py`
- Check the test suite in `main/tests.py`
- Read inline comments in all Python files
- See detailed README.md for usage

### For Extended Development

When modifying this project:
1. Maintain all ethics documentation
2. Update disclaimers if adding features
3. Add security measures if deploying
4. Consider user privacy in all changes
5. Document your modifications

### For Reporting Issues

If you find:
- Privacy concerns
- Security vulnerabilities
- Misleading claims
- Code that violates these guidelines

Please review the issue, document it clearly, and plan remediation.

---

## 📄 License & Attribution

**GRom** is provided as an academic prototype under the understanding that:

1. This documentation is maintained with the code
2. Ethical disclaimers are preserved
3. The rule-based nature of AI feedback is not misrepresented
4. Local data privacy is maintained
5. Users are informed of all limitations

---

## ✅ Ethical Checklist

Before deploying or distributing this project:

- [ ] All privacy disclaimers are visible
- [ ] AI limitations are clearly stated
- [ ] No claims about medical/psychological assessment
- [ ] Data storage method is explained
- [ ] Code is transparent and auditable
- [ ] Tests cover key functionality
- [ ] No external data transmission
- [ ] User consent is obtained (if modified)
- [ ] Security considerations are documented
- [ ] Professional help resources are provided

---

**Last Updated**: December 2025
**Status**: Academic Prototype
**Version**: 1.0

For questions about ethics, data privacy, or AI feedback limitations, review this document and the README.md file.
