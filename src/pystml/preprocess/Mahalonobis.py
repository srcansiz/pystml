import math
import numpy as np
import matplotlib.pyplot as plt

from typing import Union
from scipy.stats import chi2
from matplotlib import patches
from itertools import combinations


'''
@center : If center is true it returns distance between each point and center
@point  : points is an array of two observation index. If points argument is presented
          center will be ignored
@rowvar : True if arrays' row represent each variable in dataset.
@oq     : For outlier detection, cutoff quantile according to two tail chi-sqaure distribution
'''


class Mahalanobis:

    def __init__(self,
                 data: Union[list, np.ndarray],
                 center: bool = True,
                 points: Union[list[float, float]] = None,
                 row_var: bool = False,
                 oq: float = 0.95):

        self.center = center
        self.points = points
        self.oq = oq

        if isinstance(data, list):
            self.data = np.array(data) if row_var is True else np.array(data).T
        elif isinstance(data, np.ndarray):
            self.data = data if row_var is False else data.T
        elif data.__class__ and data.__class__.__name__ == 'DataFrame':
            self.data = data if row_var is False else data.to_numpy().T
        else:
            raise ValueError('Data should be list, DataFrame or np.array.')

        self.cutoff = None
        self.covariance = np.cov(self.data, rowvar=False)
        self.centerpoint = np.mean(self.data, axis=0)
        self.distances = self.returnDistance()
        self.outliers = self.getOutliers()

    # Get distance between each point and center
    def getDistanceBEAC(self):
        distances = []
        covariance_pm1 = np.linalg.matrix_power(self.covariance, -1)
        for i, val in enumerate(self.data):
            p1 = val
            p2 = self.centerpoint
            distance = (p1 - p2).T.dot(covariance_pm1).dot(p1 - p2)
            distances.append(distance)

        return distances

    # Get distance between to points
    def getDistanceBTP(self):
        if len(self.points) == 2 and 0 <= self.points[0] < self.data.shape[0] and 0 <= self.points[0] < self.data.shape[
            0]:
            difference = self.data[self.points[0], :] - self.data[self.points[1], :]
            covariance_pm1 = np.linalg.matrix_power(self.covariance, -1)
            distance = difference.T.dot(covariance_pm1).dot(difference)
        else:
            raise ValueError('Data should be list or numpy array.')
        return distance

    # Returns distance based on given arguments
    def returnDistance(self):
        if self.points is None:
            return self.getDistanceBEAC()
        else:
            return self.getDistanceBTP()

    # Returns outliers by given quantile
    def getOutliers(self):

        # Two tail cutoff point according to given oq
        self.cutoff = chi2.ppf(self.oq, self.data.shape[1])
        outliers = [m for m, val in enumerate(self.distances) if val > self.cutoff]
        return outliers

    # Method for plotting data with mahalanobis.
    def plot(self):

        indexes = [m for m in range(self.data.shape[1])]
        comb = list(combinations(indexes, r=2))

        noc = len(comb)
        kk = np.sqrt(noc)
        fl = math.floor(kk)
        nc = fl + 1 if kk - fl != 0 else fl

        fig = plt.figure(figsize=(7, 7), facecolor='w', edgecolor='k')
        fig.suptitle('Distance cutoff and Scatter plots', fontsize=20)
        for i, cb in enumerate(comb):
            covariance = self.covariance[cb, :][:, cb]
            # Eigen vector and
            lambda_, v = np.linalg.eig(covariance)
            lambda_ = np.sqrt(lambda_)

            # Ellipse width and hieght
            width, height = lambda_[0] * np.sqrt(self.cutoff) * 2, lambda_[1] * np.sqrt(self.cutoff) * 2,

            # Angle of distribution
            angle = np.rad2deg(np.cos(v[0, 0])) if self.covariance[0, 1] <= 0 else np.rad2deg(np.arccos(v[0, 0]))

            # Ellipse patch
            ellipse = patches.Ellipse(xy=(self.centerpoint[0], self.centerpoint[1]),
                                      width=width, height=height, angle=angle, edgecolor='red')

            ellipse.set_facecolor('none')

            axs = plt.subplot(nc, nc, i + 1)
            axs.add_artist(ellipse)
            plt.title('Variables [' + ','.join([str(m) for m in cb]) + '] ')
            plt.scatter(self.data[:, cb[0]], self.data[:, cb[1]])
            plt.subplots_adjust(hspace=0.9, wspace=0.2)

        plt.show()
