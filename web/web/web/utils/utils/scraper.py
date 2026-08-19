import urllib.parse
import aiohttp
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

async def fetch_movies(query: str):
    results = []
    encoded_query = urllib.parse.quote_plus(query)
    search_url = f"https://moviesmod.day/?s={encoded_query}"
    
    try:
        async with aiohttp.ClientSession(headers=HEADERS) as session:
            async with session.get(search_url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
                if resp.status == 200:
                    html = await resp.text()
                    soup = BeautifulSoup(html, "html.parser")
                    
                    articles = soup.find_all("article", limit=8)
                    for article in articles:
                        title_tag = article.find("h2") or article.find("h3") or article.find("a")
                        link_tag = article.find("a", href=True)
                        
                        if title_tag and link_tag:
                            title = title_tag.get_text(strip=True)[:40]
                            link = link_tag["href"]
                            results.append({"title": title, "url": link})
    except Exception as e:
        print(f"Scraping Error: {e}")
        
    return results
  
