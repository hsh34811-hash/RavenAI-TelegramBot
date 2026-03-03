# 🤝 Contributing to 24xRaven Bot | المساهمة في بوت 24xRaven

Thank you for considering contributing to 24xRaven Bot! | شكراً لاهتمامك بالمساهمة في بوت 24xRaven!

---

## 📋 Table of Contents | المحتويات

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct | قواعد السلوك

This project adheres to a code of conduct. By participating, you are expected to uphold this code.

### Our Standards | معاييرنا

- Be respectful and inclusive
- Accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

---

## 🎯 How Can I Contribute? | كيف يمكنك المساهمة؟

### Reporting Bugs | الإبلاغ عن الأخطاء

Before creating bug reports, please check existing issues. When creating a bug report, include:

- Clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Screenshots (if applicable)
- Environment details (OS, Python version, etc.)

### Suggesting Features | اقتراح ميزات جديدة

Feature suggestions are welcome! Please provide:

- Clear description of the feature
- Why this feature would be useful
- Possible implementation approach
- Examples or mockups (if applicable)

### Code Contributions | المساهمات البرمجية

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Test thoroughly
5. Commit your changes
6. Push to your fork
7. Open a Pull Request

---

## 🛠️ Development Setup | إعداد بيئة التطوير

### Prerequisites | المتطلبات

```bash
Python 3.8+
pip
git
```

### Setup Steps | خطوات الإعداد

1. **Clone your fork**
```bash
git clone https://github.com/YOUR_USERNAME/24xRaven-Bot.git
cd 24xRaven-Bot
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure the bot**
- Copy `bot.py` and add your tokens
- Test locally before submitting

---

## 📝 Coding Standards | معايير البرمجة

### Python Style Guide

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions small and focused
- Comment complex logic

### Example | مثال

```python
def calculate_user_stats(user_id):
    """
    Calculate statistics for a specific user.
    
    Args:
        user_id (int): The Telegram user ID
        
    Returns:
        dict: User statistics including message count and join date
    """
    # Implementation here
    pass
```

### Documentation | التوثيق

- Update README.md if adding features
- Add comments in Arabic and English where helpful
- Update CHANGELOG.md

---

## 💬 Commit Guidelines | إرشادات الـ Commit

### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

### Types | الأنواع

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples | أمثلة

```bash
feat: Add voice message support

Added functionality to process and respond to voice messages
using speech-to-text API.

Closes #123
```

```bash
fix: Resolve image generation timeout issue

Increased timeout duration and added retry logic for
image generation requests.
```

---

## 🔄 Pull Request Process | عملية الـ Pull Request

### Before Submitting | قبل الإرسال

- [ ] Code follows project style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings or errors
- [ ] Tested on multiple scenarios

### PR Description Template | قالب وصف الـ PR

```markdown
## Description | الوصف
Brief description of changes

## Type of Change | نوع التغيير
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring

## Testing | الاختبار
Describe testing performed

## Screenshots | لقطات الشاشة
If applicable

## Checklist | قائمة التحقق
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] No breaking changes
```

### Review Process | عملية المراجعة

1. Maintainer will review your PR
2. Address any requested changes
3. Once approved, PR will be merged
4. Your contribution will be credited

---

## 🏆 Recognition | التقدير

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in project documentation

---

## 📞 Questions? | أسئلة؟

Feel free to reach out:

- **Telegram**: [@P_X_24](https://t.me/P_X_24)
- **Channel**: [Raven_xx24](https://t.me/Raven_xx24)
- **Email**: hsh34811@gmail.com

---

<div align="center">

**Thank you for contributing! | شكراً لمساهمتك!**

Made with ❤️ by ✘ 𝙍𝘼𝙑𝙀𝙉

Copyright © 2026 - All Rights Reserved

</div>
