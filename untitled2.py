# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:47:57 2024

@author: Rahul Kumar
"""

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")