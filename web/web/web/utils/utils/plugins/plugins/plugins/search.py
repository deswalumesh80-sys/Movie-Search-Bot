from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from utils.scraper import fetch_movies

@Client.on_message(filters.text & filters.private & ~filters.command(["start", "help"]))
async def search_handler(client: Client, message: Message):
    query = message.text.strip()
    status_msg = await message.reply_text(f"🔍 Searching & Scraping for **'{query}'**...")
    
    movie_results = await fetch_movies(query)
    
    if not movie_results:
        await status_msg.edit_text("❌ Koi movie link nahi mili. Kripya naam/spelling check karein.")
        return
        
    buttons = []
    for item in movie_results:
        buttons.append([InlineKeyboardButton(f"🎬 {item['title']}", url=item['url'])])
        
    await status_msg.edit_text(
        f"🍿 **Results Scraped for:** `{query}`\n\nDownload ya watch karne ke liye click karein:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
  
