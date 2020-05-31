from colorcluster import *
import cv2

from utils import get_grayscale, remove_noise
import numpy as np
import tesseract
import imutils

im = cv2.imread("data/original.jpeg")
prepared = remove_noise(im)
clustered = color_clusters(prepared, NUM_CLUSTERS=5)
gray = get_grayscale(clustered)
center_colors = get_center_colors(gray)

colors, count = np.unique(center_colors, axis=None, return_counts = True)

cv2.imshow('mask', clustered)



for angle in [45, 0, -45]:
    rotated = imutils.rotate_bound(gray, angle)
    for color in colors:
        tmp = rotated.copy()
        tmp[tmp != color] = 255
        tmp[tmp == color] = 0
        tesseract.read(tmp)
        cv2.imshow('try', tmp)
        cv2.waitKey()


