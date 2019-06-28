import cv2
import numpy as np

def byte2img(bytestr,filename=None,debug=False,grayscale=False):
    bytestr = bytestr[2:] if isinstance(bytestr,str) and bytestr.startswith('0x') else bytestr
    hexlen = len(bytestr)
    binlen = 4*hexlen
    binstr = bin(int(bytestr,16))[2:]
    binstr = '0'*(binlen-len(binstr)) + binstr
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
        filepath = img
        img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    rows,cols=img.shape[:2]
    if rows != 16 or cols !=16:
        img = cv2.resize(img, (16, 16))
        #_,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
        dirpath,filename = os.path.split(filepath)
        fn,ext = os.path.splitext(filename)
        fullpath = os.path.join("keyimgs",fn.replace("Scrapper", "prvkey")+ext)
        cv2.imwrite(fullpath,img)
    bytestr=""
    if grayscale:
        for byte in np.reshape(img,img.shape[0] * img.shape[1]): bytestr += hex(byte/16).replace("0x","").strip("L")
    else:
        binstr=""
        for binary in np.reshape(img,img.shape[0] * img.shape[1]): binstr += "1" if binary > 0 else "0"
        bytestr = hex(int(binstr,2)).replace("0x","").strip("L")
        bytestr = '0'*(64-len(bytestr)) + bytestr
    if bytestr == '0' * 64: bytestr = '1'*64
    if debug:
        from eth.key import priv2addr; 
        from eth.req import getbalance;
        addr = priv2addr(bytestr)
        print addr,bytestr,getbalance(addr)
    return bytestr

def dataset2privkeys(fullpath,debug=True):
    from os import listdir
    from os.path import isfile, join
    return [img2byte(join(fullpath, f),debug) for f in listdir(fullpath) if isfile(join(fullpath, f))]