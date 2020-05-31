import pytesseract


def get_configs():
    configs = []
    psm = [7,8,11,12,13]
    for p in psm:
        for oem in [0,3]:
            configs.append(f'-l eng --oem {oem} --psm {p} --tessdata-dir  tessdata --user-words data/brands.txt')
    return configs


def read(im):
    configs = get_configs()
    results = []
    for c in configs:
        text = pytesseract.image_to_string(im, config=c)
        results.append([text.lower(), c])
        print(text,"  ::  ", c)
    return results



