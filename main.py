from telethon.sync import TelegramClient, events
import os
import requests

# Load environment variables from Railway
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")
chat_id = os.environ.get("CHAT_ID")

# Keywords and channel to monitor
keywords = ['AGE: 0.00d', 'AGE: 0.01d']
canal = '@ethprotrending'

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=canal))
async def handler(event):
    message = event.message.message
    if any(keyword.lower() in message.lower() for keyword in keywords):
        print(f"🔔 Match found: {message}")
        alert_msg = f"🚨 ALERT: '{message}' in {canal}"
        requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={
            "chat_id": chat_id,
            "text": alert_msg
        })

client.start()
client.run_until_disconnected()
