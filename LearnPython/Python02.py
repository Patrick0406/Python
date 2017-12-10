#!/usr/bin/python
# -*- coding: UTF-8 -*-
#文件名：python02.py

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)/2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print quicksort([3,6,8,10,1,2,1])
