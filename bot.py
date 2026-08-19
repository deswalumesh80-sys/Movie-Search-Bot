import asyncio
from pyrogram import Client
import config
from web.server import web_server
from aiohttp import web

plugins = dict(root="plugins")

app = Client(
    "movie_finder_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=plugins
)

async def main():
    await app.start()
    print("Bot is successfully started with Scraper & Web Server!")
    
    # Render Keep-Alive Web Server
    app_runner = web.AppRunner(await web_server())
    await app_runner.setup()
    site = web.TCPSite(app_runner, "0.0.0.0", config.PORT)
    await site.start()
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
  
