import math, json

def addnums(a,b):
    return a + b

def multiply(a,b):
    c = 0
    for i in range(b):
        c += a
    return c

def circlearea(r):
    return 3.14 * r * r

def checkprime(num):
    if num <= 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
