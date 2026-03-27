import urllib.request
import zipfile
import os

# The 10 jewellery images generated for you
images = [
    ("01_Diamond_Solitaire.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_0"),
    ("02_Gold_Statement.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_1"),
    ("03_Sapphire_Pendant.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_2"),
    ("04_Emerald_Halo.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_3"),
    ("05_Luxury_Watch.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_4"),
    ("06_Diamond_Earrings.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_5"),
    ("07_Tennis_Bracelet.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_6"),
    ("08_Ruby_Ring.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_7"),
    ("09_Pearl_Brooch.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_8"),
    ("10_Geometric_Band.jpg", "http://googleusercontent.com/image_collection/image_retrieval/15520652788677440345_9")
]

zip_name = "jewellery_images.zip"
temp_dir = "temp_images"

if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

print("Downloading images...")

try:
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for filename, url in images:
            filepath = os.path.join(temp_dir, filename)
            try:
                urllib.request.urlretrieve(url, filepath)
                zipf.write(filepath, filename)
                print(f"Added: {filename}")
            except Exception as e:
                print(f"Could not download {filename}: {e}")
    print(f"\nSuccess! Your file is ready: {zip_name}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Cleanup temp files
    for filename, _ in images:
        path = os.path.join(temp_dir, filename)
        if os.path.exists(path):
            os.remove(path)
    os.rmdir(temp_dir)