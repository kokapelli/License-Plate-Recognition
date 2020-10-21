from PIL import Image
import os, shutil
from tqdm import tqdm

path = "images/"
p240 = (352, 240)
p480 = (720, 480)
size =  p480

def resize():
    # Resize all images
    print("Resizing images...")
    for item in tqdm(os.listdir(path)):
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            if im.mode in ("RGBA", "P"):
                im = im.convert("RGB")
            f, e = os.path.splitext(path+item)
            imResize = im.resize(size, Image.ANTIALIAS)
            imResize.save(f + '_r.jpg', 'JPEG', quality=90)

            # Remove original image
            try:
                if os.path.isfile(path+item) or os.path.islink(path+item):
                    os.unlink(path+item)
                elif os.path.isdir(path+item):
                    shutil.rmtree(path+item)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (path+item, e))

resize()
print("Resizing complete")