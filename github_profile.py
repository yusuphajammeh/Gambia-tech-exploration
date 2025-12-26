import requests
import os
from dotenv import load_dotenv

# Load your secret token from the .env file
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github+json"
}

def get_github_profile():
    url = "https://api.github.com/user"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Successfully connected as: {data['name']}")
        print(f"School/Company: {data['company']}")
        
        # Save this to your AI Log for context
        with open("AI--Log.txt", "a") as log:
            log.write(f"\n[API Sync] Verified Profile: {data['name']} at {data['company']} on 2025-12-25\n")
    else:
        print(f"Failed! Error code: {response.status_code}")

if __name__ == "__main__":
    get_github_profile()