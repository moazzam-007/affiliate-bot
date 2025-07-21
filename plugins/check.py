from pyrogram import Client, filters
from heplers.convert import amazon_convert, convert_rest
import urllib.parse
from config import Telegram

# Dono tarah ke messages par trigger hoga (Photo ya Text)
@Client.on_message(
    (filters.photo | filters.text) &
    filters.regex(r"https?://[^\s]+") &
    filters.chat(Telegram.CHANNELS)
)
async def check(client, message):
    completed_urls = []
    
    # Message ka content lene ka sahi tareeka (chahe photo ho ya text)
    text_content = message.caption if message.photo else message.text
    if not text_content:
        return # Agar text ya caption nahi hai to kuch na kare

    # Baaki ka logic lagbhag same hai
    for match in message.matches:
        url = match.group(0)
        if "amzn.to" in url:
            aurl = amazon_convert(url)
            completed_urls.append((url, aurl))
        elif "googleusercontent.com" in url or "t.me" in url:
            # Is link ko ignore ya log kar sakte hain
            continue
        else:
            response = convert_rest(url)
            if response.get("convertedText"):
                aurl = urllib.parse.unquote(response["convertedText"])
                completed_urls.append((url, aurl))
            else:
                # Agar link convert na ho to log karein
                if Telegram.LOG_GROUP_ID:
                    await client.send_message(
                        chat_id=Telegram.LOG_GROUP_ID,
                        text=f"Unsupported link: {url}\nResponse: {response}"
                    )

    if not completed_urls:
        return # Agar koi link convert nahi hua to kuch na kare

    # Naye converted links ke saath text ko update karein
    for original_url, new_url in completed_urls:
        text_content = text_content.replace(original_url, new_url)

    # Message ko apne channel par bhejein
    if message.photo:
        await client.send_photo(
            chat_id=Telegram.MAIN_CHAT_ID,
            photo=message.photo.file_id,
            caption=text_content
        )
    else:
        await client.send_message(
            chat_id=Telegram.MAIN_CHAT_ID,
            text=text_content
        )
