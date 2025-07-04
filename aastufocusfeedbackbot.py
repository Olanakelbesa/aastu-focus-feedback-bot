from telegram import Update, BotCommand
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
import asyncio
import os
from dotenv import load_dotenv
import telegram

# Load environment variables
load_dotenv()

# Get configuration from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
FEEDBACK_CHAT_ID = os.getenv('FEEDBACK_CHAT_ID')

if not BOT_TOKEN or not FEEDBACK_CHAT_ID:
    raise ValueError("Please set BOT_TOKEN and FEEDBACK_CHAT_ID environment variables")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 Welcome!\n\n"
        "Send your feedback anonymously here. "
        "Your identity will not be recorded.\n\n"
        "Use /help to see available commands."
    )
    await update.message.reply_text(welcome_text)

async def feedback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    feedback = update.message.text
    
    await context.bot.send_message(
        chat_id=FEEDBACK_CHAT_ID,
        text=f"📩 New anonymous feedback:\n\n{feedback}"
    )
    await context.bot.send_message(
        chat_id=1175717871,
        text=f"📩 New anonymous feedback:\n\n{feedback}"
    )
    await update.message.reply_text("✅ Thank you for your feedback!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "Available commands:\n"
        "/start - Start the bot\n"
        "/feedback - Send anonymous feedback\n"
        "/help - Show this help message"
    )
    await update.message.reply_text(help_text)

async def set_bot_commands(application):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("feedback", "Give feedback"),
        BotCommand("help", "Get help"),
    ]
    await application.bot.set_my_commands(commands)

if __name__ == '__main__':
    # Create the application with job_queue disabled
    app = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .job_queue(None)  # Disable job queue to avoid weak reference issues
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, feedback_handler))

    # Set up bot commands before starting
    app.post_init = set_bot_commands
    
    # Start the bot
    app.run_polling()
