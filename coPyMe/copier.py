import os
import glob
from shutil import copy

path = 'your_path'

with open('./kits2.txt', 'r') as file:
    for row in file:
        image = row.split(',')[1]
        image = image[3:]
        image = image.strip()
        
        if image.endswith(('XR')):
            image = image.replace('XR', 'XPR')
        if image.endswith('XL'):
            continue
        
        image = image + '.jpg'

        print(image)
        image = image.strip()
        for root, dirs, files in os.walk(path):
            for file in files:
                if image in file:
                    image_path = os.path.join(root, file)
                    my_path = image_path[len(path):image_path.rfind('\\')]
                    my_path = os.path.join(os.getcwd(), my_path)
                    os.makedirs(my_path, exist_ok=True)
                    copy(image_path, my_path)
                    print(image_path)
