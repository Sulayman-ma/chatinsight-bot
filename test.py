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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi, I'm the bot from Fiverr, nice to meet you!"
    )

async def send_scheduled_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
       await context.bot.send_message(
           chat_id=update.effective_chat.id,
            text="This is a scheduled post!"
       )
       print("Scheduled message sent successfully.")

    except TelegramError as e:
        print(f"Error occured: {e}")


if __name__ == "__main__":
    # Application object (the bot itself)
    application = ApplicationBuilder().token("7288371310:AAHPhYtm0tHfVLoILkQu6yRBGW6D4uVEbdc").build()

    # Create command handlers with the commands and callback functions
    start_handler = CommandHandler("start", start)

    # Register the handlers
    application.add_handler(start_handler)

    # Start the bot until CTRL+C is hit
    application.run_polling()
