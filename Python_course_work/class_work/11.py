photos = {
    "1": "beach.png",
    "2": "mountain.jpg",
    "3": "party.jpg",
    "4": "selfie.png",
    "5": "birthday.png",
    "6": "concert.jpg",
    "7": "sunset.jpg",
    "8": "trip"
}

print("Photo Gallery:")
for key, value in photos.items():
    print(f"{key}. {value}")

selection = input("\nSelect photos to share (enter numbers separated by commas):\nYour selection: ")

selected_numbers = selection.split(",")
unique_photos = []

for num in selected_numbers:
    photo = photos.get(num.strip())
    if photo and photo not in unique_photos:
        unique_photos.append(photo)

print("\nSharing the following photos:")
for photo in unique_photos:
    print(photo)
