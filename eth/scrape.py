import urllib3
http = urllib3.PoolManager()

def url2content(url):
    r = http.request('GET',url)
    return r.data

def blknum2blkhash(blknum):
    skey = '>Hash:</div><divclass="col-md-9">'
    ekey = '</div>'
    url="https://etherscan.io/block/%s"%blknum
    content = url2content(url).replace("\n","").replace(" ","")
    return extractTarget(content,skey,ekey)

def extractTarget(content,skey,ekey):
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

if __name__ == "__main__":
    print(blknum2blkhash(12232161))