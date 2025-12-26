import requests
import os
from dotenv import load_dotenv
from YJ_Logger import log_event # Using your professional logger!

load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')
headers = {'Authorization': f'token {TOKEN}'}

def fetch_advanced_stats():
    url = "https://api.github.com/user"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extracting the specific stats for your new HTML cards
        stats = {
            "name": data.get('name', 'User'),
            "repos": data.get('public_repos', 0),
            "followers": data.get('followers', 0),
            "created": data.get('created_at', '')[:10] # Gets just the YYYY-MM-DD
        }
        
        print(f"📊 Stats Fetched for {stats['name']}:")
        print(f" - Repos: {stats['repos']}")
        print(f" - Followers: {stats['followers']}")
        print(f" - Member Since: {stats['created']}")
        
        # Log the success automatically
        log_event(f"Fetched Advanced Stats: {stats['repos']} repos, {stats['followers']} followers.")
        return stats
    else:
        log_event(f"Error fetching stats: {response.status_code}")
        return None

if __name__ == "__main__":
    fetch_advanced_stats()