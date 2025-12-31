import os
import requests
from dotenv import load_dotenv

# Use the logic that worked for your environment
load_dotenv()
token = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"Bearer {token}"}

def get_my_repos():
    # This endpoint gets all your public repositories
    url = "https://api.github.com/user/repos?type=owner&sort=updated"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repos = response.json()
        print(f"\n--- YUSUPHA'S REPOSITORY TRACKER ---")
        for repo in repos:
            name = repo['name']
            lang = repo['language'] if repo['language'] else "Text/Config"
            print(f"📁 {name.ljust(25)} | 💻 Language: {lang}")
    else:
        print(f"Error fetching repos: {response.status_code}")

if __name__ == "__main__":
    get_my_repos()