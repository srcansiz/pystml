"""
 Parameters ------------------------------------------------------------
    "array" :
    "rmna"  : If true average will be calculated by removing None values,
              otherwise None values will be count as zero
    "pmknown": If population mean is known

"""
import math


# Mean function
def mean(array, rmna=True):
    if None in array:
        arr = [k for k in array if k is not None]
    else:
        arr = array
    L = len(arr) if rmna is True else len(array)
    p = sum(arr)
    return p / L


# Standard deviation
def std(array, rmna=True, pmkown=False):

    avg = mean(array, rmna=rmna)

    if None in array:
        arr = [k for k in array if k is not None]
    else:
        arr = array

    L = len(arr) if rmna is True else len(array)
    difSqrt = [(k - avg) ** 2 for k in arr]
    sumDifSqrt = sum(difSqrt)
    div = sumDifSqrt / (L - 1) if pmkown is False else sumDifSqrt / L

    return math.sqrt(div)

# Covariance
#def cov(matrix , byrow=False, pmkwown=False):


