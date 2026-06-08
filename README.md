---
title: Global System (GS)
emoji: 🚀
colorFrom: blue
colorTo: green
sdk: docker
pinned: false
---

# 🌍 Global System (GS) - Telegram Delivery Bot

ប្រព័ន្ធលូកទូលាយសម្រាប់គ្រប់គ្រងលម្អិតលម្អឹងលក់ដោយប្រើ Telegram Bot

A comprehensive system for managing delivery orders through Telegram Bot, built with Python and connected to MySQL database.

---

## ✨ Features | មុខងារ

- 🤖 **Telegram Bot Integration** - គ្រប់គ្រងលម្អិតលម្អឹងលក់តាមរយៈ Telegram
- 📍 **Location Tracking** - ស្វាគមន៍ទីតាំង GPS និងដូរស្វាគមន៍ដើម្បីដឹក
- 📊 **Database Management** - រក្សាទុកលម្អិតលម្អឹងលក់ក្នុងទិន្នន័យ MySQL
- 🔐 **Admin Controls** - ក្របខ័ណ្ឋការគ្រប់គ្រងសម្រាប់អ្នកគ្រប់គ្រងប្រព័ន្ធ
- 🌐 **RESTful API** - សេវាកម្ម API សម្រាប់ទំនាក់ទំនងខាងក្រៅ
- ⚡ **Async/Await** - ដំណើរការលឿនលឿន និងដោះស្រាយលំហូរដែលបង់លែង

---

## 📁 Project Structure | រចនាសម្ព័ន្ធគម្រោង

```
Global-System/
├── main.py                 # ឯកសារចម្បងដើម្បីចាប់ផ្តើម Bot
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── README.md              # ឯកសារនេះ
├── config/
│   └── settings.py        # ការកំណត់ និងប៉ារ៉ាម៉ែត្របន្ថែម
├── handlers/
│   ├── __init__.py
│   ├── commands.py        # សេវាកម្មលេខបញ្ជាលក់ (/start, /help, etc)
│   └── messages.py        # ឧបសគ្គនៃសារ
├── services/
│   └── api_service.py     # សេវាកម្ម API និងមូលដ្ឋានទិន្នន័យ
└── dashboard/
    ├── dashboard.py       # ក្របខ័ណ្ឋ Dashboard (Web UI)
    └── index.py          # បង្ហាញទិន្នន័យ
```

---

## 🔧 Requirements | តម្រូវការ

- **Python** 3.8+
- **MySQL** 5.7+ (Clever Cloud or Local)
- **Telegram Bot API** token
- **Docker** (for deployment)

---

## 📦 Installation | ការដំឡើង

### 1️⃣ Clone Repository
```bash
git clone <your-repo-url>
cd Global-System
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables
Create `.env` file in the root directory:

```env
# Telegram Bot Token
BOT_TOKEN=your_telegram_bot_token_here

# MySQL Database URL
DATABASE_URL=mysql://username:password@host:port/database

# Admin IDs (comma-separated)
ADMIN_IDS=123456789,987654321

# Optional: Port for Web Server
PORT=8080
```

**Get Telegram Bot Token:**
1. Search `@BotFather` on Telegram
2. Use `/newbot` command
3. Copy the token provided

---

## 🚀 Running the Bot | ដំណើរការ Bot

### Local Development
```bash
python main.py
```

### Docker Deployment
```bash
docker build -t global-system .
docker run -e BOT_TOKEN=your_token -e DATABASE_URL=your_db_url global-system
```

---

## 📚 Services Documentation | ឯកសារសេវាកម្ម

### APIService (API ឥតលេខសម្គាល់)
Located in `services/api_service.py`

**Methods:**
- `api_service.get(url, headers, params)` - GET requests
- `api_service.post(url, data)` - POST requests
- `api_service.put(url, data)` - PUT requests
- `api_service.delete(url)` - DELETE requests

**Usage Example:**
```python
from services.api_service import api_service

# Fetch external data
result = await api_service.get("https://api.example.com/data")
if result["success"]:
    data = result["data"]
```

### DatabaseService (សេវាកម្មមូលដ្ឋានទិន្នន័យ)
Located in `services/api_service.py`

**Methods:**
- `db_service.fetch_one(sql, params)` - Get single record
- `db_service.fetch_all(sql, params)` - Get multiple records
- `db_service.insert(sql, params)` - Insert new data
- `db_service.update(sql, params)` - Update existing data
- `db_service.delete(sql, params)` - Delete records

**Usage Example:**
```python
from services.api_service import db_service

# Fetch customers
customers = db_service.fetch_all(
    "SELECT * FROM customers WHERE city = %s", 
    ("Phnom Penh",)
)

# Create new order
order_id = db_service.insert(
    "INSERT INTO orders (customer_id, amount) VALUES (%s, %s)",
    (123, 50000)
)
```

---

## 🎯 Available Commands | សេវាកម្មលេខបញ្ជាដែលមាន

| Command | Description | ការពិពណ៌នា |
|---------|-------------|----------|
| `/start` | Start the bot | ចាប់ផ្តើម Bot |
| `/help` | Show help menu | បង្ហាញម៉ឺនុយគាំទ |
| `/share_location` | Share your location | ស្វាគមន៍ទីតាំង |
| `/scan_location` | Scan delivery location | ស្កេនលម្អិតលម្អឹងលក់ |
| `/track` | Track order status | តាមដានស្ថានភាពលម្អិតលម្អឹងលក់ |

---

## 🔐 Database Setup | ការរៀបចំមូលដ្ឋានទិន្នន័យ

The bot automatically initializes required tables on first run. Required tables:
- `customers` - ព័ត៌មាននៃអតិថិជន
- `orders` - លម្អិតលម្អឹងលក់
- `locations` - ទីតាំងដឹក
- `admin_users` - អ្នកគ្រប់គ្រង

---

## 📱 Telegram Bot Deployment | ការដាក់ដំណើរការលើ Render/Heroku

This bot is configured to run on cloud platforms like Render or Heroku with:
- Polling mode for receiving updates
- Health check endpoint at `/` 
- Automatic database synchronization

---

## 🤝 Contributing | ការរួមចំណែក

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---

## 📝 License | ライ센ス

This project is open source and available under the MIT License.

---

## 📞 Support | ជំនួយ

For issues, questions, or suggestions:
- Create an issue in the repository
- Contact the admin via Telegram
- Check the documentation

---

**Last Updated:** 2026-06-08  
**Version:** 1.0.0