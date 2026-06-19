import os
import requests
from zipfile import ZipFile

# --------------- FOLDER SETUP ---------------
os.makedirs("assets/images", exist_ok=True)
os.makedirs("lib/models", exist_ok=True)

# --------------- IMAGE LINKS ---------------
images = {
    "france_eiffel.jpg": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
    "france_louvre.jpg": "https://images.unsplash.com/photo-1569176812925-1413cccf1a47",
    "india_taj.jpg": "https://images.unsplash.com/photo-1548013146-72479768bada",
    "india_jaipur.jpg": "https://images.unsplash.com/photo-1555685812-4b943f1cb0eb",
    "usa_grandcanyon.jpg": "https://images.unsplash.com/photo-1508264165352-258859e62245",
    "usa_goldengate.jpg": "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "italy_colosseum.jpg": "https://images.unsplash.com/photo-1526772662000-3f88f10405ff",
    "japan_fuji.jpg": "https://images.unsplash.com/photo-1549693578-d683be217e58",
    "turkey_cappadocia.jpg": "https://images.unsplash.com/photo-1555066931-4365d14bab8c",
    "thailand_phuket.jpg": "https://images.unsplash.com/photo-1493558103817-58b2924bce98",
    "greece_santorini.jpg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
    "uk_bigben.jpg": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d",
    "mexico_chichen.jpg": "https://images.unsplash.com/photo-1548022965-3b6b682a24f8",
}

# --------------- DOWNLOAD IMAGES ---------------
for name, url in images.items():
    print(f"⬇️ Downloading {name}...")
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(f"assets/images/{name}", "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    else:
        print(f"⚠️ Failed to download {name}")

# --------------- ZIP IMAGES ---------------
with ZipFile("travel_app_assets.zip", "w") as zipf:
    for root, _, files in os.walk("assets/images"):
        for file in files:
            zipf.write(os.path.join(root, file))
print("✅ Images zipped as travel_app_assets.zip")

# --------------- GENERATE travel_data.dart ---------------
travel_data = """// GENERATED FILE: Travel data for Travel App UI
// DO NOT EDIT MANUALLY

final Map<String, List<Map<String, String>>> travelData = {
  "France": [
    {"name": "Eiffel Tower, Paris", "image": "assets/images/france_eiffel.jpg"},
    {"name": "Louvre Museum", "image": "assets/images/france_louvre.jpg"}
  ],
  "India": [
    {"name": "Taj Mahal, Agra", "image": "assets/images/india_taj.jpg"},
    {"name": "Jaipur Palace", "image": "assets/images/india_jaipur.jpg"}
  ],
  "United States": [
    {"name": "Grand Canyon, Arizona", "image": "assets/images/usa_grandcanyon.jpg"},
    {"name": "Golden Gate Bridge, California", "image": "assets/images/usa_goldengate.jpg"}
  ],
  "Italy": [
    {"name": "Colosseum, Rome", "image": "assets/images/italy_colosseum.jpg"}
  ],
  "Japan": [
    {"name": "Mount Fuji", "image": "assets/images/japan_fuji.jpg"}
  ],
  "Turkey": [
    {"name": "Cappadocia Balloons", "image": "assets/images/turkey_cappadocia.jpg"}
  ],
  "Thailand": [
    {"name": "Phuket Beaches", "image": "assets/images/thailand_phuket.jpg"}
  ],
  "Greece": [
    {"name": "Santorini Island", "image": "assets/images/greece_santorini.jpg"}
  ],
  "United Kingdom": [
    {"name": "Big Ben, London", "image": "assets/images/uk_bigben.jpg"}
  ],
  "Mexico": [
    {"name": "Chichén Itzá, Yucatán", "image": "assets/images/mexico_chichen.jpg"}
  ]
};
"""

with open("lib/models/travel_data.dart", "w", encoding="utf-8") as f:
    f.write(travel_data)

print("✅ travel_data.dart created successfully at lib/models/travel_data.dart")
print("\n🎉 All done! You now have:")
print("   1. Offline images in assets/images/")
print("   2. travel_app_assets.zip for backup")
print("   3. travel_data.dart ready to use in your Flutter app")
