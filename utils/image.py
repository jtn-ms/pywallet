import cv2
import numpy as np

def byte2img(bytestr,filename=None,debug=False):
    bytestr = bytestr[2:] if isinstance(bytestr,str) and bytestr.startswith('0x') else bytestr
    
    if len(bytestr) == 64:
        img = np.reshape(np.uint8([int(byte,16)*16 for byte in bytestr]),(8,8))
    elif len(bytestr) == 40:
        img = np.reshape(np.uint8([int(byte,16)*16 for byte in bytestr]),(5,8))
    else: return
    if filename:
        cv2.imwrite(filename,img)
    if debug:
        cv2.imshow('image',img)
        if cv2.waitKey(10000) & 0xFF == ord('q'):return

import os
def img2byte(img,debug=False):
    if isinstance(img,str):
        if not os.path.exists(img): return ""
        img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    bytestr=""
    for byte in np.reshape(img,img.shape[0] * img.shape[1]):
        bytestr += hex(byte/16).replace("0x","").strip("L")
    if debug: print bytestr
    return bytestr