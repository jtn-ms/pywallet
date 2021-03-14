# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json

def str2dict(string):
    json_acceptable_string = string.replace("'", "\"").replace("\n","")
    return json.loads(json_acceptable_string)

def extractResult(content,skey='"result":"',ekey='"'):
    sidx,eidx=-1,-1

    try:
        sidx = content.index(skey) + len(skey)
    except:
        sidx = -2

    if sidx > 0:
        try:
            eidx = content[sidx:].index(ekey)
        except:
            eidx = -2
        if eidx > 0:
            return content[sidx:sidx+eidx]
    return ""