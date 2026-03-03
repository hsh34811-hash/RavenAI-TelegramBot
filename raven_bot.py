import telebot 
from telebot import types
import requests
import subprocess
import sys
import io
import threading
import json
import os

╔══════════════════════════════════════════════════════════════╗
║                    24xRaven Telegram Bot                     ║
║                  Developed by ✘ 𝙍𝘼𝙑𝙀𝙉                      ║
║                                                              ║
║  GitHub: https://github.com/hsh34811-hash                    ║
║  Telegram: @P_X_24                                           ║
║  Channel: https://t.me/Raven_xx24                            ║
║                                                              ║
║  Copyright © 2026 ✘ 𝙍𝘼𝙑𝙀𝙉 - All Rights Reserved            ║
╚══════════════════════════════════════════════════════════════╝

# ═══════════════════════════════════════════════════════════════
# تثبيت المكتبات المطلوبة تلقائياً
# ═══════════════════════════════════════════════════════════════
def install(p):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", p], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except: pass

REQUIRED_LIBS = ["pyTelegramBotAPI", "requests", "phonenumbers", "huggingface_hub"] 

for lib in REQUIRED_LIBS:
    try: __import__(lib.split()[0])
    except: install(lib)

# ═══════════════════════════════════════════════════════════════
# استيراد المكتبات الأساسية
# ═══════════════════════════════════════════════════════════════
import telebot, requests
try:
    import phonenumbers
    from phonenumbers import geocoder, carrier
    from huggingface_hub import InferenceClient
except ImportError:
    phonenumbers = None
    geocoder = None
    carrier = None
    InferenceClient = object

# ═══════════════════════════════════════════════════════════════
# إعدادات البوت الرئيسية
# ═══════════════════════════════════════════════════════════════
TOKEN = "YOUR_BOT_TOKEN_HERE"  # احصل على التوكن من @BotFather
OWNER_ID = 0  # ضع رقم ID الخاص بك هنا (احصل عليه من @userinfobot)
bot = telebot.TeleBot(TOKEN)

# ═══════════════════════════════════════════════════════════════
# إعدادات Hugging Face API
# ═══════════════════════════════════════════════════════════════
HF_TOKEN = "YOUR_HUGGING_FACE_TOKEN_HERE"  # احصل عليه من https://huggingface.co/settings/tokens
MODEL_ID = "black-forest-labs/FLUX.1-schnell"

# ═══════════════════════════════════════════════════════════════
# نظام إدارة وتتبع المستخدمين
# ═══════════════════════════════════════════════════════════════
USERS_FILE = "users.json"

def load_users():
    """
    ═══════════════════════════════════════════════════════════════
    تحميل قائمة المستخدمين من ملف JSON
    ═══════════════════════════════════════════════════════════════
    """
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_users(users):
    """
    ═══════════════════════════════════════════════════════════════
    حفظ قائمة المستخدمين في ملف JSON
    ═══════════════════════════════════════════════════════════════
    """
    try:
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f)
    except:
        pass

def notify_owner_new_user(user_info):
    """
    ═══════════════════════════════════════════════════════════════
    إرسال إشعار فوري للمطور عند تسجيل مستخدم جديد
    ═══════════════════════════════════════════════════════════════
    """
    try:
        notification = f"""
╔══════════════════════╗
║   🔔 مستخدم جديد   ║
╚══════════════════════╝

👤 الاسم: {user_info['first_name']}
🆔 المعرف: @{user_info['username'] if user_info['username'] else 'لا يوجد'}
🔢 ID: {user_info['user_id']}
📅 التاريخ: {user_info['date']}

━━━━━━━━━━━━━━━━━━━━
📊 إجمالي المستخدمين: {user_info['total_users']}
⚡ 24xRaven Bot
"""
        bot.send_message(OWNER_ID, notification)
    except Exception as e:
        print(f"Failed to notify owner: {e}")

