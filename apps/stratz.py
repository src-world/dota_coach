import httpx
from config import STRATZ


API_KEY = STRATZ
URL = "https://api.stratz.com/graphql"

async def get_counters(hero_id: int):
    query = """
    {
      constants {
        hero(id: %d) {
          matchups {
            vs { heroId winRate advantage }
          }
        }
      }
    }
    """ % hero_id
    
    headers = {"Authorization": f"Bearer {API_KEY}"}
    async with httpx.AsyncClient() as client:
        r = await client.post(URL, json={'query': query}, headers=headers)
        return r.json()['data']['constants']['hero']['matchups']['vs']