import os
import json
from datetime import datetime
from telethon import TelegramClient, errors
from dotenv import load_dotenv
from loguru import logger
import asyncio
import time

load_dotenv()

API_ID = os.getenv('TELEGRAM_API_ID')
API_HASH = os.getenv('TELEGRAM_API_HASH')
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

DATA_DIR = os.path.join(os.path.dirname(__file__), '../../data/raw/telegram_messages')
LOG_FILE = os.path.join(os.path.dirname(__file__), '../../data/scrape.log')
CHANNELS_CONFIG = os.path.join(os.path.dirname(__file__), 'channels.json')

logger.add(LOG_FILE, rotation="1 MB")

RETRY_LIMIT = 3
RETRY_DELAY = 10  # seconds


def load_channels():
    if os.path.exists(CHANNELS_CONFIG):
        with open(CHANNELS_CONFIG, 'r') as f:
            return json.load(f)
    # Default channels if config not found
    return ["lobelia4cosmetics", "tikvahpharma"]

async def scrape_channel(client, channel_username, limit=100):
    messages = []
    try:
        async for message in client.iter_messages(channel_username, limit=limit):
            messages.append(message.to_dict())
        logger.info(f"Scraped {len(messages)} messages from {channel_username}")
    except errors.FloodWaitError as e:
        logger.warning(f"Rate limited by Telegram API. Waiting {e.seconds} seconds.")
        time.sleep(e.seconds)
        return await scrape_channel(client, channel_username, limit)
    except Exception as e:
        logger.error(f"Error scraping {channel_username}: {e}")
        return []
    return messages

def save_messages(channel_username, messages):
    date_str = datetime.now().strftime('%Y-%m-%d')
    channel_dir = os.path.join(DATA_DIR, date_str)
    os.makedirs(channel_dir, exist_ok=True)
    out_path = os.path.join(channel_dir, f'{channel_username}.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)
    logger.info(f"Saved messages to {out_path}")

async def scrape_all_channels(limit=100):
    channels = load_channels()
    async with TelegramClient('anon', API_ID, API_HASH) as client:
        for channel in channels:
            for attempt in range(RETRY_LIMIT):
                try:
                    messages = await scrape_channel(client, channel, limit)
                    save_messages(channel, messages)
                    break
                except Exception as e:
                    logger.error(f"Attempt {attempt+1} failed for {channel}: {e}")
                    if attempt < RETRY_LIMIT - 1:
                        time.sleep(RETRY_DELAY)
                    else:
                        logger.error(f"Failed to scrape {channel} after {RETRY_LIMIT} attempts.")

if __name__ == '__main__':
    asyncio.run(scrape_all_channels(limit=100)) 