# ═══════════════════════════════════════════════════════════════
# نظام تحليل IP والدومينات
# ═══════════════════════════════════════════════════════════════
def get_info(target):
    """
    ═══════════════════════════════════════════════════════════════
    جلب معلومات الموقع الجغرافي الكاملة للـ IP أو Domain
    ═══════════════════════════════════════════════════════════════
    """
    try:
        r = requests.get(f"http://ip-api.com/json/{target}", timeout=7).json()
        if r.get("status") == "success":
            # تنظيف البيانات من الأحرف الخاصة
            country = str(r.get('country', 'N/A')).replace('_', ' ')
            region = str(r.get('regionName', 'N/A')).replace('_', ' ')
            city = str(r.get('city', 'N/A')).replace('_', ' ')
            isp = str(r.get('isp', 'N/A')).replace('_', ' ')
            org = str(r.get('org', 'N/A')).replace('_', ' ')
            as_info = str(r.get('as', 'N/A')).replace('_', ' ')
            lat = r.get('lat', 0)
            lon = r.get('lon', 0)
            
            info = f"""معلومات {target}

🌍 الموقع:
الدولة: {country} ({r.get('countryCode', 'N/A')})
المنطقة: {region}
المدينة: {city}

📍 الإحداثيات:
خط العرض: {lat}
خط الطول: {lon}

🌐 معلومات الشبكة:
IP: {r.get('query', 'N/A')}
المزود: {isp}
المنظمة: {org}
AS: {as_info}

⏰ المنطقة الزمنية: {r.get('timezone', 'N/A')}
"""
            return info, lat, lon
        else:
            return "تعذر جلب بيانات الموقع. تأكد من صحة الـ IP أو Domain.", None, None
    except Exception as e:
        return f"خطأ في جلب البيانات: {str(e)[:100]}", None, None

# ═══════════════════════════════════════════════════════════════
# نظام البحث المتقدم عن الأرقام
# ═══════════════════════════════════════════════════════════════
def phone_osint_pro(msg):
    try:
        if not phonenumbers:
            bot.reply_to(msg, "⚠️ خطأ: مكتبة phonenumbers غير متوفرة.")
            return
        number = msg.text.strip().replace(" ", "")
        if not number.startswith('+'):
            bot.reply_to(msg, "⚠️ الرقم يجب أن يبدأ بالكود الدولي (مثال: +201234567890)")
            return
        wait_msg = bot.reply_to(msg, "🔍 جاري البحث عن الرقم...")
        threading.Thread(target=real_phone_osint_pro, args=(msg.chat.id, number, wait_msg.message_id), daemon=True).start()
    except Exception as e: 
        bot.send_message(msg.chat.id, f"❌ فشل: {str(e)[:50]}")

def real_phone_osint_pro(cid, number, wait_msg_id):
    try:
        import time
        # رسائل انتظار
        bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text="🔍 جاري البحث عن الرقم...\n⏳ تحليل البيانات...")
        time.sleep(1)
        
        bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text="🔍 جاري البحث عن الرقم...\n⏳ تحليل البيانات...\n📡 جلب المعلومات...")
        
        parsed = phonenumbers.parse(number)
        international = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        country = geocoder.description_for_number(parsed, "ar")
        carrier_name = carrier.name_for_number(parsed, "ar") or "غير معروف"
        line_type = "موبايل" if phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.MOBILE else "أرضي"
        
        wa = f"https://wa.me/{number[1:]}"
        tg = f"https://t.me/+{number[1:]}"
        
        # حذف رسالة الانتظار
        bot.delete_message(cid, wait_msg_id)
        
        result = f"""
╔══════════════════════╗
║   📱 معلومات الرقم   ║
╚══════════════════════╝

📞 الرقم الدولي:
   {international}

🌍 الموقع:
   {country}

📡 المشغل:
   {carrier_name}

📶 نوع الخط:
   {line_type}

━━━━━━━━━━━━━━━━━━━━
🔗 الحسابات المرتبطة:

💬 WhatsApp: {wa}
✈️ Telegram: {tg}

━━━━━━━━━━━━━━━━━━━━
⚡ Powered by 24xRaven
"""
        
        bot.send_message(cid, result, disable_web_page_preview=True)
    except Exception as e:
        try:
            bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text=f"❌ خطأ في الفحص: {str(e)[:100]}")
        except:
            bot.send_message(cid, f"❌ خطأ في الفحص: {str(e)[:100]}")

