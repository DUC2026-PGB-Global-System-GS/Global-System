from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config.settings import BOT_TOKEN
from handlers.commands import start_command, help_command
from handlers.messages import handle_normal_message

def main():
    # បង្កើត Application ដោយប្រើ Token ចេញពី config/settings.py
    app = Application.builder().token(BOT_TOKEN).build()

    # 1. ដាក់បញ្ចូល Command Handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # 2. ដាក់បញ្ចូល Message Handlers (សម្រាប់ចាប់ Text messages ធម្មតា តែមិនមែនជា Commands ទេ)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_normal_message))

    # ចាប់ផ្តើមដំណើរការ Bot
    print("🤖 Bot របស់ GS កំពុងដំណើរការហើយ... (ចុច Ctrl+C ដើម្បីបិទ)")
    app.run_polling()

if __name__ == "__main__":
    main()