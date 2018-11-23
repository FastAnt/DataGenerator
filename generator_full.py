import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
import PIL
import numpy
import random
from PIL import Image
from os import listdir
import os
ia.seed(1)

global_counter = 1
for root_back, dirs_back, files_back in os.walk('./background_hight'):
    for file_back in files_back:
        for i in range(1, 6):
            for root, dirs, files in os.walk('./img1'):
                for file in files:
                    if not file.endswith('.png'):
                        continue
                    global_counter = global_counter + 1
                    background = Image.open(os.path.join(root_back, file_back))
                    old_txt_name = '.' + os.path.join(root, file).split('.')[1] + '.txt'
                    old_txt_file = open(old_txt_name)
                    line = old_txt_file.readline()
                    new_line = ''
                    # for j in range(1, 1):
                    #     is_need_skip = random.randint(0, 10)
                    #     if is_need_skip  > 4 :
                    foreground = Image.open(os.path.join(root, file))
                    orig_width = foreground.width
                    orig_height = foreground.height

                    foreg_size = random.randint(200, 500)
                    size_ratio_w = int(foreg_size) / foreground.width
                    size_ratio_h = int(foreg_size) / foreground.height
                    foreground = foreground.resize((int(foreg_size), int(foreg_size)), Image.ANTIALIAS)
                    if(background.width - foreground.width < 1):
                        continue
                    if (background.height - foreground.height < 1):
                        continue
                    foreg_x = random.randint(0, background.width - foreground.width)
                    foreg_y = random.randint(0, background.height - foreground.height)
                    background.paste(foreground, (foreg_x, foreg_y), foreground)



                    #print(old_txt_name)
                    new_line_list = line.split(' ')
                    if not new_line_list:
                        continue
                    new_line_list[0] = 0

                    y_offset = orig_height * float(new_line_list[2]) * size_ratio_h*0.9
                    x_offset = orig_width * float(new_line_list[1]) * size_ratio_w
                    new_line_list[1] = str(( foreg_x + x_offset) / background.width)
                    new_line_list[2] = str(( foreg_y + y_offset) / background.height)

                    new_line_list[3] = str(float(new_line_list[3]) * orig_width *size_ratio_w / background.width)
                    new_line_list[4] = str(float(new_line_list[4]) * orig_height * size_ratio_h / background.height)
                    new_line = str(new_line_list[0]) + ' ' + str(new_line_list[1]) + ' ' + str(new_line_list[2]) + ' ' + str(
                        new_line_list[3]) + ' ' + str(new_line_list[4]) + '\n'

                    new_file_name_txt = 'result_directory_finger/' + str(global_counter)+'.txt'
                    new_file_name_img = 'result_directory_finger/' + str(global_counter) + '.jpg'
                    new_file = open(new_file_name_txt, 'w')
                    new_file.write(new_line)
                    new_file.close()
                    background.save(new_file_name_img)

