from imgaug import augmenters as iaa
import numpy as np
from PIL import Image
import os

aug = iaa.PiecewiseAffine(scale=(0.01, 0.05))
images = np.random.randint(0, 255, (16,105, 120, 4), dtype=np.uint8)
images[0] = Image.open("/home/amelnytskyi/develop/DataGenerator/DataGenerator/test_for_nozer/Ua_1.10_warning-bumpy_road.svg.png")
images[0] = aug.augment_image(images[0])
#images[0].save("./1.png")
Image.fromarray(images[0]).save("./1.png")


aug = aug = iaa.ContrastNormalization((0.5, 1.5))
images = np.random.randint(0, 255, (16,105, 120, 4), dtype=np.uint8)
images[0] = Image.open("/home/amelnytskyi/develop/DataGenerator/DataGenerator/test_for_nozer/Ua_1.10_warning-bumpy_road.svg.png")
images[0] = aug.augment_image(images[0])
#images[0].save("./1.png")
Image.fromarray(images[0]).save("./2.png")

aug = iaa.Affine(shear=(-16, 16))
images = np.random.randint(0, 255, (16,105, 120, 4), dtype=np.uint8)
images[0] = Image.open("/home/amelnytskyi/develop/DataGenerator/DataGenerator/test_for_nozer/Ua_1.10_warning-bumpy_road.svg.png")
images[0] = aug.augment_image(images[0])
#images[0].save("./1.png")
Image.fromarray(images[0]).save("./3.png")

# aug = iaa.Grayscale(alpha=(0.0, 1.0))
# images = np.random.randint(0, 255, (16,105, 120, 4), dtype=np.uint8)
# images[0] = Image.open("/home/amelnytskyi/develop/DataGenerator/DataGenerator/test_for_nozer/Ua_1.10_warning-bumpy_road.svg.png")
# images[0] = aug.augment_image(images[0])
# #images[0].save("./1.png")
# Image.fromarray(images[0]).save("./4.png")

aug = iaa.CoarseDropout((0.0, 0.05), size_percent=(0.02, 0.25))
images = np.random.randint(0, 255, (16,105, 120, 4), dtype=np.uint8)
images[0] = Image.open("/home/amelnytskyi/develop/DataGenerator/DataGenerator/test_for_nozer/Ua_1.10_warning-bumpy_road.svg.png")
images[0] = aug.augment_image(images[0])
#images[0].save("./1.png")
Image.fromarray(images[0]).save("./4.png")

global_counter = 0
for root, dirs, files in os.walk('./targets'):
    for file in files:
        if file.endswith('.png'):
            old_txt_name = '.' + os.path.join(root, file).split('.')[1] + '.txt'
            old_txt_file = open(old_txt_name)
            line = old_txt_file.readline()

            img =  Image.open(os.path.join(root, file))
            width, height = img.size
            aug = iaa.PiecewiseAffine(scale=(0.01, 0.05))
            images = np.random.randint(0, 255, (16,height ,width , 4), dtype=np.uint8)

            images[0] = Image.open(os.path.join(root,file))
            images[0] = aug.augment_image(images[0])
            #Image.fromarray(images[0]).save("./1.png")

            new_file_name_txt = 'result_directory_targets/'+ 'PiecewiseAffine_'+ str(global_counter) + '.txt'
            new_file_name_img = 'result_directory_targets/'+ 'PiecewiseAffine_' + str(global_counter) + '.png'
            new_file = open(new_file_name_txt, 'w')
            new_file.write(line)
            new_file.close()
            Image.fromarray(images[0]).save(new_file_name_img)

            aug = aug = iaa.ContrastNormalization((0.5, 1.5))
            images = np.random.randint(0, 255, (16,height ,width , 4), dtype=np.uint8)
            images[0] = Image.open(os.path.join(root,file))
            images[0] = aug.augment_image(images[0])
            new_file_name_txt = 'result_directory_targets/'+ 'ContrastNormalization_' + str(global_counter) + '.txt'
            new_file_name_img = 'result_directory_targets/'+ 'ContrastNormalization_' + str(global_counter) + '.png'
            new_file = open(new_file_name_txt, 'w')
            new_file.write(line)
            new_file.close()
            Image.fromarray(images[0]).save(new_file_name_img)

            aug = iaa.Affine(shear=(-16, 16))
            images = np.random.randint(0, 255, (16,height ,width , 4), dtype=np.uint8)
            images[0] = Image.open(os.path.join(root,file))
            images[0] = aug.augment_image(images[0])
            new_file_name_txt = 'result_directory_targets/' +'Affine_' + str(global_counter) + '.txt'
            new_file_name_img = 'result_directory_targets/' +'Affine_' + str(global_counter) + '.png'
            new_file = open(new_file_name_txt, 'w')
            new_file.write(line)
            new_file.close()
            Image.fromarray(images[0]).save(new_file_name_img)


            aug = iaa.CoarseDropout((0.0, 0.05), size_percent=(0.02, 0.25))
            images = np.random.randint(0, 255, (16,height ,width , 4), dtype=np.uint8)
            images[0] = Image.open(os.path.join(root,file))
            images[0] = aug.augment_image(images[0])
            new_file_name_txt = 'result_directory_targets/' +'CoarseDropout_' + str(global_counter) + '.txt'
            new_file_name_img = 'result_directory_targets/'+'CoarseDropout_' + str(global_counter) + '.png'
            new_file = open(new_file_name_txt, 'w')
            new_file.write(line)
            new_file.close()
            Image.fromarray(images[0]).save(new_file_name_img)

            global_counter = global_counter + 1
