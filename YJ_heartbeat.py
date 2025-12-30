import json
import datetime


def update_public_files():
    timestamp = datetime.datetime.now().strftime("%b %d, %H:%M")

    # 1. Update heartbeat.txt
    with open("heartbeat.txt", "w") as f:
        f.write(f"Robot Heartbeat Active: {timestamp}")

    # 2. Update data.json for your Website
    try:
        with open("data.json", "r") as f:
            data = json.load(f)

        data["last_updated"] = timestamp

        with open("data.json", "w") as f:
            json.dump(data, f)
        print("✔️ data.json updated for the website.")
    except Exception as e:
        print(f"Error updating data.json: {e}")


if __name__ == "__main__":
    update_public_files()