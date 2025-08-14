import os

from telegram import Bot


def send_notification(message: str) -> None:
    """Send a notification message via Telegram bot."""
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    bot.send_message(chat_id=os.environ["CHAT_ID"], text=message)
