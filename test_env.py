import os
from dotenv import load_dotenv

# This finds the exact folder where THIS script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(script_dir, '.env')

# Load the file from that exact path
load_dotenv(dotenv_path=env_path)

token = os.getenv("GITHUB_TOKEN")
if token:
    print(f"✅ SUCCESS! Token found: {token[:4]}...")
else:
    print(f"❌ STILL FALSE. Looking in: {env_path}")