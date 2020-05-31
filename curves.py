import cv2
import numpy as np
import pytesseract
from utils import erode, dilate
import tesseract

def preprocess(im):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    # ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_TRUNC)[1]
    thresh = cv2.threshold(thresh, 60, 255, cv2.THRESH_BINARY_INV)[1]
    thresh = erode(thresh)
    thresh = dilate(thresh)
    return thresh

def character_recognition(im):
    ctrs, hier = cv2.findContours(im, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[0])

    for i, ctr in enumerate(sorted_ctrs):
        x, y, w, h = cv2.boundingRect(ctr)

        roi = img[y:y + h, x:x + w]

        mask = np.zeros((img.shape[0], img.shape[1]), np.uint8)
        # mask = img.copy()
        # mask = 0
        cv2.drawContours(mask, ctr, -1, (255, 255, 255), 10)
        # bin_mask = cv2.threshold(mask, 60, 255, cv2.THRESH_BINARY_INV)[1]
        # roi2 = cv2.bitwise_not(thresh[y:y + h, x:x + w])
        character = cv2.bitwise_and(thresh, thresh, mask=mask)
        cv2.imshow('roi', character)
        config = "-l eng --oem 0 --tessdata-dir  tessdata --psm 10"
        text = pytesseract.image_to_string(character, config=config)
        print(text)
        cv2.waitKey(0)

        area = w * h

        if 200 < area < 1900:
            # cv2.imshow('roi', roi2)
            # cv2.waitKey(0)
            # config = "-l eng --oem 0 --tessdata-dir  tessdata --psm 10"
            # text = pytesseract.image_to_string(roi2, config=config)
            print(text)

            rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow('rect', rect)


img = cv2.imread("data/rotated.jpeg")
prepared = preprocess(img)
prepared = cv2.bitwise_not(prepared)
tesseract.read(prepared)
cv2.imshow('thresh', prepared)
cv2.waitKey(0)