# -*- coding: utf-8 -*-
"""
分數序列
2/1+3/2+4/3+5/4+6/5+7/6+8/7+....+滿20項求和
"""
mole=2
deno=1
suM=0
cal=0
for i in range(20):
    cal=mole /deno
    suM+=cal
    deno=mole
    mole=mole+1

print("2/1+3/2+...前20項和為{:.5f}".format(suM))