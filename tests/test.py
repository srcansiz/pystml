import numpy as np
import pandas as pd
from pystml.stats import stats
from pystml.stats import LOF
from pystml.stats import distances
from scipy.spatial.distance import minkowski, cityblock, euclidean

rlt = [1,2,3,4, None]
mm = stats.mean(np.array(rlt), rmna=False)

std = stats.std(rlt)

'''
gh = [
     np.array([1,2,3,4]),
     np.array([1,2,3,4])
 ]
'''
pddf = pd.DataFrame([ [13,24,45],
                      [13,15, 56],
                      [12,32, 33],
                      [67,34, 45]],  columns=['X', 'Y', 'Z'])

print(pddf.iloc[1])
fg = [pddf.iloc[1] , pddf.iloc[0]]
gh = [
     [1,2,3,4],
     [10,3,4,16]
 ]


l = LOF.LOF(gh)


print('Euclid')
print(distances.euclidean(fg))
print('Manhattan')
print(distances.manhattan(fg))
print('Minkowski')
print(distances.minkowski(fg, 2**4))

print(minkowski(fg[0], fg[1], 2**4))
print(cityblock(fg[0], fg[1]))
print(euclidean(fg[0], fg[1]))


print(std)
print(mm)



## Creating numpy array
x = np.array([
    [5, 1, 2, 3, 2, 4, 2, 5, 6, 5, 4, 3, 2, 10, 8, 9, 15, 5, 10],
    [10, 2, 2, 3, 1, 6, 3, 4, 7, 6, 3, 4, 2, 9, 10, 9, 14, 14, 2],
    [9, 2, 2, 3, 1, 6, 3, 10, 7, 6, 1, 4, 14, 9, 10, 9, 14, 14, 2],
    [9, 2, 2, 3, 123, 6, 3, 10, 5, 6, 1, 4, 2, 9, 10, 9, 14, 14, 2],
    [9, 2, 2, 3, 14, 6, 3, 10, 7, 6, 1, 4, 2, 9, 10, 9, 14, 14, 2],
    [9, 2, 2, 3, 1, 6, 3, 16, 7, 6, 1, 4, 2, 9, 10, 9, 14, 14, 2]
])

distance = distances.Mahalanobis(x, rowvar=True)
print(distance.distances)
print(distance.centerpoint)
print(distance.outliers)
# Plot data to find outliers
distance.plot()
