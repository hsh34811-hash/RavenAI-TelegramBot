# ⚙️ Setup Guide | دليل الإعداد

## 24xRaven Bot - Complete Setup Instructions

**Developed by ✘ 𝙍𝘼𝙑𝙀𝙉**

---

## 🔐 Important Security Notice | تنبيه أمني مهم

⚠️ **NEVER commit sensitive information to Git!**

⚠️ **لا تقم أبداً برفع المعلومات الحساسة على Git!**

This includes:
- Bot tokens
- API keys
- User IDs
- Database files
- Configuration files with secrets

---

## 📋 Step-by-Step Setup | الإعداد خطوة بخطوة

### Step 1: Get Your Bot Token | الخطوة 1: احصل على توكن البوت

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Choose a name for your bot (e.g., "My Awesome Bot")
4. Choose a username (must end with 'bot', e.g., "myawesome_bot")
5. Copy the token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

**Example:**
```
Token: 1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-EXAMPLE
```

---

### Step 2: Get Your User ID | الخطوة 2: احصل على ID الخاص بك

1. Open Telegram and search for **@userinfobot**
2. Start the bot
3. Copy your user ID (a number like: `123456789`)

**Example:**
```
User ID: 1234567890
```

---

### Step 3: Get Hugging Face Token | الخطوة 3: احصل على توكن Hugging Face

1. Go to [https://huggingface.co/](https://huggingface.co/)
2. Sign up or log in
3. Go to **Settings** → **Access Tokens**
4. Click **New token**
5. Give it a name (e.g., "24xRaven Bot")
6. Select **Read** permission
7. Copy the token (looks like: `hf_xxxxxxxxxxxxxxxxxxxxx`)

**Example:**
```
Token: hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

### Step 4: Configure the Bot | الخطوة 4: إعداد البوت

#### Option A: Direct Configuration (Quick) | الخيار أ: الإعداد المباشر (سريع)

Open `raven_bot.py` and find these lines:

```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
OWNER_ID = 0
HF_TOKEN = "YOUR_HUGGING_FACE_TOKEN_HERE"
```

Replace with your actual values:

```python
TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-EXAMPLE"
OWNER_ID = 1234567890
HF_TOKEN = "hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

⚠️ **Warning**: Don't commit this file to Git!

---

#### Option B: Environment Variables (Recommended) | الخيار ب: متغيرات البيئة (موصى به)

1. **Copy the example file:**
```bash
cp .env.example .env
```

2. **Edit `.env` file:**
```bash
nano .env  # or use any text editor
```

3. **Fill in your values:**
```env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-EXAMPLE
OWNER_ID=1234567890
HF_TOKEN=hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

4. **Update `raven_bot.py` to use environment variables:**

Add at the top of `raven_bot.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))
HF_TOKEN = os.getenv('HF_TOKEN')
```

5. **Install python-dotenv:**
```bash
pip install python-dotenv
```

---

### Step 5: Verify Configuration | الخطوة 5: التحقق من الإعداد

Run this command to check if everything is set up correctly:

```bash
python -c "from raven_bot import TOKEN, OWNER_ID, HF_TOKEN; print('✅ Configuration OK' if all([TOKEN, OWNER_ID, HF_TOKEN]) else '❌ Missing values')"
```

---

## 🔒 Security Checklist | قائمة التحقق الأمنية

Before running your bot, make sure:

- [ ] `.env` file is in `.gitignore`
- [ ] `users.json` is in `.gitignore`
- [ ] No tokens in `bot.py` (if using .env)
- [ ] File permissions are correct (`chmod 600 .env`)
- [ ] You're not sharing your tokens with anyone

---

## 🚀 Running the Bot | تشغيل البوت

### First Run | التشغيل الأول

```bash
python raven_bot.py
```

You should see:
```
╔══════════════════════════════════════════════════════════════╗
║                    24xRaven Bot Started                      ║
║                  Developed by ✘ 𝙍𝘼𝙑𝙀𝙉                      ║
║                                                              ║
║  Status: ✅ Running                                          ║
║  Version: 1.0.0                                              ║
║                                                              ║
║  Copyright © 2026 ✘ 𝙍𝘼𝙑𝙀𝙉 - All Rights Reserved            ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 🧪 Testing | الاختبار

