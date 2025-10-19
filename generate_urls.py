# generate_google_maps_urls.py

categories = [
    "restaurants", "hotels", "pharmacies", "supermarkets",
    "cafes", "schools", "hospitals", "gyms", "malls", "banks"
]

cities = [
    "Casablanca", "Rabat", "Agadir", 
    "Marrakech", "Tangier", "Fez",
    "Meknes", "Oujda", "Tetouan", "Kenitra", 
   "Safi", 
    "Mohammedia",
    "El Jadida", "Beni Mellal", "Nador", "Taza", "Khouribga", "Laayoune"
]

base_url = "https://www.google.com/maps/search/"

urls = []

for city in cities:
    for category in categories:
        query = f"{category}+{city}".replace(" ", "+")
        url = f"{base_url}{query}/"
        urls.append(url)

# Print or save to file
for u in urls:
    print(u)

# Optionally save to CSV
import csv

with open("morocco_maps_urls.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["City", "Category", "URL"])
    for city in cities:
        for category in categories:
            query = f"{category}+{city}".replace(" ", "+")
            url = f"{base_url}{query}/"
            writer.writerow([city, category, url])

print("\n✅ URLs saved to morocco_maps_urls.csv")




