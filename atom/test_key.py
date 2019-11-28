# -*- coding: utf-8 -*-
# import py.test

from atom.key import genkey

def test_htdf(count=10):
    lstRet = []
    for _ in range(count):
        lstRet.append(genkey('htdf'))
    assert len(lstRet) == count
    