### Test 1: Basic Functionality | الاختبار 1: الوظائف الأساسية

1. Open Telegram
2. Search for your bot
3. Send `/start`
4. You should see the welcome message

### Test 2: Image Generation | الاختبار 2: توليد الصور

1. Click "🎨 توليد صور AI"
2. Send: "a beautiful sunset"
3. Wait 5-10 seconds
4. You should receive an AI-generated image

### Test 3: Phone Search | الاختبار 3: البحث عن الأرقام

1. Click "📱 البحث بالرقم"
2. Send: "+201234567890" (use a real number)
3. You should receive phone information

### Test 4: IP Analysis | الاختبار 4: تحليل IP

1. Click "🌐 معلومات IP/Domain"
2. Send: "8.8.8.8"
3. You should receive IP information

### Test 5: Admin Commands | الاختبار 5: أوامر المطور

1. Send `/stats`
2. You should see user statistics

---

## 🐛 Troubleshooting | حل المشاكل

### Problem: "Unauthorized" Error

**Cause**: Wrong bot token

**Solution**:
1. Check your token from @BotFather
2. Make sure there are no extra spaces
3. Verify the token in your configuration

---

### Problem: "Module not found"

**Cause**: Missing dependencies

**Solution**:
```bash
pip install -r requirements.txt
```

---

### Problem: Image generation fails

**Cause**: Invalid Hugging Face token or no access to model

**Solution**:
1. Verify your HF token
2. Make sure you're logged in to Hugging Face
3. Check if you have access to the model
4. Try regenerating your token

---

### Problem: Phone search not working

**Cause**: Invalid phone format

**Solution**:
- Use international format: `+[country code][number]`
- Example: `+201234567890` (Egypt)
- Example: `+14155552671` (USA)

---

### Problem: Bot doesn't respond

**Possible causes**:
1. Bot is not running
2. Wrong bot username
3. Bot was blocked by user
4. Network issues

**Solution**:
1. Check if bot process is running
2. Verify bot username
3. Restart the bot
4. Check internet connection

---

## 📊 Configuration Examples | أمثلة الإعداد

### Example 1: Development Setup | مثال 1: إعداد التطوير

```python
# raven_bot.py
TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-EXAMPLE"
OWNER_ID = 1234567890
HF_TOKEN = "hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

### Example 2: Production Setup | مثال 2: إعداد الإنتاج

```bash
# .env
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz-EXAMPLE
OWNER_ID=1234567890
HF_TOKEN=hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

```python
# raven_bot.py
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_ID'))
HF_TOKEN = os.getenv('HF_TOKEN')
```

---

## 🔄 Updating Configuration | تحديث الإعداد

### To Change Bot Token | لتغيير توكن البوت

1. Get new token from @BotFather
2. Update in `raven_bot.py` or `.env`
3. Restart the bot

### To Change Owner ID | لتغيير ID المالك

1. Get your new ID from @userinfobot
2. Update `OWNER_ID` in configuration
3. Restart the bot

### To Change HF Token | لتغيير توكن Hugging Face

1. Generate new token on Hugging Face
2. Update `HF_TOKEN` in configuration
3. Restart the bot

---

## 📞 Need Help? | تحتاج مساعدة؟

If you're still having issues:

- 📖 Read the [Quick Start Guide](QUICKSTART.md)
- 🔒 Check [Security Guidelines](SECURITY.md)
- 💬 Join our [Telegram Channel](https://t.me/Raven_xx24)
- 📧 Email: hsh34811@gmail.com

---

<div align="center">

**Setup Complete! 🎉**

**الإعداد مكتمل! 🎉**

Your bot is ready to use!

البوت جاهز للاستخدام!

---

Made with ❤️ by ✘ 𝙍𝘼𝙑𝙀𝙉

Copyright © 2026 - All Rights Reserved

</div>
