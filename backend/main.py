from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from steam_api import get_steam_games

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/games")
def api_get_games():
    games = get_steam_games()
    return games

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)