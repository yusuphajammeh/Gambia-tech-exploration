import os
import requests
import json
import datetime
from dotenv import load_dotenv

# We import the logger here so the heartbeat can record its success
from YJ_Logger import log_event

# 1. Load your GitHub Token securely
load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {'Authorization': f'token {TOKEN}'}


def run_sync():
    try:
        # 2. Fetch your Profile Data
        user_res = requests.get("https://api.github.com/user", headers=HEADERS).json()

        # 3. Fetch your Repository Data
        repos_res = requests.get("https://api.github.com/user/repos?type=owner", headers=HEADERS).json()
        repo_count = len(repos_res)

        # 4. Handle Timestamps and Account Age
        timestamp = datetime.datetime.now().strftime("%b %d, %H:%M")
        current_year = datetime.datetime.now().year
        created_year = int(user_res.get('created_at', str(current_year))[:4])
        years_ago = current_year - created_year
        age_display = "Joined this year" if years_ago == 0 else (
            f"1 Year Ago" if years_ago == 1 else f"{years_ago} Years Ago")

        # 5. Prepare the data for your website
        stats = {
            "name": user_res.get('name', 'YUSUPHA JAMMEH'),
            "repos": repo_count,
            "followers": user_res.get('followers', 0),
            "created": age_display,
            "last_updated": timestamp
        }

        # 6. Update the files (Matches your YJ-Sync.yml requirements)
        # Update heartbeat.txt
        with open("heartbeat.txt", "w") as f:
            f.write(f"Robot Heartbeat Active: {timestamp}")

        # Update data.json
        with open('data.json', 'w') as f:
            json.dump(stats, f)

        # 7. Log the success professionally using the Logger
        log_event(f"Robot Sync: {repo_count} repos tracked. Portfolio updated.", category="ROBOT")
        print(f"🚀 [SYNC SUCCESS] {timestamp}")

    except Exception as e:
        print(f"❌ [SYNC ERROR] {e}")


if __name__ == "__main__":
    run_sync()