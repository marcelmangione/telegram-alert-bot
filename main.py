from telethon.sync import TelegramClient, events
from telethon.sessions import StringSession
import os
import requests

# Palavras-chave e canal alvo
keywords = ['AGE: 0.00d', 'AGE: 0.01d']
canal = '@ethprotrending'

if __name__ == "__main__":
    # Força leitura das variáveis no momento da execução
    api_id = int(os.environ.get("API_ID", "0"))
    api_hash = str(os.environ.get("API_HASH", ""))
    string_session = os.environ.get("STRING_SESSION", "")
    bot_token = os.environ.get("BOT_TOKEN", "")
    chat_id = os.environ.get("CHAT_ID", "")

    print("DEBUG:", api_id, api_hash)  # Pode remover depois

    client = TelegramClient(StringSession(string_session), api_id, api_hash)

    @client.on(events.NewMessage(chats=canal))
    async def handler(event):
        message = event.message.message
        if any(keyword.lower() in message.lower() for keyword in keywords):
            alert_msg = f"🚨 ALERT: '{message}' in {canal}"
            requests.post(f"https://api.telegram.org/bot{bot_token}/sendMessage", data={
                "chat_id": chat_id,
                "text": alert_msg
            })

    client.start()
    client.run_until_disconnected()

