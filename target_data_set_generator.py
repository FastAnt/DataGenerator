from imgaug import augmenters as iaa
import numpy as np
from PIL import Image
import os
NUMBER_OF_REPEATS = 3
global_counter = 0
for root, dirs, files in os.walk('./targets'):
    for file in files:

        if file.endswith('.png'):
            for i in range(1, NUMBER_OF_REPEATS):
                old_txt_name = '.' + os.path.join(root, file).split('.')[1] + '.txt'
                old_txt_file = open(old_txt_name)
                line = old_txt_file.readline()

                img =  Image.open(os.path.join(root, file))
                width, height = img.size

                aug = iaa.PiecewiseAffine(scale=(0.01, 0.03))
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

                aug = aug = iaa.ContrastNormalization((0.4, 1.7))
                images = np.random.randint(0, 255, (16,height ,width , 4), dtype=np.uint8)
                images[0] = Image.open(os.path.join(root,file))
                images[0] = aug.augment_image(images[0])
                new_file_name_txt = 'result_directory_targets/'+ 'ContrastNormalization_' + str(global_counter) + '.txt'
                new_file_name_img = 'result_directory_targets/'+ 'ContrastNormalization_' + str(global_counter) + '.png'
                new_file = open(new_file_name_txt, 'w')
                new_file.write(line)
                new_file.close()
                Image.fromarray(images[0]).save(new_file_name_img)

                aug = iaa.Affine(shear=(-19, 19))
                images = np.random.randint(0, 255, (16,height ,width , 4), dtype=np.uint8)
                images[0] = Image.open(os.path.join(root,file))
                images[0] = aug.augment_image(images[0])
                new_file_name_txt = 'result_directory_targets/' +'Affine_' + str(global_counter) + '.txt'
                new_file_name_img = 'result_directory_targets/' +'Affine_' + str(global_counter) + '.png'
                new_file = open(new_file_name_txt, 'w')
                new_file.write(line)
                new_file.close()
                Image.fromarray(images[0]).save(new_file_name_img)


                aug = iaa.CoarseDropout((0.0, 0.07), size_percent=(0.02, 0.29))
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
