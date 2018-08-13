from __future__ import print_function

def answer(x,y):
    r=set(x)
    s=set(y)

    m = [a for a in x if a not in s]
    n = [b for b in y if b not in r]
    o = m+n
    print (*o,sep=',')

x = [14, 27, 1, 4, 2, 50, 3, 1, 99]
y = [2, 4, -4, 3, 1, 1, 14, 27, 50]

answer(x,y)

