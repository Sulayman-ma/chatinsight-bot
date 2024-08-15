import os
import logging
from telegram import Update
from telegram.error import TelegramError
from telegram.ext import (
    ContextTypes, 
    CommandHandler,
    ApplicationBuilder
)



logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def greeting(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi, I'm the bot from ChatInsight, nice to meet you!"
    )


if __name__ == "__main__":
    # Application object (the bot itself)
    application = ApplicationBuilder().token(
        os.getenv(
            "API_KEY", 
            "7288371310:AAHPhYtm0tHfVLoILkQu6yRBGW6D4uVEbdc"
        )
    ).build()

    # Create command handlers with the commands and callback functions
    greeting_handler = CommandHandler("hello", greeting)

    # Register the handlers
    application.add_handler(greeting_handler)

    # Start the bot until CTRL+C is hit
    application.run_polling()
