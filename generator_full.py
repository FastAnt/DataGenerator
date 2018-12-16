import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import PIL
import numpy
import random
from PIL import Image
from os import listdir
import os

NUMBER_OF_REPEATS = 3

MIN_SIZE = 30
MAX_SIZE = 165


#zone for generative
MINIMAL_X = 0
MINIMAL_Y = 0

# string contants
BACKGROUNDS_FOLDER = './backgrounds'
TARGETS_FOLDER = './result_directory_targets'
OUTPUT_FOLDER = './result_directory'


ia.seed(1)



# counter for naming
global_counter = 1

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

for root_back, dirs_back, files_back in os.walk(BACKGROUNDS_FOLDER):
    files_back = filter(lambda file: file.endswith('.png'), files_back)

    for file_back in files_back:
        for i in range(1, NUMBER_OF_REPEATS):
            for root, dirs, files in os.walk(TARGETS_FOLDER):
                files = filter(lambda file: file.endswith('.png'), files)

                for file in files:
                    global_counter = global_counter + 1
                    background = Image.open(os.path.join(root_back, file_back))

                    new_file_name_txt = OUTPUT_FOLDER + '/' + str(global_counter) + '.txt'
                    new_file_name_img = OUTPUT_FOLDER + '/' + str(global_counter) + '.png'
                    new_line = ''

                    # process each image file max 3 times
                    for j in range(1, 3):
                        # each file has 40% probability to be processed
                        is_need_skip = random.randint(0, 10)
                        if is_need_skip > 4:
                            continue


                        old_txt_name = '.' + os.path.join(root, file).split('.')[1] + '.txt'
                        old_txt_file = open(old_txt_name)
                        line = old_txt_file.readline()
                        new_line = ''

                        foreground = Image.open(os.path.join(root, file))
                        orig_width = foreground.width
                        orig_height = foreground.height

                        new_foreg_size = random.randint(MIN_SIZE, MAX_SIZE)
                        size_ratio_w = int(new_foreg_size) / orig_width
                        size_ratio_h = int(new_foreg_size) / orig_height

                        if (background.width - new_foreg_size < 1 or background.height - new_foreg_size < 1):
                            continue

                        foreground = foreground.resize((int(new_foreg_size), int(new_foreg_size)), Image.ANTIALIAS)

                        #paste target on background
                        foreg_x = random.randint(int(background.width/2), background.width - foreground.width)
                        foreg_y = random.randint(0, int((background.height - foreground.height)/2))
                        background.paste(foreground, (foreg_x, foreg_y), foreground)

                        new_line_list = line.split(' ')
                        if not new_line_list:
                            continue

                        y_offset = orig_height * float(new_line_list[2]) * size_ratio_h
                        x_offset = orig_width * float(new_line_list[1]) * size_ratio_w
                        new_line_list[1] = str(( foreg_x + x_offset) / background.width)
                        new_line_list[2] = str(( foreg_y + y_offset) / background.height)

                        new_line_list[3] = str(float(new_line_list[3]) * orig_width *size_ratio_w / background.width)
                        new_line_list[4] = str(float(new_line_list[4]) * orig_height * size_ratio_h / background.height)
                        new_line = " ".join(new_line_list)


                        new_file = open(new_file_name_txt, 'a+')
                        new_file.write(new_line)
                        new_file.close()

                    if new_line=='':
                        new_file = open(new_file_name_txt, 'a+')
                        new_file.write('')
                    background.save(new_file_name_img)

