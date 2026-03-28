import requests
import os
from datetime import datetime, timedelta

WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK')

def check_dodgers():
    # Looks at yesterday's games
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    url = f"https://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate={yesterday}&endDate={yesterday}"
    
    data = requests.get(url).json()
    
    for date in data.get("dates", []):
        for game in date.get("games", []):
            # 119 is the Dodgers ID
            home_team = game["teams"]["home"]
            if home_team["team"]["id"] == 119 and home_team.get("isWinner"):
                requests.post(WEBHOOK_URL, json={"content": "⚾ **DODGERS HOME WIN!** 🐼\nGet your $7 Panda Plate today with code: `DODGERSWIN` @everyone"})

if __name__ == "__main__":
    check_dodgers()
