import os
import random
import ctypes
import time

index = 0

def change_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def get_random_image(folder_path):
    global index
    image_files = [file for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]
    if image_files:
        image_path = os.path.join(folder_path, image_files[index%len(image_files)])
        index += 1
        return image_path
    else:
        return None

def main():
    folder_path = 'C:\\Users\\dudu\\Desktop\\a'  # Specify the path to your folder containing images

    while True:
        image_path = get_random_image(folder_path)

        if image_path:
            change_wallpaper(image_path)
        time.sleep(0.05)
if __name__ == '__main__':
    main()
