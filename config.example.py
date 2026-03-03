# ═══════════════════════════════════════════════════════════════
# 24xRaven Bot - Configuration File Example
# Developed by ✘ 𝙍𝘼𝙑𝙀𝙉
# 
# GitHub: https://github.com/hsh34811-hash
# Telegram: @P_X_24
# Channel: https://t.me/Raven_xx24
# 
# Copyright © 2026 ✘ 𝙍𝘼𝙑𝙀𝙉 - All Rights Reserved
# ═══════════════════════════════════════════════════════════════

"""
Configuration file for 24xRaven Telegram Bot

Instructions:
1. Copy this file and rename it to 'config.py'
2. Fill in your actual values
3. Never commit config.py to version control
"""

# ═══════════════════════════════════════════════════════════════
# Telegram Bot Configuration
# ═══════════════════════════════════════════════════════════════

# Get your bot token from @BotFather on Telegram
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Your Telegram user ID (you can get it from @userinfobot)
OWNER_ID = 0  # Replace with your actual ID

# ═══════════════════════════════════════════════════════════════
# Hugging Face Configuration
# ═══════════════════════════════════════════════════════════════

# Get your token from https://huggingface.co/settings/tokens
HF_TOKEN = "YOUR_HUGGING_FACE_TOKEN_HERE"

# AI Model for image generation
MODEL_ID = "black-forest-labs/FLUX.1-schnell"

# ═══════════════════════════════════════════════════════════════
# Image Generation Settings
# ═══════════════════════════════════════════════════════════════

IMAGE_WIDTH = 1024
IMAGE_HEIGHT = 1024
GUIDANCE_SCALE = 7.5
NUM_INFERENCE_STEPS = 4

# ═══════════════════════════════════════════════════════════════
# Bot Behavior Settings
# ═══════════════════════════════════════════════════════════════

# Minimum prompt length for image generation
MIN_PROMPT_LENGTH = 8

# Request timeout in seconds
REQUEST_TIMEOUT = 7

# ═══════════════════════════════════════════════════════════════
# Database Settings
# ═══════════════════════════════════════════════════════════════

USERS_FILE = "users.json"

# ═══════════════════════════════════════════════════════════════
# API Endpoints
# ═══════════════════════════════════════════════════════════════

IP_API_URL = "http://ip-api.com/json/{target}"

# ═══════════════════════════════════════════════════════════════
# Messages Configuration (Optional Customization)
# ═══════════════════════════════════════════════════════════════

WELCOME_MESSAGE = """
╔══════════════════════════════════════════════════════════════╗
║                    24xRaven Telegram Bot                     ║
║                  Developed by ✘ 𝙍𝘼𝙑𝙀𝙉                      ║
╚══════════════════════════════════════════════════════════════╝

مرحباً بك في بوت 24xRaven
البوت الأقوى للخدمات الاحترافية

⚡ الميزات المتاحة:
━━━━━━━━━━━━━━━━━━━━
🎨 توليد صور بالذكاء الاصطناعي
📱 البحث المتقدم عن الأرقام
🌐 تحليل IP والدومينات

اختر الخدمة من القائمة أدناه ⬇️
"""

# ═══════════════════════════════════════════════════════════════
# Logging Configuration
# ═══════════════════════════════════════════════════════════════

LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "bot.log"

# ═══════════════════════════════════════════════════════════════
# Feature Flags
# ═══════════════════════════════════════════════════════════════

ENABLE_IMAGE_GENERATION = True
ENABLE_PHONE_SEARCH = True
ENABLE_IP_ANALYSIS = True
ENABLE_USER_TRACKING = True
ENABLE_OWNER_NOTIFICATIONS = True

# ═══════════════════════════════════════════════════════════════
# Rate Limiting (Optional - for future implementation)
# ═══════════════════════════════════════════════════════════════

MAX_REQUESTS_PER_USER_PER_HOUR = 50
MAX_IMAGE_GENERATIONS_PER_DAY = 20

# ═══════════════════════════════════════════════════════════════
# Advanced Settings
# ═══════════════════════════════════════════════════════════════

# Threading settings
MAX_WORKER_THREADS = 5

# Cache settings
ENABLE_CACHE = False
CACHE_EXPIRY_SECONDS = 3600

# ═══════════════════════════════════════════════════════════════
# End of Configuration
# ═══════════════════════════════════════════════════════════════
