import numpy as np
import cv2
from os import listdir
import os



class ImageProcessor:
    def __init__(self):
        pass

    def run(self, input_folder, output_folder, extensions, filters):
        for root_back, dirs_back, files in os.walk(input_folder):
            files = filter(lambda file: file.endswith(tuple(extensions)), files)

            if not os.path.exists(output_folder):
                os.makedirs(output_folder)

            for file in files:
                cv_image = self.open_file(input_folder, file)

                # TODO: use priority of filters
                if "contours" in filters:
                    cv_image = self.contours(cv_image)

                if "canny" in filters:
                    cv_image = self.canny(cv_image)

                self.save_file(output_folder, file, cv_image)


    def open_file(self, input_folder, filename):
        im = cv2.imread(input_folder + filename)
        return im

    def save_file(self, output_folder, filename, cv_image):
        cv2.imwrite(output_folder + filename, cv_image)


    def contours(self, cv_image):
        imgray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return im2

    def canny(self, cv_image):
        edges = cv2.Canny(cv_image, 100, 200)
        return edges


def main():
    INPUT_FOLDER = './result_directory/'
    OUTPUT_FOLDER = './processed_files/'

    image_processor = ImageProcessor()
    image_processor.run(INPUT_FOLDER, OUTPUT_FOLDER, [".png", ".jpg"], ["canny", "contours"])

main()