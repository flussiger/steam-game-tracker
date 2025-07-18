import requests
from config import STEAM_API_KEY, STEAM_ID

def get_steam_games():
    print(f"Using API Key: {STEAM_API_KEY}")
    print(f"Using Steam ID: {STEAM_ID}")
    
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": STEAM_API_KEY,
        "steamid": STEAM_ID,
        "format": "json",
        "include_appinfo": "true",
        "include_played_free_games": "true"
    }

    print(f"Making request to: {url}")
    print(f"With params: {params}")

    try:
        response = requests.get(url, params=params)
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text[:500]}...")  # First 500 chars
        
        if response.status_code == 200:
            data = response.json()
            print(f"JSON response: {data}")
            
            if "response" in data and "games" in data["response"]:
                return data["response"]["games"]
            else:
                print("No games found in response")
                return []
        else:
            print(f"Error: HTTP {response.status_code}")
            return []
            
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []
