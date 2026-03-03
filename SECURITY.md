# 🔒 Security Policy | سياسة الأمان

## 24xRaven Bot - Security Guidelines

**Developed by ✘ 𝙍𝘼𝙑𝙀𝙉**

---

## 🛡️ Supported Versions | الإصدارات المدعومة

Currently supported versions with security updates:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | ✅ Yes             |
| < 1.0   | ❌ No              |

---

## 🚨 Reporting a Vulnerability | الإبلاغ عن ثغرة أمنية

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 1. **DO NOT** Create a Public Issue | **لا تقم** بإنشاء مشكلة عامة

Please do not disclose security vulnerabilities publicly until they have been addressed.

### 2. Contact Us Privately | تواصل معنا بشكل خاص

Send details to:
- **Email**: hsh34811@gmail.com
- **Telegram**: [@P_X_24](https://t.me/P_X_24)

### 3. Include These Details | قم بتضمين هذه التفاصيل

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)
- Your contact information

### 4. Response Timeline | الجدول الزمني للرد

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: 1-3 days
  - High: 1-2 weeks
  - Medium: 2-4 weeks
  - Low: Next release

---

## 🔐 Security Best Practices | أفضل ممارسات الأمان

### For Users | للمستخدمين

#### 1. Protect Your Tokens | احمِ التوكنات الخاصة بك

```python
# ❌ NEVER commit tokens to version control
TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"

# ✅ Use environment variables
import os
TOKEN = os.getenv('BOT_TOKEN')
```

#### 2. Keep Dependencies Updated | حافظ على تحديث المكتبات

```bash
# Check for updates
pip list --outdated

# Update packages
pip install --upgrade package_name
```

#### 3. Use Strong Passwords | استخدم كلمات مرور قوية

- Never share your bot token
- Use unique tokens for each bot
- Regenerate tokens if compromised

#### 4. Limit Bot Permissions | قلل صلاحيات البوت

Only grant necessary permissions to your bot on Telegram.

### For Developers | للمطورين

#### 1. Input Validation | التحقق من المدخلات

```python
# Always validate user input
def validate_phone(number):
    if not number.startswith('+'):
        return False
    if len(number) < 10:
        return False
    return True
```

#### 2. Error Handling | معالجة الأخطاء

```python
# Never expose sensitive information in errors
try:
    # risky operation
    pass
except Exception as e:
    # ❌ Don't do this
    bot.send_message(chat_id, f"Error: {str(e)}")
    
    # ✅ Do this instead
    bot.send_message(chat_id, "An error occurred. Please try again.")
    logger.error(f"Error details: {str(e)}")
```

#### 3. Rate Limiting | تحديد المعدل

```python
# Implement rate limiting to prevent abuse
from functools import wraps
import time

def rate_limit(max_calls, time_frame):
    calls = {}
    def decorator(func):
        @wraps(func)
        def wrapper(user_id, *args, **kwargs):
            now = time.time()
            if user_id not in calls:
                calls[user_id] = []
            calls[user_id] = [t for t in calls[user_id] if now - t < time_frame]
            if len(calls[user_id]) >= max_calls:
                return "Rate limit exceeded"
            calls[user_id].append(now)
            return func(user_id, *args, **kwargs)
        return wrapper
    return decorator
```

#### 4. Secure API Calls | استدعاءات API آمنة

```python
# Always use HTTPS
# ❌ Don't do this
url = "http://api.example.com/data"

# ✅ Do this
url = "https://api.example.com/data"

# Set timeouts
response = requests.get(url, timeout=10)
```

---

## 🔍 Known Security Considerations | اعتبارات أمنية معروفة

### 1. Token Storage | تخزين التوكنات

**Current**: Tokens stored in code
**Risk**: Medium
**Mitigation**: Use environment variables or config files (not committed)

**Recommended**:
```bash
# Create .env file
echo "BOT_TOKEN=your_token_here" > .env
echo "HF_TOKEN=your_hf_token" >> .env

# Add to .gitignore
echo ".env" >> .gitignore
```

```python
# Load from .env
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
```

### 2. User Data | بيانات المستخدم

**Current**: User IDs stored in JSON
**Risk**: Low
**Mitigation**: File permissions, no sensitive data stored

**Recommended**:
```bash
# Set proper file permissions
chmod 600 users.json
```

### 3. API Keys | مفاتيح API

**Current**: Hugging Face token in code
**Risk**: High if exposed
**Mitigation**: Never commit to public repositories

**Recommended**:
- Use environment variables
- Rotate keys regularly
- Use key management services (AWS KMS, HashiCorp Vault)

### 4. Input Validation | التحقق من المدخلات

**Current**: Basic validation
**Risk**: Low
**Mitigation**: Validate all user inputs

