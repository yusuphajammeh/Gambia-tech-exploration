import os
import json
import datetime
import urllib.request
from dotenv import load_dotenv

# Import your professional logger
try:
    from YJ_Logger import log_event
except ImportError:
    # Fallback if logger is missing during transition
    def log_event(m, c): print(f"{c}: {m}")

# Load Token
load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')

def run_sync():
    try:
        # 1. Setup API Request
        user_url = "https://api.github.com/user"
        repo_url = "https://api.github.com/user/repos?type=owner"
        headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

        # 2. Fetch Profile Data
        req_user = urllib.request.Request(user_url, headers=headers)
        with urllib.request.urlopen(req_user) as response:
            user_res = json.loads(response.read().decode())

        # 3. Fetch Repo Data
        req_repos = urllib.request.Request(repo_url, headers=headers)
        with urllib.request.urlopen(req_repos) as response:
            repos_res = json.loads(response.read().decode())

        # 4. Handle Timestamps and Age
        timestamp = datetime.datetime.now().strftime("%b %d, %H:%M")
        current_year = datetime.datetime.now().year
        created_at = user_res.get('created_at', str(current_year))
        created_year = int(created_at[:4])
        years_ago = current_year - created_year
        age_display = "Joined this year" if years_ago == 0 else (f"{years_ago} Year Ago" if years_ago == 1 else f"{years_ago} Years Ago")

        # 5. Prepare stats
        stats = {
            "name": user_res.get('name', 'YUSUPHA JAMMEH'),
            "repos": len(repos_res),
            "followers": user_res.get('followers', 0),
            "created": age_display,
            "last_updated": timestamp
        }

        # 6. Save Files
        with open('data.json', 'w') as f:
            json.dump(stats, f)

        with open("heartbeat.txt", "w") as f:
            f.write(f"Robot Heartbeat Active: {timestamp}")

        # 7. Log Success
        log_event(f"Robot Sync: {len(repos_res)} repos tracked.", category="ROBOT")
        print(f"🚀 [SYNC SUCCESS] {timestamp}")

    except Exception as e:
        print(f"❌ [SYNC ERROR] {e}")

if __name__ == "__main__":
    run_sync()