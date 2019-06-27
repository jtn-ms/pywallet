import cv2
import numpy as np

def byte2img(bytestr,filename=None,debug=False,grayscale=False):
    bytestr = bytestr[2:] if isinstance(bytestr,str) and bytestr.startswith('0x') else bytestr
    hexlen = len(bytestr)
    binlen = 4*hexlen
    binstr = bin(int(bytestr,16))[2:]
    binstr = ''.join(['0']*(binlen-len(binstr))) + binstr
    hexarr = np.uint8([int(byte,16)*16 for byte in bytestr])
    binarr = np.uint8([int(binary)*255 for binary in binstr])
    if len(bytestr) == 64:
        img = np.reshape(binarr,(16,16))# if not grayscale else np.reshape(hexarr,(8,8))
    elif len(bytestr) == 40:
        img = np.reshape(binarr,(10,16)) if not grayscale else np.reshape(hexarr,(5,8))
    else: return
    if filename:
        cv2.imwrite(filename,img)
    if debug:
        cv2.imshow('image',img)
        if cv2.waitKey(10000) & 0xFF == ord('q'):return

import os
def img2byte(img,debug=False,grayscale=False):
    if isinstance(img,str):
        if not os.path.exists(img): return ""
        img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    bytestr=""
    if grayscale:
        for byte in np.reshape(img,img.shape[0] * img.shape[1]): bytestr += hex(byte/16).replace("0x","").strip("L")
    else:
        binstr=""
        for binary in np.reshape(img,img.shape[0] * img.shape[1]): binstr += "1" if binary > 0 else "0"
        bytestr = hex(int(binstr,2)).replace("0x","").strip("L")
    if debug: print bytestr
    return bytestr