# ═══════════════════════════════════════════════════════════════
# نظام توليد الصور بالذكاء الاصطناعي
# ═══════════════════════════════════════════════════════════════
def generate_image(msg):
    try:
        if not InferenceClient:
            bot.reply_to(msg, "⚠️ خطأ: مكتبات توليد الصور غير جاهزة.")
            return
        prompt = msg.text.strip()
        if len(prompt) < 8:
            bot.reply_to(msg, "⚠️ الوصف قصير جداً، اكتب وصف أطول للحصول على نتائج أفضل")
            return
        wait_msg = bot.reply_to(msg, "🎨 جاري تحضير الصورة...")
        threading.Thread(target=real_image_gen, args=(msg.chat.id, prompt, wait_msg.message_id), daemon=True).start()
    except Exception as e: 
        bot.send_message(msg.chat.id, f"❌ فشل: {str(e)[:50]}")

def real_image_gen(cid, prompt, wait_msg_id):
    try:
        import time
        # رسائل انتظار متحركة
        bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text="🎨 جاري تحضير الصورة...\n⏳ معالجة الوصف...")
        time.sleep(1)
        
        bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text="🎨 جاري تحضير الصورة...\n⏳ معالجة الوصف...\n🖌️ توليد الصورة بالذكاء الاصطناعي...")
        
        client = InferenceClient(token=HF_TOKEN)
        image = client.text_to_image(prompt, model=MODEL_ID, guidance_scale=7.5, num_inference_steps=4, width=1024, height=1024)
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # حذف رسالة الانتظار
        bot.delete_message(cid, wait_msg_id)
        
        # رسالة احترافية مع الصورة
        caption = f"""
╔══════════════════════╗
║   ✅ تم التوليد بنجاح   ║
╚══════════════════════╝

🎨 المحرك: FLUX.1-schnell
📝 الوصف: {prompt[:100]}{'...' if len(prompt) > 100 else ''}

━━━━━━━━━━━━━━━━━━━━
⚡ Powered by 24xRaven
"""
        bot.send_photo(cid, img_byte_arr, caption=caption)
    except Exception as e:
        try:
            bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text=f"❌ خطأ: {str(e)[:150]}\n\n💡 جرب مرة أخرى بعد قليل")
        except:
            bot.send_message(cid, f"❌ خطأ: {str(e)[:150]}\n\n💡 جرب مرة أخرى بعد قليل")

# ═══════════════════════════════════════════════════════════════
# معالج طلبات معلومات IP/Domain
# ═══════════════════════════════════════════════════════════════
def ip_info_handler(msg):
    try:
        target = msg.text.strip()
        # رسالة انتظار متحركة
        wait_msg = bot.reply_to(msg, "🔍 جاري البحث عن المعلومات...")
        threading.Thread(target=real_ip_info, args=(msg.chat.id, target, wait_msg.message_id), daemon=True).start()
    except Exception as e:
        bot.send_message(msg.chat.id, f"فشل: {str(e)[:80]}")

def real_ip_info(cid, target, wait_msg_id):
    try:
        import time
        # تحديث رسالة الانتظار
        bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text="🔍 جاري البحث عن المعلومات...\n⏳ جاري تحليل البيانات...")
        time.sleep(1)
        
        bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text="🔍 جاري البحث عن المعلومات...\n⏳ جاري تحليل البيانات...\n📡 جاري جلب الموقع الجغرافي...")
        
        # جلب المعلومات
        info, lat, lon = get_info(target)
        
        if lat and lon:
            # حذف رسالة الانتظار
            bot.delete_message(cid, wait_msg_id)
            
            # رابط Google Maps
            google_maps_link = f"https://www.google.com/maps?q={lat},{lon}"
            
            # تحسين عرض المعلومات
            info_formatted = f"""
╔══════════════════════╗
║   🌐 معلومات {target}   ║
╚══════════════════════╝

{info}

🗺️ عرض على الخريطة:
{google_maps_link}

━━━━━━━━━━━━━━━━━━━━
⚡ Powered by 24xRaven
"""
            
            # إرسال الموقع كـ Location في Telegram
            try:
                bot.send_location(cid, latitude=lat, longitude=lon)
                bot.send_message(cid, info_formatted)
            except:
                # إذا فشل إرسال الموقع، إرسال المعلومات فقط
                bot.send_message(cid, info_formatted)
        else:
            bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text=info)
            
    except Exception as e:
        try:
            bot.edit_message_text(chat_id=cid, message_id=wait_msg_id, text=f"❌ فشل: {str(e)[:80]}")
        except:
            bot.send_message(cid, f"❌ فشل: {str(e)[:80]}")

