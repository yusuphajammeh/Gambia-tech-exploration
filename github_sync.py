import os, requests, json, time, datetime
from dotenv import load_dotenv
from YJ_Engine import log_event

load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')
HEADERS = {'Authorization': f'token {TOKEN}'}

def sync_all():
    try:
        # 1. Fetch Stats & Calculate Age (from your github_profile logic)
        user_res = requests.get("https://api.github.com/user", headers=HEADERS).json()
        current_year = datetime.datetime.now().year
        created_year = int(user_res.get('created_at', str(current_year))[:4])
        years_ago = current_year - created_year
        age_display = "Joined this year" if years_ago == 0 else (f"1 Year Ago" if years_ago == 1 else f"{years_ago} Years Ago")

        # 2. Track Repos (from your repo_tracker logic)
        repos = requests.get("https://api.github.com/user/repos?type=owner&sort=updated", headers=HEADERS).json()
        repo_count = len(repos)

        # 3. Update Website Data (data.json)
        timestamp = datetime.datetime.now().strftime("%b %d, %H:%M")
        website_stats = {
            "name": user_res.get('name', 'YUSUPHA'),
            "repos": repo_count,
            "followers": user_res.get('followers', 0),
            "created": age_display,
            "last_updated": timestamp
        }

        # Save to root and website folder if it exists
        paths = ['data.json', 'Y-J_website/data.json']
        for path in paths:
            if os.path.exists(os.path.dirname(path)) or '/' not in path:
                with open(path, 'w') as f: json.dump(website_stats, f)

        # 4. Heartbeat Pulse
        with open("heartbeat.txt", "w") as f:
            f.write(f"Robot Heartbeat Active: {timestamp}")

        log_event(f"System Sync Complete: {repo_count} Repos found. Portfolio updated.", category="ROBOT")
        print(f"🚀 [SYNC SUCCESS] {timestamp}")

    except Exception as e:
        log_event(f"Sync Failure: {str(e)}", category="ERROR")
        print(f"❌ [SYNC ERROR] {e}")

if __name__ == "__main__":
    # Run once immediately
    sync_all()
    # Then wait 1 hour and repeat
    print("🤖 Robot is standing by... (Syncing every 60 mins)")
    while True:
        time.sleep(3600)
        sync_all()