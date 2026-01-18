from config import STRATZ
import stratz as st
import aiohttp

async def fetch_match_data(player_id):
    url = f"https://api.opendota.com/api/players/{player_id}/recentMatches"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None