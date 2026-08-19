from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_handler(client: Client, message: Message):
    user_name = message.from_user.first_name if message.from_user else "User"
    await message.reply_text(
        f"Namaste {user_name}! 🎬\n\n"
        "Main **Live Web Scraper Movie Bot** hoon.\n\n"
        "Mujhe kisi bhi Movie ya Series ka naam bhejein, main direct web servers se scrape karke download links dunga."
    )
  
