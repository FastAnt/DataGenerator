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


ia.seed(1)

# counter for naming
global_counter = 1

for root_back, dirs_back, files_back in os.walk('./backgrounds'):
    for file_back in files_back:
        for i in range(1, NUMBER_OF_REPEATS):
            for root, dirs, files in os.walk('./result_directory_targets'):
                for file in files:
                    if not file.endswith('.png'):
                        continue
                    global_counter = global_counter + 1
                    background = Image.open(os.path.join(root_back, file_back))

                    new_file_name_txt = 'result_directory/' + str(global_counter) + '.txt'
                    new_file_name_img = 'result_directory/' + str(global_counter) + '.jpg'
                    new_line = ''
                    for j in range(1, 3):
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

                        foreg_size = random.randint(MIN_SIZE, MAX_SIZE)
                        size_ratio_w = int(foreg_size) / foreground.width
                        size_ratio_h = int(foreg_size) / foreground.height

                        foreground = foreground.resize((int(foreg_size), int(foreg_size)), Image.ANTIALIAS)
                        if(background.width - foreground.width < 1):
                            continue
                        if (background.height - foreground.height < 1):
                            continue

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
                        new_line = str(new_line_list[0]) + ' ' + str(new_line_list[1]) + ' ' + str(new_line_list[2]) + ' ' + str(
                            new_line_list[3]) + ' ' + str(new_line_list[4]) + '\n'


                        new_file = open(new_file_name_txt, 'a+')
                        new_file.write(new_line)
                        new_file.close()

                    if new_line=='':
                        new_file = open(new_file_name_txt, 'a+')
                        new_file.write('')
                    background.save(new_file_name_img)

