import cv2
from PIL import Image
import numpy

def pil2ocv(pil_image):
  cv2_im = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
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
