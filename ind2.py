#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    A = tuple(map(int, input().split()))
    s = 0
    for item in A:
        if not ((item % 2) == 0):
            s += item
    x0 = 0
    x1 = 0
    for i, a in enumerate(A):
        if a < 0:
            x0 = i
            break
    for i, a in enumerate(A[::-1]):
        if a < 0:
            x1 = len(A) - 1 - i
            break
    print(s)
    print(sum(A[x0 + 1:x1]))
