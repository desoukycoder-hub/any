import json, urllib.request, os, sys, base64

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE, "config.json"), "r", encoding="utf-8") as f:
    TOKEN = json.load(f)["bot_token"]

API = "https://discord.com/api/v10"
GUILD = "1538530169583575101"
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json", "User-Agent": "Bot/1.0"}

icons = [
    ("falcon.png", "Falcon"),
    ("diamond.png", "Diamond"),
    ("falcon_moon.png", "Falcon Moon"),
]

# Upload falcon first
path = os.path.join(r"C:\Users\Wael Desouky\Downloads\kick", icons[0][0])
with open(path, "rb") as f:
    icon_data = base64.b64encode(f.read()).decode()
icon_b64 = f"data:image/png;base64,{icon_data}"

body = {"icon": icon_b64}
data = json.dumps(body).encode("utf-8")
req = urllib.request.Request(f"{API}/guilds/{GUILD}", data=data, method="PATCH", headers=headers)
try:
    resp = urllib.request.urlopen(req)
    print(f"Uploaded: {icons[0][1]}")
except urllib.error.HTTPError as e:
    print(f"Error: {e.code} {e.read().decode()}")
