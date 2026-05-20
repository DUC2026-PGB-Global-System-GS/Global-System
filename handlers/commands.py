from telegram import Update
from telegram.ext import ContextTypes

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"សួស្តី {user_name}! ខ្ញុំជា Bot របស់ GS។ តើខ្ញុំអាចជួយអ្វីអ្នកបានខ្លះ?")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "💡 នេះជាបញ្ជី Command ដែលអ្នកអាចប្រើប្រាស់បាន៖\n\n"
        "/start - ចាប់ផ្តើមដំណើរការ Bot\n"
        "/help - មើលការណែនាំពីរបៀបប្រើ"
    )
    await update.message.reply_text(help_text)