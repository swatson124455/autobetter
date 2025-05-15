import requests
from app.config import settings

GRAPHQL_URL = "https://api.polymarket.com/graphql"
QUERY_MARKETS = '''query { markets { id name probabilities { yes no } } }'''

async def fetch_markets():
    resp = requests.post(
        GRAPHQL_URL,
        json={'query': QUERY_MARKETS},
        headers={'Authorization': f"Bearer {settings.POLYMARKET_API_KEY}"},
        timeout=5
    )
    data = resp.json().get('data', {}).get('markets', [])
    return data
