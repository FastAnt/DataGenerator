import cv2
import numpy as np
from PIL import Image
import random


background = Image.open('./1.png')
foreground = Image.open("./chaica_0.png")

foreg_size = random.randint(100, 400)

size_ratio_w = int(foreg_size)/foreground.width
size_ratio_h = int(foreg_size)/foreground.height
foreground = foreground.resize((int(foreg_size), int(foreg_size)), Image.ANTIALIAS)


foreg_x = random.randint(0, background.width - foreground.width)
foreg_y = random.randint(0, background.height - foreground.height)
background.paste(foreground, (foreg_x, foreg_y), foreground)

file = open('./chaica_0.txt')
line =  file.readline()
print(line.split(' '))
new_line_list =line.split(' ')
new_line_list[1] = (foreg_x +foreg_size/2)/ background.width
new_line_list[2] = (foreg_y +foreg_size/2)/ background.height

new_line_list[3] = str(float(new_line_list[3]) * size_ratio_w*1.3)
new_line_list[4] = str(float(new_line_list[4]) * size_ratio_h*1.3)
print(new_line_list)
new_line = str(new_line_list[0]) + ' '+str(new_line_list[1]) + ' ' +str(new_line_list[2]) +' '+str(new_line_list[3]) + ' '+str(new_line_list[4]) + '\n'
second_new_line = str(new_line_list[0]) + ' '+str(new_line_list[1]) + ' ' +str(new_line_list[2]) +' '+str(new_line_list[3]) + ' '+str(new_line_list[4])
file = open('new.txt', 'w')
file.write(new_line)
file.write(second_new_line)
file.close()
background.show()
background.save("new.jpg")