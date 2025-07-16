import os
import json
from datetime import datetime
from telethon import TelegramClient
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/raw/telegram_messages')

async def scrape_channel(channel_username, limit=100):
    async with TelegramClient('anon', API_ID, API_HASH) as client:
        messages = []
        async for message in client.iter_messages(channel_username, limit=limit):
            messages.append(message.to_dict())
        # Save to JSON
        date_str = datetime.now().strftime('%Y-%m-%d')
        channel_dir = os.path.join(DATA_DIR, date_str)
        os.makedirs(channel_dir, exist_ok=True)
        with open(os.path.join(channel_dir, f'{channel_username}.json'), 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    import asyncio
    # Example usage
    asyncio.run(scrape_channel('lobelia4cosmetics', limit=100)) 