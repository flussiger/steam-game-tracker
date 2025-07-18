// Fetch games from backend and show them in a list
console.log("Starting to fetch games...");
fetch("http://localhost:8000/api/games")
  .then(response => {
    console.log("Response status:", response.status);
    console.log("Response headers:", response.headers);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  })
  .then(games => {
    console.log("Games received:", games);
    console.log("Games type:", typeof games);
    console.log("Games length:", games ? games.length : "undefined");
    
    const list = document.getElementById("game-list");
    list.innerHTML = ""; // Clear loading text

    if (!games || !Array.isArray(games) || games.length === 0) {
      list.textContent = `Keine Spiele gefunden. Received: ${JSON.stringify(games)}`;
      return;
    }

    console.log("Processing", games.length, "games");
    
    // Sort games by playtime (most to least played)
    const sortedGames = games.sort((a, b) => b.playtime_forever - a.playtime_forever);
    
    sortedGames.forEach((game, index) => {
      console.log(`Game ${index}:`, game);
      const li = document.createElement("li");
      // Playtime is in minutes, convert to hours rounded
      const hours = Math.round(game.playtime_forever / 60);
      li.textContent = `${game.name} — ${hours} Stunden gespielt`;
      list.appendChild(li);
    });
    console.log("Finished processing games");
  })
  .catch(err => {
    console.error("Fetch error:", err);
    const list = document.getElementById("game-list");
    list.textContent = "Fehler beim Laden der Spiele: " + err.message;
  });
