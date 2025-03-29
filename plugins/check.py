from pyrogram import Client,filters
from heplers.convert import amazon_convert,convert_rest
import urllib.parse
from config import Telegram
@Client.on_message(filters.photo & filters.regex(r"https?://[^\s]+") & filters.chat(Telegram.CHANNELS))
async def check(client, message):
    completed_urls = []
    for match in message.matches:
        url = match.group(0)
        if "amzn.to" in url:
            aurl = amazon_convert(url)
            completed_urls.append((url, aurl))
        elif "youtu.be" in url or "t.me" in url or "youtube.com" in url:
            print("Youtube Spoted")
        else:
            response = convert_rest(url)
            if response.get("convertedText"):
                aurl = response["convertedText"]
                aurl = urllib.parse.unquote(aurl)
                completed_urls.append((url, aurl))
            else:
                await print("No Link Found")
    if completed_urls:
        caption = message.caption
        for url,aurl in completed_urls:
            caption = caption.replace(url, aurl)
        await client.send_photo(
            chat_id = Telegram.MAIN_CHAT_ID,
            photo=message.photo.file_id,
            caption=caption
        )
    else:
        print("No links found in the message.")