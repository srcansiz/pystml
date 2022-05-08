import math
from pystml.stats.distances import euclidean as euc

# Loop
def euclidean(int [:,:] points):

    cdef int [:] P1 = points[0]
    cdef int [:] P2 = points[1]
    cdef int L = len(points[0])

    # Find difference between each pair and square with itself
    diffs = [(P1[i] - P2[i]) ** 2 for i in range(L)]

    return math.sqrt(sum(diffs))


# def loop_over_data(int data):
#     cdef int n, i, len_p
#
#     for row in enumerate(data):
#         for point in enumerate(data):

