# 🏗️ Architecture Documentation | التوثيق المعماري

## 24xRaven Bot - Technical Architecture

**Developed by ✘ 𝙍𝘼𝙑𝙀𝙉**

---

## 📋 Table of Contents | المحتويات

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Core Components](#core-components)
4. [Data Flow](#data-flow)
5. [API Integration](#api-integration)
6. [Security](#security)
7. [Performance](#performance)
8. [Future Enhancements](#future-enhancements)

---

## 🎯 Overview | نظرة عامة

24xRaven Bot is built using a modular, event-driven architecture that ensures:
- **Scalability**: Handle multiple concurrent requests
- **Maintainability**: Clean, documented code structure
- **Extensibility**: Easy to add new features
- **Reliability**: Error handling and recovery mechanisms

### Technology Stack | المكدس التقني

```
┌─────────────────────────────────────┐
│         Python 3.8+                 │
├─────────────────────────────────────┤
│  pyTelegramBotAPI (Telegram API)    │
│  Hugging Face Hub (AI Models)       │
│  Requests (HTTP Client)             │
│  PhoneNumbers (Phone Analysis)      │
│  Pillow (Image Processing)          │
└─────────────────────────────────────┘
```

---

## 🏛️ System Architecture | البنية المعمارية

```
┌──────────────────────────────────────────────────────────┐
│                    Telegram Client                       │
└────────────────────┬─────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────┐
│                  24xRaven Bot Core                       │
│  ┌────────────────────────────────────────────────────┐  │
│  │           Command Handler Layer                    │  │
│  │  • /start  • /stats  • Callback Queries           │  │
│  └────────────────────────────────────────────────────┘  │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────────────┐  │
│  │          Business Logic Layer                      │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐        │  │
│  │  │  Image   │  │  Phone   │  │    IP    │        │  │
│  │  │   Gen    │  │  Search  │  │ Analysis │        │  │
│  │  └──────────┘  └──────────┘  └──────────┘        │  │
│  └────────────────────────────────────────────────────┘  │
│                          │                               │
│                          ▼                               │
│  ┌────────────────────────────────────────────────────┐  │
│  │           Data Access Layer                        │  │
│  │  • User Management  • Statistics  • Logging       │  │
│  └────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────────────────┐
│              External Services                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │ Hugging  │  │ IP-API   │  │  Phone   │              │
│  │   Face   │  │   .com   │  │ Numbers  │              │
│  └──────────┘  └──────────┘  └──────────┘              │
└──────────────────────────────────────────────────────────┘
```

---

## 🔧 Core Components | المكونات الأساسية

### 1. Command Handler | معالج الأوامر

**Purpose**: Process user commands and route to appropriate handlers

```python
@bot.message_handler(commands=['start'])
def start(msg):
    # Handle /start command
    pass
```

**Features**:
- Command routing
- User authentication
- Input validation
- Error handling

### 2. Image Generation Module | وحدة توليد الصور

**Purpose**: Generate AI images using Hugging Face models

**Flow**:
```
User Input → Validation → API Request → Image Processing → Response
```

**Key Functions**:
- `generate_image()`: Entry point
- `real_image_gen()`: Async processing
- Threading for non-blocking execution

### 3. Phone Search Module | وحدة البحث عن الأرقام

**Purpose**: Analyze phone numbers and provide detailed information

**Data Retrieved**:
- Country and region
- Carrier information
- Line type (mobile/landline)
- Social media links

**Libraries Used**:
- `phonenumbers`: Number parsing and validation
- `geocoder`: Geographic information
- `carrier`: Carrier identification

### 4. IP Analysis Module | وحدة تحليل IP

**Purpose**: Analyze IP addresses and domains

**Information Provided**:
- Geographic location
- ISP and organization
- Coordinates for mapping
- Network details

**API**: ip-api.com

### 5. User Management System | نظام إدارة المستخدمين

**Purpose**: Track users and provide statistics

**Features**:
- New user detection
- User database (JSON)
- Owner notifications
- Statistics generation

**Data Structure**:
```json
[
    user_id_1,
    user_id_2,
    ...
]
```

---

## 🔄 Data Flow | تدفق البيانات

### Image Generation Flow | تدفق توليد الصور

```
1. User clicks "🎨 توليد صور AI"
   ↓
2. Bot prompts for description
   ↓
3. User sends description
   ↓
4. Validation (length check)
   ↓
5. Show waiting message
   ↓
6. Thread spawned for processing
   ↓
7. API call to Hugging Face
   ↓
8. Image received and processed
   ↓
9. Delete waiting message
   ↓
10. Send image to user
```

### Phone Search Flow | تدفق البحث عن الأرقام

```
1. User clicks "📱 البحث بالرقم"
   ↓
2. Bot prompts for phone number
   ↓
3. User sends number
   ↓
4. Format validation
   ↓
5. Show waiting message
   ↓
6. Parse number with phonenumbers
   ↓
7. Retrieve carrier and location
   ↓
8. Generate social media links
   ↓
9. Format response
   ↓
10. Send to user
```

---

## 🔌 API Integration | تكامل الـ API

### Hugging Face API

**Endpoint**: Inference API
**Model**: black-forest-labs/FLUX.1-schnell
**Authentication**: Bearer token

```python
client = InferenceClient(token=HF_TOKEN)
image = client.text_to_image(
    prompt,
    model=MODEL_ID,
    guidance_scale=7.5,
    num_inference_steps=4,
    width=1024,
    height=1024
)
```

### IP-API

**Endpoint**: http://ip-api.com/json/{target}
**Method**: GET
**Response**: JSON

```python
response = requests.get(
    f"http://ip-api.com/json/{target}",
    timeout=7
)
```

---

## 🔒 Security | الأمان

### Current Measures | الإجراءات الحالية

1. **Owner Verification**
   - Commands like `/stats` restricted to OWNER_ID
   
2. **Input Validation**
   - Phone number format checking
   - Prompt length validation
   - IP/Domain format verification

3. **Error Handling**
   - Try-catch blocks for all API calls
   - Graceful degradation
   - User-friendly error messages

4. **Rate Limiting** (Planned)
   - Per-user request limits
   - Daily quotas for resource-intensive operations

### Recommendations | التوصيات

- [ ] Implement database encryption
- [ ] Add API key rotation
- [ ] Enable HTTPS for all external calls
- [ ] Add request signing
- [ ] Implement user authentication levels

---

## ⚡ Performance | الأداء

### Current Optimizations | التحسينات الحالية

1. **Multi-threading**
   - Non-blocking operations
   - Concurrent request handling
   
2. **Async Processing**
   - Background tasks for heavy operations
   - Immediate user feedback

3. **Resource Management**
   - Automatic library installation
   - Memory-efficient image handling

### Performance Metrics | مقاييس الأداء

| Operation | Average Time | Max Time |
|-----------|-------------|----------|
| Image Generation | 5-10s | 15s |
| Phone Search | 1-2s | 5s |
| IP Analysis | 1-3s | 7s |
| Command Response | <1s | 2s |

### Future Optimizations | التحسينات المستقبلية

- [ ] Implement caching for frequent requests
- [ ] Database connection pooling
- [ ] CDN for static assets
- [ ] Load balancing for multiple instances
- [ ] Redis for session management

---

## 🚀 Future Enhancements | التحسينات المستقبلية

### Planned Features | الميزات المخططة

1. **Database Migration**
   - Move from JSON to SQLite/PostgreSQL
   - Better data persistence
   - Advanced querying

2. **Admin Panel**
   - Web-based dashboard
   - User management
   - Analytics and reporting

3. **Multi-language Support**
   - Language detection
   - Translation API integration
   - Localized responses

4. **Advanced AI Features**
   - Image editing
   - Style transfer
   - Multiple AI models

5. **Subscription System**
   - Premium features
   - Usage quotas
   - Payment integration

### Scalability Plan | خطة التوسع

```
Current: Single Instance
   ↓
Phase 1: Load Balancer + Multiple Instances
   ↓
Phase 2: Microservices Architecture
   ↓
Phase 3: Kubernetes Deployment
   ↓
Phase 4: Global CDN + Edge Computing
```

---

## 📊 Monitoring & Logging | المراقبة والتسجيل

### Current Logging | التسجيل الحالي

- Console output for bot status
- Error messages to user
- Owner notifications for new users

### Planned Monitoring | المراقبة المخططة

- [ ] Structured logging (JSON format)
- [ ] Log aggregation (ELK Stack)
- [ ] Performance monitoring (Prometheus)
- [ ] Error tracking (Sentry)
- [ ] Uptime monitoring

---

## 🧪 Testing Strategy | استراتيجية الاختبار

### Current Testing | الاختبار الحالي

- Manual testing
- User feedback

### Planned Testing | الاختبار المخطط

- [ ] Unit tests for core functions
- [ ] Integration tests for API calls
- [ ] End-to-end tests for user flows
- [ ] Load testing for scalability
- [ ] Security testing

---

## 📞 Contact | التواصل

For technical questions or contributions:

- **GitHub**: [hsh34811-hash](https://github.com/hsh34811-hash)
- **Telegram**: [@P_X_24](https://t.me/P_X_24)
- **Channel**: [Raven_xx24](https://t.me/Raven_xx24)
- **Email**: hsh34811@gmail.com

---

<div align="center">

**Developed with ❤️ by ✘ 𝙍𝘼𝙑𝙀𝙉**

Copyright © 2026 - All Rights Reserved

</div>
