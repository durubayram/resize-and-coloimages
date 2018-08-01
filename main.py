import random
import cv2
from PIL import Image, ImageEnhance
import os


path = "C:/Users/DURU BAYRAM/PycharmProjects/untitled/photos/"  # path for photos
dirs = os.listdir(path)

new_path = "C:/Users/DURU BAYRAM/PycharmProjects/untitled/resized_photos/"
# path where resized and colored photos will upload

image_path_list = []
valid_image_extensions = [".jpg", ".jpeg"]  # specify valid extensions
valid_image_extensions = [item.lower() for item in valid_image_extensions]


for file in os.listdir(path):
    extension = os.path.splitext(file)[1]
    image_path_list.append(os.path.join(path, file))


for imagePath in image_path_list:
    image = cv2.imread(imagePath)

    if image is not None:
        cv2.imshow(imagePath, image) # show image
    elif image is None:
        print("Error loading: " + imagePath)
        # end this loop iteration and move on to next image
        continue

    key = cv2.waitKey(0)
    if key == 27:  # escape
        break
# close any open windows
cv2.destroyAllWindows()


def resize():
    for i in range(0, 32):
        item = dirs[i]
        if os.path.isfile(path+item):
            dx = dy = 512
            im = Image.open(path+item)
            w, h = im.size
            x = random.randint(0, w-dx-1)
            y = random.randint(1, h-dy-1)
            f, e = os.path.splitext(path+item)
            new_image = im.crop((x, y, x+dx, y+dy))
            change_colors(new_image)
            output, _ = os.path.splitext(new_path)
            new_image.save(output + f[-2:] + ' renew.jpg', 'JPEG', quality=90)


def change_colors(x):
    en = ImageEnhance.Color(x)
    img = en.enhance(3) #color type
    img.show()


resize()
