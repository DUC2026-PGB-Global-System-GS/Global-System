import sqlite3
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

# ========================================================
# 1. បង្កើត និងរៀបចំ DATABASE (DATABASE SETUP)
# ========================================================
def init_db():
    conn = sqlite3.connect("delivery_bot.db")
    cursor = conn.cursor()
    
    # បង្កើត Table សម្រាប់រក្សាទិន្នន័យអតិថិជន
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            phone TEXT DEFAULT NULL,
            registered_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # បង្កើត Table សម្រាប់កត់ត្រាការដឹកជញ្ជូន (ប្រវត្តិផ្ញើអីវ៉ាន់)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            item_name TEXT,
            status TEXT DEFAULT 'កំពុងរៀបចំ',
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        )
    """)
    conn.commit()
    conn.close()

# ដំណើរការបង្កើត Table ភ្លាមៗនៅពេលបើកកូដ
init_db()


# ========================================================
# 2. មុខងារ COMMAND /START (ឆែកមើល OLD / NEW USER)
# ========================================================
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    first_name = user.first_name
    username = user.username if user.username else "No_Username"

    # ភ្ជាប់ទៅកាន់ Database ដើម្បីពិនិត្យមើល ID
    conn = sqlite3.connect("delivery_bot.db")
    cursor = conn.cursor()
    cursor.execute("SELECT phone FROM users WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()

    if user_data is None:
        # ----------------------------------------------------
        # ករណីទី ១៖ រកមិនឃើញ ID = USER NEW
        # ----------------------------------------------------
        cursor.execute(
            "INSERT INTO users (user_id, username, first_name) VALUES (?, ?, ?)",
            (user_id, username, first_name)
        )
        conn.commit()
        
        welcome_text = (
            f"👋 សួស្តីសមាជិកថ្មី លោក/អ្នក {first_name}! មកកាន់ប្រព័ន្ធដឹកជញ្ជូន GS។\n\n"
            "ដើម្បីភាពងាយស្រួលក្នុងការដឹកជញ្ជូន និងទាក់ទង សូមចុចចុះឈ្មោះលេខទូរសព្ទរបស់អ្នកជាមុនសិនបាទ។"
        )
        # បង្កើតប៊ូតុងឱ្យគាត់ចុចផ្ញើលេខទូរសព្ទអូតូ (Contact Button)
        keyboard = [[{"text": "📱 ចុចផ្ញើលេខទូរសព្ទដើម្បីចុះឈ្មោះ", "request_contact": True}]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
        
        await update.message.reply_text(welcome_text, reply_markup=reply_markup)

    else:
        # ----------------------------------------------------
        # ករណីទី ២៖ រកឃើញ ID = USER OLD
        # ----------------------------------------------------
        phone_number = user_data[0]
        
        # ទាញយកប្រវត្តិដឹកជញ្ជូនចុងក្រោយរបស់គាត់ (បើមាន)
        cursor.execute("SELECT item_name, status FROM orders WHERE user_id = ? ORDER BY order_id DESC LIMIT 1", (user_id,))
        last_order = cursor.fetchone()
        
        history_text = ""
        if last_order:
            history_text = f"📦 អីវ៉ាន់ចុងក្រោយ៖ {last_order[0]} ({last_order[1]})"
        else:
            history_text = "📦 ប្រវត្តិ៖ មិនទាន់មានការផ្ញើអីវ៉ាន់នៅឡើយទេ"

        welcome_text = (
            f"🎉 រីករាយដែលបានជួបអ្នកម្តងទៀត លោក/អ្នក {first_name} (អតិថិជនចាស់)!\n"
            f"📞 លេខទូរសព្ទ៖ {phone_number if phone_number else 'មិនទាន់ចុះឈ្មោះ'}\n"
            f"-------------------------------\n"
            f"{history_text}\n\n"
            "👉 សូមជ្រើសរើសសេវាកម្ម៖\n"
            "📝 /new_order - បង្កើតការផ្ញើអីវ៉ាន់ថ្មី\n"
            "🔍 /track - តាមដានស្ថានភាពអីវ៉ាន់"
        )
        await update.message.reply_text(welcome_text)

    conn.close()


# ========================================================
# 3. មុខងារ COMMAND /HELP
# ========================================================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "💡 ការណែនាំអំពីបញ្ជា (Commands)៖\n\n"
        "/start - ពិនិត្យមើលគណនី និងប្រវត្តិផ្ញើ\n"
        "/help - មើលការណែនាំឡើងវិញ"
    )
    await update.message.reply_text(help_text)