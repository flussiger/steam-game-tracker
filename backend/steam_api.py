import requests
from config import STEAM_API_KEY, STEAM_ID

def get_steam_games(): 
    url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
    params = {
        "key": STEAM_API_KEY,
        "steamid": STEAM_ID,
        "format": "json",
        "include_appinfo": "true",
        "include_played_free_games": "true"
    }

    try:
        response = requests.get(url, params=params)        
        if response.status_code == 200:
            data = response.json()            
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


def get_player_info(): 
    url = f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params = {
        "key": STEAM_API_KEY,
        "steamids": STEAM_ID,
        "format": "json",
    }

    try:
        response2 = requests.get(url, params=params)        
        if response2.status_code == 200:
            data2 = response2.json()            
            if "response" in data2 and "players" in data2["response"]:
                return data2["response"]["players"]
            else:
                print("No player found in response")
                return []
        else:
            print(f"Error: HTTP {response2.status_code}")
            return []
            
    except Exception as e:
        print(f"Exception occurred: {e}")
        return []
