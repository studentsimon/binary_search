#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.
    HINT: 
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.
    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    length = len(xs) #list length
    middle = length//2 #split

    if length == 0:
        return None

    elif xs[middle] < 0:
        if length == 1:
            return None
        else:
            f1 = find_smallest_positive(xs[middle+1:])
            if f1 == None:
                return None
            else:
                return f1+middle+1
    elif xs[middle] == 0:
         return middle + 1
    else:
        if length == 1:
            return 0
        else:
            if find_smallest_positive(xs[:middle])==None:
                return middle
            else:
                return find_smallest_positive(xs[:middle])
    

def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.
    HINT: 
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

        finder([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.
    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([1, 2, 3], 4)
    0
    '''
    if len(xs) == 0:
        return 0
    

    x1 = finder(xs, x)
    x2 = finder2(xs, x)

    if(x1 == -1 or x2 == -1):
        return 0
    
    return (x1-x2 + 1)

def finder(xs, x):

    if xs[len(xs)-1] == x:
        return len(xs)-1

    
    left = 0
    right = len(xs)-1
    while left<=right:
        mid = (left+right)//2
       
        if x > xs[mid]:
            right = mid-1
        if x < xs[mid]:
            left = mid+1
        if x == xs[mid]:
            
            if xs[mid+1] < x:
                return mid
            else:
                
                left = mid + 1
    
    return -1


def finder2(xs, x):

    if xs[0] == x:
        return 0
    
    left = 0
    right = len(xs)-1
    while left<=right:
        mid = (left+right)//2
        
        if x > xs[mid]:
            right = mid-1
        if x < xs[mid]:
            left = mid+1
        if x == xs[mid]:
            
            if xs[mid-1] > x:
                return mid
            else:
                
                right = mid - 1
    
    return -1

def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]
    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest, 
               you recursively call your function on the interval [lo,m2] or [m1,hi]
    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''
    l = lo
    r = hi

    def go(l, r):
        m1 = l + (r - l)/8
        m2 = r - (r - l)/4
        if r - l < epsilon:
            return r
        if f(m1)<f(m2):
            return go(l, m2)
        if f(m1)>f(m2):
            return go(m1, r)
    return go(l, r)
    
    

