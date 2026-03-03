# ⚡ Quick Start Guide | دليل البدء السريع

## 24xRaven Bot - Get Started in 5 Minutes!

**Developed by ✘ 𝙍𝘼𝙑𝙀𝙉**

---

## 🎯 Prerequisites | المتطلبات

Before you begin, make sure you have:

- ✅ Python 3.8 or higher installed
- ✅ A Telegram account
- ✅ Basic command line knowledge
- ✅ 5 minutes of your time!

---

## 🚀 Installation | التثبيت

### Step 1: Get the Code | الخطوة 1: احصل على الكود

```bash
# Clone the repository
git clone https://github.com/hsh34811-hash/24xRaven-Bot.git

# Navigate to the directory
cd 24xRaven-Bot
```

### Step 2: Install Dependencies | الخطوة 2: تثبيت المكتبات

```bash
# Install required packages
pip install -r requirements.txt
```

That's it! The bot will auto-install any missing libraries when it runs.

---

## 🔑 Configuration | الإعدادات

### Step 3: Get Your Bot Token | الخطوة 3: احصل على توكن البوت

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Follow the instructions
4. Copy your bot token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 4: Get Your User ID | الخطوة 4: احصل على ID الخاص بك

1. Search for [@userinfobot](https://t.me/userinfobot) on Telegram
2. Start the bot
3. Copy your user ID (a number like: `123456789`)

### Step 5: Get Hugging Face Token | الخطوة 5: احصل على توكن Hugging Face

1. Go to [Hugging Face](https://huggingface.co/)
2. Sign up or log in
3. Go to Settings → Access Tokens
4. Create a new token
5. Copy the token

### Step 6: Configure the Bot | الخطوة 6: إعداد البوت

Open `raven_bot.py` and find these lines:

```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
OWNER_ID = 0
HF_TOKEN = "YOUR_HUGGING_FACE_TOKEN_HERE"
```

Replace with your values:

```python
TOKEN = "YOUR_BOT_TOKEN_HERE"
OWNER_ID = YOUR_USER_ID_HERE
HF_TOKEN = "YOUR_HF_TOKEN_HERE"
```
HF_TOKEN = "YOUR_HF_TOKEN_HERE"
```

---

## ▶️ Running the Bot | تشغيل البوت

### Step 7: Start the Bot | الخطوة 7: ابدأ البوت

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

🎉 **Congratulations! Your bot is now running!**

---

## 📱 Using the Bot | استخدام البوت

### Step 8: Test Your Bot | الخطوة 8: اختبر البوت

1. Open Telegram
2. Search for your bot (the username you created with BotFather)
3. Send `/start`
4. You should see the welcome message!

### Available Features | الميزات المتاحة

#### 🎨 Generate AI Images | توليد صور بالذكاء الاصطناعي

1. Click "🎨 توليد صور AI"
2. Type your image description (e.g., "a beautiful sunset over mountains")
3. Wait 5-10 seconds
4. Receive your AI-generated image!

**Tips for better results:**
- Be specific in your description
- Use descriptive adjectives
- Mention style if desired (e.g., "realistic", "cartoon", "oil painting")

#### 📱 Search Phone Numbers | البحث عن الأرقام

1. Click "📱 البحث بالرقم"
2. Enter phone number in international format (e.g., `+201234567890`)
3. Get detailed information:
   - Country and region
   - Carrier name
   - Line type
   - WhatsApp and Telegram links

#### 🌐 Analyze IP/Domain | تحليل IP والدومينات

1. Click "🌐 معلومات IP/Domain"
2. Enter an IP address (e.g., `8.8.8.8`) or domain (e.g., `google.com`)
3. Get comprehensive information:
   - Geographic location
   - ISP and organization
   - Map location
   - Network details

---

## 🛠️ Troubleshooting | حل المشاكل

### Bot doesn't start | البوت لا يعمل

**Problem**: `ModuleNotFoundError`
```bash
# Solution: Install missing package
pip install package_name
```

**Problem**: `Unauthorized` error
```bash
# Solution: Check your bot token
# Make sure you copied it correctly from BotFather
```

### Image generation fails | فشل توليد الصور

**Problem**: Timeout or error
```bash
# Solution: Check your Hugging Face token
# Make sure you have access to the model
# Try again after a few seconds
```

### Phone search not working | البحث عن الأرقام لا يعمل

**Problem**: Invalid format
```bash
# Solution: Use international format
# Correct: +201234567890
# Wrong: 01234567890
```

---

## 📊 Admin Commands | أوامر المطور

As the bot owner, you have access to special commands:

### `/stats` - View Statistics

Shows:
- Total number of users
- Bot activity

Example:
```
/stats
```

Response:
```
╔══════════════════════════════════════════════════════════════╗
║                    📊 إحصائيات البوت                        ║
╚══════════════════════════════════════════════════════════════╝

👥 إجمالي المستخدمين: 42

━━━━━━━━━━━━━━━━━━━━
⚡ 24xRaven Bot
```

---

## 🔄 Keeping the Bot Running | إبقاء البوت يعمل

### Option 1: Screen (Linux) | الخيار 1: Screen

```bash
# Start a screen session
screen -S raven-bot

# Run the bot
python raven_bot.py

# Detach: Press Ctrl+A then D
# Reattach: screen -r raven-bot
```

### Option 2: nohup (Linux/Mac) | الخيار 2: nohup

```bash
nohup python raven_bot.py &
```

### Option 3: PM2 (Recommended) | الخيار 3: PM2 (موصى به)

```bash
# Install PM2
npm install -g pm2

# Start bot
pm2 start raven_bot.py --name raven-bot --interpreter python3

# View logs
pm2 logs raven-bot

# Stop bot
pm2 stop raven-bot

# Restart bot
pm2 restart raven-bot
```

### Option 4: Systemd Service (Linux) | الخيار 4: خدمة Systemd

Create `/etc/systemd/system/raven-bot.service`:

```ini
[Unit]
Description=24xRaven Telegram Bot
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/path/to/24xRaven-Bot
ExecStart=/usr/bin/python3 /path/to/24xRaven-Bot/raven_bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Then:
```bash
sudo systemctl enable raven-bot
sudo systemctl start raven-bot
sudo systemctl status raven-bot
```

---

## 🌐 Deployment Options | خيارات النشر

### Free Hosting Options | خيارات الاستضافة المجانية

1. **Heroku** (Free tier available)
2. **Railway** (Free tier available)
3. **Render** (Free tier available)
4. **PythonAnywhere** (Free tier available)

### VPS Options | خيارات VPS

1. **DigitalOcean** ($5/month)
2. **Linode** ($5/month)
3. **Vultr** ($2.50/month)
4. **AWS EC2** (Free tier for 1 year)

---

## 📚 Next Steps | الخطوات التالية

Now that your bot is running, you can:

1. ✅ Customize the welcome message
2. ✅ Add more features
3. ✅ Share with friends
4. ✅ Deploy to a server
5. ✅ Contribute to the project

---

## 🆘 Need Help? | تحتاج مساعدة؟

- 📖 Read the [full documentation](README.md)
- 🏗️ Check the [architecture guide](ARCHITECTURE.md)
- 🤝 See [contributing guidelines](CONTRIBUTING.md)
- 💬 Join our [Telegram channel](https://t.me/Raven_xx24)
- 📧 Email: hsh34811@gmail.com

---

## 🎉 Success Checklist | قائمة النجاح

- [ ] Bot token configured
- [ ] Owner ID set
- [ ] Hugging Face token added
- [ ] Dependencies installed
- [ ] Bot started successfully
- [ ] Tested `/start` command
- [ ] Generated an AI image
- [ ] Searched a phone number
- [ ] Analyzed an IP address
- [ ] Checked `/stats` command

If you checked all boxes, you're all set! 🚀

---

<div align="center">

**Made with ❤️ by ✘ 𝙍𝘼𝙑𝙀𝙉**

[GitHub](https://github.com/hsh34811-hash) • [Telegram](https://t.me/P_X_24) • [Channel](https://t.me/Raven_xx24)

Copyright © 2026 - All Rights Reserved

</div>
