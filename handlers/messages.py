import sqlite3
from telegram import Update
from telegram.ext import ContextTypes

async def handle_normal_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ឆែកមើលថាតើសារនោះជា លេខទូរសព្ទ (Contact) មែនឬទេ
    if update.message.contact:
        user_id = update.message.contact.user_id
        phone_number = update.message.contact.phone_number
        
        # យកលេខទូរសព្ទទៅ Update ចូល Database
        conn = sqlite3.connect("delivery_bot.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET phone = ? WHERE user_id = ?", (phone_number, user_id))
        conn.commit()
        conn.close()
        
        await update.message.reply_text(
            f"✅ ជោគជ័យ! ប្រព័ន្ធបានកត់ត្រាលេខទូរសព្ទ `{phone_number}` របស់អ្នករួចរាល់ហើយ។\n"
            "សូមចុច `/start` ម្តងទៀតដើម្បីចូលទៅកាន់ Menu ធំ។"
        )
        return

    # សារជាអក្សរធម្មតា
    text_received = update.message.text.lower()
    if "សួស្តី" in text_received or "hello" in text_received:
        await update.message.reply_text("សួស្តីបាទ! មានអ្វីឱ្យខ្ញុំជួយដែរទេ? 😊")
    else:
        await update.message.reply_text("សូមប្រើប្រាស់ Commands ផ្សេងៗដែលមានក្នុង Menu បាទ។")