import math

# Loop
def euclidean(list points):

    cdef list  P1 = points[0]
    cdef list  P2 = points[1]
    cdef int L = len(points[0])

    # Find difference between each pair and square with itself
    diffs = [(P1[i] - P2[i]) ** 2 for i in range(L)]

    return math.sqrt(sum(diffs))


