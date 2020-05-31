import cv2
from PIL import Image
import numpy as np

def pil2ocv(pil_image):
  cv2_im = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
  return cv2_im

def ocv2pil(cv2_im):
  cv2_im = cv2.cvtColor(cv2_im,cv2.COLOR_BGR2RGB)
  pil_im = Image.fromarray(cv2_im)
  return pil_im

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image,5)

# dilation
def dilate(image):
    kernel = np.ones((3, 3), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((3, 3), np.uint8)
    return cv2.erode(image, kernel, iterations=1)