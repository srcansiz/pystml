import math
from .mahalanobis import Mahalanobis
from ._distances import euclidean as _euclidean

# Reference : https://en.wikipedia.org/wiki/Euclidean_distance
def euclidean(points):
    nested = all(isinstance(i, list) or i.__class__.__name__ in ['ndarray', 'Series'] for i in points)
    if nested is False or len(points) > 2:
        raise ValueError(
            'Points should be presented in nested list, pd.Series or np.array. For example: [[a,b,c],[x,z,y]]')

    lengths = [len(k) > 1 for k in points]
    if all(lengths) is not True:
        raise ValueError(
            'Point coordinates does not matched, they should be matched for example: [[a,b,c],[x,z,y]]')

    return _euclidean(points)


# Reference : https://en.wikipedia.org/wiki/Taxicab_geometry
def manhattan(points):
    nested = all(isinstance(i, list) or i.__class__.__name__ in ['ndarray', 'Series'] for i in points)
    if nested is False or len(points) > 2:
        raise ValueError(
            'Points should be presented in nested list, pd.Series or np.array. For example: [[a,b,c],[x,z,y]]')

    lengths = [len(k) > 1 for k in points]
    if all(lengths) is not True:
        raise ValueError(
            'Point coordinates does not matched, they should be matched for example: [[a,b,c],[x,z,y]]')

    P1 = points[0]
    P2 = points[1]
    L = len(points[0])

    # Find difference between each pairs and square with it self
    diffs = [abs(P1[i] - P2[i]) for i in range(L)]

    return sum(diffs)


# Reference : https://en.wikipedia.org/wiki/Minkowski_distance
def minkowski(points, p=2 ** -1):
    nested = all(isinstance(i, list) or i.__class__.__name__ in ['ndarray', 'Series'] for i in points)
    if nested is False or len(points) > 2:
        raise ValueError(
            'Points should be presented in nested list, pd.Series or np.array. For example: [[a,b,c],[x,z,y]]')

    lengths = [len(k) > 1 for k in points]
    if all(lengths) is not True:
        raise ValueError(
            'Point coordinates does not matched, they should be matched for example: [[a,b,c],[x,z,y]]')

    P1 = points[0]
    P2 = points[1]
    L = len(points[0])

    dists = [abs(P1[i] - P2[i]) ** p for i in range(L)]

    return sum(dists) ** (1 / p)