**Recommended**:
```python
import re

def sanitize_input(text):
    # Remove potentially dangerous characters
    return re.sub(r'[^\w\s\-\+\.]', '', text)
```

---

## 🛠️ Security Checklist | قائمة التحقق الأمنية

### Before Deployment | قبل النشر

- [ ] All tokens moved to environment variables
- [ ] `.env` file added to `.gitignore`
- [ ] Dependencies updated to latest versions
- [ ] Input validation implemented
- [ ] Error messages don't expose sensitive info
- [ ] Rate limiting configured
- [ ] HTTPS used for all external calls
- [ ] File permissions set correctly
- [ ] Logging configured (without sensitive data)
- [ ] Security headers added (if using web interface)

### Regular Maintenance | الصيانة الدورية

- [ ] Review access logs weekly
- [ ] Update dependencies monthly
- [ ] Rotate API keys quarterly
- [ ] Security audit annually
- [ ] Backup data regularly
- [ ] Monitor for unusual activity
- [ ] Review and update security policies

---

## 🚫 Common Vulnerabilities to Avoid | الثغرات الشائعة التي يجب تجنبها

### 1. Command Injection | حقن الأوامر

```python
# ❌ NEVER do this
import os
user_input = message.text
os.system(f"echo {user_input}")

# ✅ Use safe alternatives
import subprocess
subprocess.run(["echo", user_input], check=True)
```

### 2. SQL Injection | حقن SQL

```python
# ❌ NEVER do this
query = f"SELECT * FROM users WHERE id = {user_id}"

# ✅ Use parameterized queries
query = "SELECT * FROM users WHERE id = ?"
cursor.execute(query, (user_id,))
```

### 3. Path Traversal | اجتياز المسار

```python
# ❌ NEVER do this
filename = message.text
with open(f"files/{filename}", 'r') as f:
    content = f.read()

# ✅ Validate and sanitize
import os
filename = os.path.basename(message.text)
safe_path = os.path.join("files", filename)
if os.path.commonprefix([safe_path, "files"]) == "files":
    with open(safe_path, 'r') as f:
        content = f.read()
```

### 4. Information Disclosure | الكشف عن المعلومات

```python
# ❌ Don't expose internal details
except Exception as e:
    bot.send_message(chat_id, f"Database error: {str(e)}")

# ✅ Use generic messages
except Exception as e:
    logger.error(f"Database error: {str(e)}")
    bot.send_message(chat_id, "An error occurred. Please try again later.")
```

---

## 📋 Security Audit Log | سجل التدقيق الأمني

### Version 1.0.0 - 2026-03-03

**Audit Date**: 2026-03-03
**Auditor**: ✘ 𝙍𝘼𝙑𝙀𝙉
**Status**: ✅ Passed

**Findings**:
- ✅ No critical vulnerabilities
- ⚠️ Tokens in code (Medium) - Documented
- ✅ Input validation present
- ✅ Error handling implemented
- ⚠️ Rate limiting not implemented - Planned

**Actions Taken**:
- Added security documentation
- Created `.gitignore` for sensitive files
- Implemented input validation
- Added error handling

**Recommendations**:
- Implement rate limiting
- Move tokens to environment variables
- Add logging system
- Implement user authentication levels

---

## 🔗 Security Resources | موارد الأمان

### Python Security

- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [OWASP Python Security](https://owasp.org/www-project-python-security/)

### Telegram Bot Security

- [Telegram Bot API Security](https://core.telegram.org/bots/api#authorizing-your-bot)
- [Bot Security Best Practices](https://core.telegram.org/bots/faq#security)

### General Security

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [CWE Top 25](https://cwe.mitre.org/top25/)

---

## 📞 Security Contact | التواصل الأمني

For security-related inquiries:

- **Email**: hsh34811@gmail.com (PGP key available on request)
- **Telegram**: [@P_X_24](https://t.me/P_X_24)
- **Response Time**: Within 48 hours

---

## 🏆 Security Hall of Fame | قاعة مشاهير الأمان

We appreciate security researchers who responsibly disclose vulnerabilities:

*No vulnerabilities reported yet*

---

## 📜 Disclosure Policy | سياسة الإفصاح

We follow responsible disclosure:

1. **Report**: Security researcher reports vulnerability privately
2. **Acknowledge**: We acknowledge receipt within 48 hours
3. **Fix**: We develop and test a fix
4. **Release**: We release the fix
5. **Disclose**: We publicly disclose the vulnerability (with credit)
6. **Reward**: We recognize the researcher in our Hall of Fame

---

<div align="center">

**Security is a shared responsibility**

**الأمان مسؤولية مشتركة**

Made with ❤️ by ✘ 𝙍𝘼𝙑𝙀𝙉

Copyright © 2026 - All Rights Reserved

</div>
