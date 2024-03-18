from telegram.ext import Updater, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Bot token from BotFather
TOKEN =

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! I will monitor your subscribers.')

def main():
    """Start the bot."""
    updater = Updater(token='your token', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    # Keep the program running
    updater.idle()

if __name__ == '__main__':
    main()
from telegram.ext import Updater, CommandHandler
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Bot token from BotFather
TOKEN = '6965122891:AAE0atzFBbmYpNQv1vodTUQX-06m_g-k-dk'

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello! I will monitor your subscribers.')

def main():
    """Start the bot."""
    updater = Updater(bot_token= '6965122891:AAE0atzFBbmYpNQv1vodTUQX-06m_g-k-dk', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    # Keep the program running
    updater.idle()

if __name__ == '__main__':
    main()
