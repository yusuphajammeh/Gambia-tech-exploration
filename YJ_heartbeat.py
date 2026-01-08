import os
import json
import datetime
import urllib.request

# 1. LOCAL TOKEN CHECK: Manual read of .env to avoid 'dotenv' dependency
if os.path.exists('.env'):
    with open('.env', 'r') as f:
        for line in f:
            if line.startswith('GITHUB_TOKEN='):
                os.environ['GITHUB_TOKEN'] = line.split('=')[1].strip()

TOKEN = os.getenv('GITHUB_TOKEN')


def log_to_file(message, category="ROBOT"):
    log_file = "AI--Log.txt"
    date_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\n 🔷 ENTRY_POINT >> {date_str}\n")
            f.write(f" ┗━━ {category}: {message}\n")
            f.write(f" {'─' * 60}\n")
    except:
        pass


def run_sync():
    try:
        # 2. Setup API Requests
        user_url = "https://api.github.com/user"
        repo_url = "https://api.github.com/user/repos?type=owner"

        # Adding User-Agent is required by GitHub API
        headers = {
            "Authorization": f"token {TOKEN}",
            "User-Agent": "Y-J-Portfolio-Robot"
        }

        # Fetch Data
        req_user = urllib.request.Request(user_url, headers=headers)
        with urllib.request.urlopen(req_user) as response:
            user_res = json.loads(response.read().decode())

        req_repos = urllib.request.Request(repo_url, headers=headers)
        with urllib.request.urlopen(req_repos) as response:
            repos_res = json.loads(response.read().decode())

        # 3. Process Stats
        timestamp = datetime.datetime.now().strftime("%b %d, %H:%M")
        repo_count = len(repos_res)

        # Account Age logic
        current_year = datetime.datetime.now().year
        created_at = user_res.get('created_at', str(current_year))
        created_year = int(created_at[:4])
        years_ago = current_year - created_year
        age_display = "Joined this year" if years_ago == 0 else (
            f"{years_ago} Year Ago" if years_ago == 1 else f"{years_ago} Years Ago")

        stats = {
            "name": user_res.get('name', 'YUSUPHA JAMMEH'),
            "repos": repo_count,
            "followers": user_res.get('followers', 0),
            "created": age_display,
            "last_updated": timestamp
        }

        # 4. Save Results
        with open('data.json', 'w') as f:
            json.dump(stats, f)

        with open("heartbeat.txt", "w") as f:
            f.write(f"Robot Heartbeat Active: {timestamp}")

        log_to_file(f"Robot Sync: {repo_count} repos tracked. Status: Online.")
        print(f"🚀 [SUCCESS] Sync completed at {timestamp}")

    except Exception as e:
        # This will now tell you exactly what went wrong
        print(f"❌ [SYNC ERROR] {e}")


if __name__ == "__main__":
    run_sync()