# ═══════════════════════════════════════════════════════════════
# القائمة الرئيسية للبوت
# ═══════════════════════════════════════════════════════════════
def main_menu():
    m = types.InlineKeyboardMarkup(row_width=2)
    m.add(
        types.InlineKeyboardButton("🎨 توليد صور AI", callback_data="tool_image"),
        types.InlineKeyboardButton("� البحث بالرقم", callback_data="tool_phone")
    )
    m.add(
        types.InlineKeyboardButton("🌐 معلومات IP/Domain", callback_data="tool_ip")
    )
    return m

# ═══════════════════════════════════════════════════════════════
# معالجات الأوامر الرئيسية
# ═══════════════════════════════════════════════════════════════
@bot.message_handler(commands=['start'])
def start(msg):
    user_id = msg.from_user.id
    first_name = msg.from_user.first_name or "مستخدم"
    username = msg.from_user.username
    
    # تحميل قائمة المستخدمين
    users = load_users()
    
    # التحقق إذا كان المستخدم جديد
    if user_id not in users:
        users.append(user_id)
        save_users(users)
        
        # إرسال إشعار للأونر
        import datetime
        user_info = {
            'user_id': user_id,
            'first_name': first_name,
            'username': username,
            'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'total_users': len(users)
        }
        threading.Thread(target=notify_owner_new_user, args=(user_info,), daemon=True).start()
    
    welcome_text = """
╔══════════════════════╗
║   🦅 24xRaven Bot 🦅   ║
╚══════════════════════╝

مرحباً بك في بوت 24xRaven
البوت الأقوى للخدمات الاحترافية

⚡ الميزات المتاحة:
━━━━━━━━━━━━━━━━━━━━
🎨 توليد صور بالذكاء الاصطناعي
📱 البحث المتقدم عن الأرقام
🌐 تحليل IP والدومينات

اختر الخدمة من القائمة أدناه ⬇️
"""
    bot.send_message(msg.chat.id, welcome_text, reply_markup=main_menu())

# ═══════════════════════════════════════════════════════════════
# أمر الإحصائيات (للمطور فقط)
# ═══════════════════════════════════════════════════════════════
@bot.message_handler(commands=['stats'])
def stats(msg):
    if msg.from_user.id == OWNER_ID:
        users = load_users()
        stats_text = f"""
╔══════════════════════╗
║   📊 إحصائيات البوت   ║
╚══════════════════════╝

👥 إجمالي المستخدمين: {len(users)}

━━━━━━━━━━━━━━━━━━━━
⚡ 24xRaven Bot
"""
        bot.send_message(msg.chat.id, stats_text)
    else:
        bot.send_message(msg.chat.id, "⚠️ هذا الأمر متاح للمطور فقط")

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    uid = call.message.chat.id
    mid = call.message.message_id
    
    if call.data == "tool_image":
        bot.edit_message_text(chat_id=uid, message_id=mid, text="🎨 توليد صور بالذكاء الاصطناعي\n\n📝 اكتب وصف الصورة التي تريد توليدها:\n(كلما كان الوصف أدق، كانت النتيجة أفضل)")
        bot.register_next_step_handler_by_chat_id(uid, generate_image)
    
    elif call.data == "tool_phone":
        bot.edit_message_text(chat_id=uid, message_id=mid, text="📱 البحث المتقدم عن الأرقام\n\n📞 أدخل رقم الهاتف بالصيغة الدولية:\n(مثال: +201234567890)")
        bot.register_next_step_handler_by_chat_id(uid, phone_osint_pro)
    
    elif call.data == "tool_ip":
        bot.edit_message_text(chat_id=uid, message_id=mid, text="🌐 تحليل IP والدومينات\n\n🔍 أدخل IP أو Domain:\n(مثال: 8.8.8.8 أو google.com)")
        bot.register_next_step_handler_by_chat_id(uid, ip_info_handler)

# ═══════════════════════════════════════════════════════════════
# تشغيل البوت
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    24xRaven Bot Started                      ║
║                  Developed by ✘ 𝙍𝘼𝙑𝙀𝙉                      ║
║                                                              ║
║  Status: ✅ Running                                          ║
║  Version: 1.0.0                                              ║
║                                                              ║
║  Copyright © 2026 ✘ 𝙍𝘼𝙑𝙀𝙉 - All Rights Reserved            ║
╚══════════════════════════════════════════════════════════════╝
    """)
    bot.infinity_polling()
