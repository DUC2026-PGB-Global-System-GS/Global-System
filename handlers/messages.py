from telegram import Update
from telegram.ext import ContextTypes

async def handle_normal_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_received = update.message.text.lower()
    
    # លក្ខខណ្ឌឆ្លើយតបងាយៗ
    if "សួស្តី" in text_received or "hello" in text_received or "hi" in text_received:
        await update.message.reply_text("សួស្តីបាទ! សប្បាយណាស់ដែលបានជជែកជាមួយអ្នក។ 😊")
    elif "អរគុណ" in text_received or "thanks" in text_received:
        await update.message.reply_text("រីករាយបាទ! គ្មានបញ្ហាទេ។ 🤝")
    else:
        await update.message.reply_text(f"ខ្ញុំបានទទួលសាររបស់អ្នកហើយ៖ \"{update.message.text}\" ប៉ុន្តែខ្ញុំមិនទាន់យល់ពីអត្ថន័យនៅឡើយទេ។")