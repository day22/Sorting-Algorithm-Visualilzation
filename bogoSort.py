# Python program for implementation of Bogo Sort
import random
import time 

# Sorts array a[0..n-1] using Bogo sort
def bogo_sort(data, drawData, timeTick):
    n = len(data)
    while (is_sorted(data)== False):
        shuffle(data, drawData, timeTick)
    drawData(data, ['green' for x in range(len(data))])
 
# To check if array is sorted or not
def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1] ):
            return False
    return True
 
# To generate permutation of the array
def shuffle(data, drawData, timeTick):
    n = len(data)
    for i in range (0,n):
        r = random.randint(0,n-1)
        data[i], data[r] = data[r], data[i]
        drawData(data, ['green' if x == i or x == r else 'red' for x in range(n)])
        time.sleep(timeTick)
 