<div align="center">

# 24xRaven Telegram Bot

<p align="center">
  <img src="https://cdn.simpleicons.org/python/3776AB" alt="Python" width="60" height="60"/>
  <img src="https://cdn.simpleicons.org/telegram/26A5E4" alt="Telegram" width="60" height="60"/>
  <img src="https://cdn.simpleicons.org/openai/412991" alt="AI" width="60" height="60"/>
</p>

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Raven_xx24)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

**بوت تليجرام احترافي متعدد الوظائف مع ذكاء اصطناعي متقدم**

[العربية](#arabic) • [English](#english)

</div>

---

<div id="arabic">

## المحتويات

- [نظرة عامة](#نظرة-عامة)
- [المميزات](#المميزات)
- [التثبيت](#التثبيت)
- [الاستخدام](#الاستخدام)
- [الأوامر](#الأوامر)
- [المتطلبات](#المتطلبات)
- [الإعدادات](#الإعدادات)
- [المساهمة](#المساهمة)
- [الترخيص](#الترخيص)
- [التواصل](#التواصل)

## نظرة عامة

24xRaven Bot هو بوت تليجرام احترافي مطور بلغة Python يوفر مجموعة متنوعة من الخدمات المتقدمة:

<div align="center">

| الميزة | الوصف |
|--------|-------|
| توليد الصور بالذكاء الاصطناعي | استخدام نموذج FLUX.1-schnell من Hugging Face |
| البحث المتقدم عن الأرقام | معلومات تفصيلية عن أي رقم هاتف |
| تحليل IP والدومينات | معلومات جغرافية وتقنية شاملة |
| نظام إحصائيات متقدم | تتبع المستخدمين والنشاط |

</div>

## المميزات

### توليد الصور بالذكاء الاصطناعي
- استخدام نموذج FLUX.1-schnell المتقدم
- جودة عالية (1024x1024)
- سرعة توليد فائقة
- دعم الأوصاف بالعربية والإنجليزية

### البحث عن الأرقام
- معلومات الموقع الجغرافي
- اسم المشغل
- نوع الخط (موبايل/أرضي)
- روابط مباشرة لـ WhatsApp و Telegram

### تحليل IP/Domain
- الموقع الجغرافي الدقيق
- معلومات الشبكة (ISP, AS)
- إرسال الموقع على الخريطة
- رابط Google Maps مباشر

### مميزات تقنية
- تثبيت تلقائي للمكتبات
- معالجة متعددة الخيوط (Threading)
- رسائل انتظار تفاعلية
- نظام تتبع المستخدمين
- إشعارات فورية للمطور

## التثبيت

### المتطلبات الأساسية
- Python 3.8 أو أحدث
- حساب Telegram Bot (من [@BotFather](https://t.me/BotFather))
- Hugging Face API Token

### خطوات التثبيت

1. **استنساخ المشروع**
```bash
git clone https://github.com/hsh34811-hash/24xRaven-Bot.git
cd 24xRaven-Bot
```

2. **تثبيت المكتبات**
```bash
pip install -r requirements.txt
```

3. **إعداد البوت**
- افتح ملف `bot.py`
- غير `TOKEN` بتوكن البوت الخاص بك
- غير `OWNER_ID` برقم ID الخاص بك
- غير `HF_TOKEN` بتوكن Hugging Face

4. **تشغيل البوت**
```bash
python raven_bot.py
```

## الاستخدام

### البدء
1. ابحث عن البوت على Telegram
2. اضغط `/start`
3. اختر الخدمة المطلوبة من القائمة

### الأوامر المتاحة

| الأمر | الوصف | الصلاحية |
|------|------|---------|
| `/start` | بدء البوت وعرض القائمة الرئيسية | الجميع |
| `/stats` | عرض إحصائيات البوت | المطور فقط |

## الأوامر

### توليد الصور
1. اختر "🎨 توليد صور AI"
2. اكتب وصف الصورة
3. انتظر التوليد (5-10 ثواني)

### البحث عن رقم
1. اختر "📱 البحث بالرقم"
2. أدخل الرقم بالصيغة الدولية (+201234567890)
3. احصل على المعلومات الكاملة

### تحليل IP
1. اختر "🌐 معلومات IP/Domain"
2. أدخل IP أو Domain
3. احصل على الموقع والمعلومات

## المتطلبات

```txt
pyTelegramBotAPI>=4.14.0
requests>=2.31.0
phonenumbers>=8.13.0
huggingface-hub>=0.20.0
Pillow>=10.0.0
```

## الإعدادات

### إعدادات البوت الأساسية
```python
TOKEN = "YOUR_BOT_TOKEN"          # توكن البوت من BotFather
OWNER_ID = YOUR_TELEGRAM_ID       # رقم ID الخاص بك
HF_TOKEN = "YOUR_HF_TOKEN"        # توكن Hugging Face
MODEL_ID = "black-forest-labs/FLUX.1-schnell"  # نموذج الصور
```

### الحصول على Hugging Face Token
1. سجل في [Hugging Face](https://huggingface.co/)
2. اذهب إلى Settings → Access Tokens
3. أنشئ توكن جديد
4. انسخه في `HF_TOKEN`

## لقطات الشاشة

<div align="center">

> لقطات الشاشة ستضاف قريباً

</div>

## المساهمة

المساهمات مرحب بها! إذا كنت تريد المساهمة:

1. Fork المشروع
2. أنشئ فرع جديد (`git checkout -b feature/AmazingFeature`)
3. Commit التغييرات (`git commit -m 'Add some AmazingFeature'`)
4. Push للفرع (`git push origin feature/AmazingFeature`)
5. افتح Pull Request

## الترخيص

هذا المشروع مرخص تحت رخصة MIT - انظر ملف [LICENSE](LICENSE) للتفاصيل.

```
Copyright © 2026 ✘ 𝙍𝘼𝙑𝙀𝙉 - All Rights Reserved
```

## التواصل

<div align="center">

<p align="center">
  <a href="https://github.com/hsh34811-hash">
    <img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="50" height="50"/>
  </a>
  <a href="https://t.me/P_X_24">
    <img src="https://cdn.simpleicons.org/telegram/26A5E4" alt="Telegram" width="50" height="50"/>
  </a>
  <a href="https://t.me/Raven_xx24">
    <img src="https://cdn.simpleicons.org/telegram/26A5E4" alt="Channel" width="50" height="50"/>
  </a>
  <a href="mailto:hsh34811@gmail.com">
    <img src="https://cdn.simpleicons.org/gmail/EA4335" alt="Email" width="50" height="50"/>
  </a>
</p>

[![GitHub](https://img.shields.io/badge/GitHub-hsh34811--hash-181717?style=for-the-badge&logo=github)](https://github.com/hsh34811-hash)
[![Telegram](https://img.shields.io/badge/Telegram-@P__X__24-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/P_X_24)
[![Channel](https://img.shields.io/badge/Channel-Raven__xx24-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/Raven_xx24)
[![Email](https://img.shields.io/badge/Email-hsh34811@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hsh34811@gmail.com)

</div>

---

</div>

<div id="english">

## Contents

- [Overview](#overview-en)
- [Features](#features-en)
- [Installation](#installation-en)
- [Usage](#usage-en)
- [Commands](#commands-en)
- [Requirements](#requirements-en)
- [Configuration](#configuration-en)
- [Contributing](#contributing-en)
- [License](#license-en)
- [Contact](#contact-en)

## Overview {#overview-en}

24xRaven Bot is a professional Telegram bot developed in Python that provides a variety of advanced services:

<div align="center">

| Feature | Description |
|---------|-------------|
| AI Image Generation | Using FLUX.1-schnell model from Hugging Face |
| Advanced Phone Number Search | Detailed information about any phone number |
| IP/Domain Analysis | Comprehensive geographic and technical information |
| Advanced Statistics System | User and activity tracking |

</div>

## Features {#features-en}

### AI Image Generation
- Using advanced FLUX.1-schnell model
- High quality (1024x1024)
- Ultra-fast generation
- Support for Arabic and English descriptions

### Phone Number Search
- Geographic location information
- Carrier name
- Line type (mobile/landline)
- Direct links to WhatsApp and Telegram

### IP/Domain Analysis
- Precise geographic location
- Network information (ISP, AS)
- Send location on map
- Direct Google Maps link

### Technical Features
- Automatic library installation
- Multi-threading processing
- Interactive waiting messages
- User tracking system
- Instant developer notifications

## Installation {#installation-en}

### Prerequisites
- Python 3.8 or newer
- Telegram Bot account (from [@BotFather](https://t.me/BotFather))
- Hugging Face API Token

### Installation Steps

1. **Clone the project**
```bash
git clone https://github.com/hsh34811-hash/24xRaven-Bot.git
cd 24xRaven-Bot
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure the bot**
- Open `raven_bot.py` file
- Change `TOKEN` to your bot token
- Change `OWNER_ID` to your ID number
- Change `HF_TOKEN` to your Hugging Face token

4. **Run the bot**
```bash
python raven_bot.py
```

## Usage {#usage-en}

### Getting Started
1. Search for the bot on Telegram
2. Press `/start`
3. Choose the desired service from the menu

### Available Commands

| Command | Description | Permission |
|---------|-------------|------------|
| `/start` | Start the bot and display main menu | Everyone |
| `/stats` | Display bot statistics | Developer only |

## Requirements {#requirements-en}

```txt
pyTelegramBotAPI>=4.14.0
requests>=2.31.0
phonenumbers>=8.13.0
huggingface-hub>=0.20.0
Pillow>=10.0.0
```

## Configuration {#configuration-en}

### Basic Bot Settings
```python
TOKEN = "YOUR_BOT_TOKEN"          # Bot token from BotFather
OWNER_ID = YOUR_TELEGRAM_ID       # Your ID number
HF_TOKEN = "YOUR_HF_TOKEN"        # Hugging Face token
MODEL_ID = "black-forest-labs/FLUX.1-schnell"  # Image model
```

## Contributing {#contributing-en}

Contributions are welcome! If you want to contribute:

1. Fork the project
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License {#license-en}

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
Copyright © 2026 ✘ 𝙍𝘼𝙑𝙀𝙉 - All Rights Reserved
```

## Contact {#contact-en}

<div align="center">

<p align="center">
  <a href="https://github.com/hsh34811-hash">
    <img src="https://cdn.simpleicons.org/github/181717" alt="GitHub" width="50" height="50"/>
  </a>
  <a href="https://t.me/P_X_24">
    <img src="https://cdn.simpleicons.org/telegram/26A5E4" alt="Telegram" width="50" height="50"/>
  </a>
  <a href="https://t.me/Raven_xx24">
    <img src="https://cdn.simpleicons.org/telegram/26A5E4" alt="Channel" width="50" height="50"/>
  </a>
  <a href="mailto:hsh34811@gmail.com">
    <img src="https://cdn.simpleicons.org/gmail/EA4335" alt="Email" width="50" height="50"/>
  </a>
</p>

[![GitHub](https://img.shields.io/badge/GitHub-hsh34811--hash-181717?style=for-the-badge&logo=github)](https://github.com/hsh34811-hash)
[![Telegram](https://img.shields.io/badge/Telegram-@P__X__24-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/P_X_24)
[![Channel](https://img.shields.io/badge/Channel-Raven__xx24-2CA5E0?style=for-the-badge&logo=telegram)](https://t.me/Raven_xx24)
[![Email](https://img.shields.io/badge/Email-hsh34811@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:hsh34811@gmail.com)

</div>

---

<div align="center">

### إذا أعجبك المشروع، لا تنسى إضافة نجمة | If you like the project, don't forget to star it

**Made with ❤️ by ✘ 𝙍𝘼𝙑𝙀𝙉**

</div>

</div>
