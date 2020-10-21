import os

# DEPRECATED! Same functionality can be achieved on Microsoft 10 by
# selected all images, press F2, rename as see fit

path = 'images/'

print("Renaming...")
for index, filename in enumerate(sorted(os.listdir(path))):
    try:
        os.rename(os.path.join(path, filename), os.path.join(path, ''.join(['image', str(index), '.jpg'])))
    except Exception as e:
        print(f"{filename} -> Renaming Failed")