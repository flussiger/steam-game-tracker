# Steam Game Tracker

A simple web application to display your Steam games with playtime information.

## Setup

1. **Get your Steam API Key:**
   - Go to https://steamcommunity.com/dev/apikey
   - Register for a Steam Web API key

2. **Get your Steam ID:**
   - Go to your Steam profile
   - Look at the URL - the number after `/profiles/` is your Steam ID
   - Or use https://steamid.io/ to convert your Steam username

3. **Configure the application:**
   ```bash
   cd backend
   cp config.example.py config.py
   ```
   Then edit `config.py` and add your actual API key and Steam ID.

4. **Run the application:**
   ```bash
   cd backend
   python main.py
   ```

5. **Open in browser:**
   
   **Recommended way:**
   - Keep the backend running (step 4)
   - Navigate to the `frontend` folder in File Explorer
   - Double-click `index.html` to open it in your browser
   - The page will automatically call the backend to load your games
   
   **Alternative (raw data only):**
   - Go to http://localhost:8000/api/games to see raw game data
   - Go to http://localhost:8000/api/player to see raw player data

## Important
Never commit your `config.py` file with real API keys to Git!