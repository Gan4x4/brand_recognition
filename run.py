import dataset
from colorcluster import *
import cv2

from utils import get_grayscale, remove_noise
import numpy as np
import tesseract
import imutils

def check(brand, results):
    for txt, config in results:
        if brand in txt:
            return config
    return None


def filter_by_color(img, inv = False):
    if inv :
        background = 255
        foreground = 0
    else:
        background = 0
        foreground = 255

    tmp = img.copy()
    tmp[tmp != color] = background
    tmp[tmp == color] = foreground
    return tmp

i = 0
good = 0
for file, brand in dataset.dataset:
    im = cv2.imread(file)
    print (im.shape)
    aspect = im.shape[0]/im.shape[1]
    w = 300
    im = cv2.resize(im, (w, int(w*aspect)))
    cv2.imshow('current', im)

    prepared = remove_noise(im)
    #prepared = im
    clustered = color_clusters(prepared, NUM_CLUSTERS=8)
    gray = get_grayscale(clustered)
    center_colors = get_center_colors(gray)

    colors, count = np.unique(center_colors, axis=None, return_counts=True)



    print(brand,file)

    finded = False
    for angle in [45, 0, -45]:
        print(angle)
        rotated = imutils.rotate_bound(gray, angle)

        for color in colors[:3]:
            for inv in [True,False]:
                filtered = filter_by_color(rotated,inv)
                h = filtered.shape[0]
                w = filtered.shape[1]
                cropped = filtered[int(h*.35):int(h*.65), 0:w]
                cv2.imshow('cropped', cropped)
                cv2.waitKey(1)
                results = tesseract.read(cropped)
                if check(brand,results):
                    print(brand, "OK")
                    finded = True
            #cv2.imshow('try', tmp)
            #cv2.waitKey()

    if finded:
        good += 1
    i +=1


    print (f' detected{good} from {i}')
