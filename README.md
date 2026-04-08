# telegram-stil-bot

A Telegram bot that collects and sends image files (`.jpg`, `.png`) from common Android media directories via the Telegram Bot API.

## How It Works

The bot scans predefined directories on an Android device (Telegram, WhatsApp, Instagram, Camera, Screenshots, etc.) and sends all found images to a specified Telegram chat using the Bot API.

## Requirements

- Python 3
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/)

## Setup

1. Install the dependency:
   ```bash
   pip install pyTelegramBotAPI
   ```

2. Edit `main.py` and set your Telegram user ID and bot token:
   ```python
   ID = 'your_tg_id'
   bot = telebot.TeleBot("your_tg_bot_token")
   ```

3. Run the bot:
   ```bash
   python main.py
   ```

## Note

This project is for **educational and testing purposes only**.
