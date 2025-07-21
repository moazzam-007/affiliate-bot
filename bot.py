from flask import Flask
import threading
import os
import time
from pyrogram import Client
from config import Telegram

# --- Flask Web Server ka Setup ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Affiliate Bot is alive and running!"

# --- Aapke Pyrogram Bot ka Asli Code ---

def run_pyrogram_bot():
    print("Pyrogram Bot ka process shuru ho raha hai...")
    
    # Aapka bot client ka code
    client = Client(
        ":memory:",
        api_id=Telegram.API_ID,
        api_hash=Telegram.API_HASH,
        session_string=Telegram.STRING_SESSION,
        plugins=dict(root="plugins"),
        workers=20,
        in_memory=True
    )

    print("Pyrogram client chal raha hai...")
    client.run()


# --- Server aur Bot ko Shuru Karne ka Code ---

if __name__ == "__main__":
    # Bot ko ek alag, background thread mein chalu karein
    bot_thread = threading.Thread(target=run_pyrogram_bot)
    bot_thread.start()
    
    # Aur Flask web server ko main thread mein chalu karein
    print("Flask web server shuru ho raha hai...")
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
