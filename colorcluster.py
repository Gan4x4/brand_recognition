from __future__ import print_function
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

import numpy as np
from utils import ocv2pil, pil2ocv


def color_clusters(cv2_im, NUM_CLUSTERS=3):
    im = ocv2pil(cv2_im)
    coef = 350 / min(im.size)
    im = im.resize((int(im.size[0] * coef), int(im.size[1] * coef)))      # optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    #print('finding clusters')
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    #print('cluster centres:\n', codes)
    codes = codes.astype(np.uint8)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent
    peak = codes[index_max]
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    #print('most frequent is %s (#%s)' % (peak, colour))

    import imageio
    c = ar.copy()
    for i, code in enumerate(codes):
        c[scipy.r_[scipy.where(vecs==i)],:] = code
    #imageio.imwrite('clusters.png', c.reshape(*shape).astype(np.uint8))
    #print('saved clustered image')
    out =  c.reshape(*shape).astype(np.uint8)
    out = pil2ocv(out)
    return out

def get_center_colors(gray_im):
    center = np.array(gray_im.shape[:2])/2
    colors = []
    for i in range(-5,5,2):
        for j in range (-5,5,2):
            x = int(center[0] + i)
            y = int(center[1] + j)
            colors.append(gray_im[x,y])

    return np.array(colors)