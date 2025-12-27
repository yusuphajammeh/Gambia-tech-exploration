import requests
import time
import os
import datetime # 1. Make sure this is at the VERY top of the file
import json # Add this at the top of your file
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
        
        # Combined into one clean dictionary
        # Get the current year
        current_year = datetime.datetime.now().year
        # Get the year the account was created (first 4 characters of '2024-09-22')
        created_year = int(data.get('created_at', str(current_year))[:4])
        
        # Calculate the difference
        years_ago = current_year - created_year
        
        # Create a friendly string (e.g., "1 Year Ago" or "Joined this year")
        if years_ago == 0:
            age_display = "Joined this year"
        elif years_ago == 1:
            age_display = "1 Year Ago"
        else:
            age_display = f"{years_ago} Years Ago"

        stats = {
            "name": data.get('name', 'User'),
            "repos": data.get('public_repos', 0),
            "followers": data.get('followers', 0),
            "created": age_display, # Now sends "1 Year Ago" instead of a date
            "last_updated": datetime.datetime.now().strftime("%b %d, %H:%M")
        }

        print(f"📊 Stats Fetched for {stats['name']}:")
        print(f" - Repos: {stats['repos']}")
        print(f" - Followers: {stats['followers']}")
        print(f" - Member Since: {stats['created']}")
        
        log_event(f"Fetched Advanced Stats: {stats['repos']} repos, {stats['followers']} followers.")
        return stats
    else:
        log_event(f"Error fetching stats: {response.status_code}")
        return None

if __name__ == "__main__":
    print("🚀 GitHub Bridge is now active and monitoring...")
    
    while True:
        stats = fetch_advanced_stats()
        if stats:
            # Save the data to the JSON file
            with open('Y-J_website/data.json', 'w') as f:
                json.dump(stats, f)
            
            print(f"✅ Sync Complete at {stats['last_updated']}. Sleeping for 1 hour...")
        
        # This tells the script to wait 3600 seconds (1 hour) before running again
        time.sleep(3600)
