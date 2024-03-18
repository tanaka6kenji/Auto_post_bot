# Auto_post_bot
Setting Up the Bot:

Create a Telegram Bot: Use BotFather to create a new bot and get the token.

Install Required Libraries: Ensure you have python-telegram-bot installed.

Write the Bot Code: Replace "YOUR_BOT_TOKEN" with your actual bot token in the code below.

Run the Bot: Start your bot code in a Python environment.

Using the Bot:

Start the Bot: Chat with your bot on Telegram.

Set Auto-Posting: Use /set <message> to set a message for auto-posting every 24 hours.

Unset Auto-Posting: Use /unset to stop auto-posting.

Code Explanation:

The bot uses python-telegram-bot to interact with the Telegram API.
post_message sends the scheduled message to the chat ID.
set_timer extracts the message and schedules a job to post it every 24 hours.
unset stops the auto-posting job if active.
start sends a welcome message on /start.
main sets up and runs the bot.
Complete Bot Code:
