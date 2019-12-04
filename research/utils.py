# -*- coding: utf-8 -*-
# junying-todo, 2019-12-03

PRIVATE_ADDR_LENGTH = 64
PRIVATE_ADDR_MAX_INT = 115792089237316195423570985008687907853269984665640564039457584007913129639935L
ADDR_LENGTH = 40
ADDR_MAX_INT = 1461501637330902918203684832716283019655932542975L

def int2hex(value):
    if isinstance(value,str): value=str(value)
    hexstr=hex(value)
    if hexstr.startswith('0x'): hexstr=hexstr[2:]
    hexstr = hexstr.strip('L')
    if len(hexstr) < PRIVATE_ADDR_LENGTH: 
        hexstr = '0'*(PRIVATE_ADDR_LENGTH - len(hexstr)) + hexstr
    return hexstr

def hex2int(value):
    return int(value,16)

def normalize_privaddr(value):
    if isinstance(value,str): value=hex2int(value)
    return 1.0/(PRIVATE_ADDR_MAX_INT/value)

def normalize_addr(value):
    if isinstance(value,str): value=hex2int(value)
    return 1.0/(ADDR_MAX_INT/value)