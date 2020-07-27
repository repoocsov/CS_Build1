"""
K-means clustering
https://www.naftaliharris.com/blog/visualizing-k-means-clustering/
https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a

DBSCAN clustering
https://towardsdatascience.com/dbscan-clustering-explained-97556a2ad556

# ONLY ALLOWED TO USE NUMPY AND SCIPY

model, node, centroid
"""

from point import Point
from centroid import Centroid

class Kmeans:

    def __init__(self, k):
        self.k = k
        self.centroids = None # List of centroid objects


    def fit(self, data):
        # First assign centroids randomly
            # The initial  K centroids are randomly chosen from the dataset
            
        # Calculate which centroid each point belongs to
            # Need to calculate distance from each point to each centroid
            # The centroid/node distance that is the least is the centroid the point gets assigned to.
            # Probably save that to a list up above that will originially be initialized as None
        # Calculate new centroid by taking mean of points in that cluster
            # hmm...
        # Re-assign data points to the closest cluster center
            # repeat

        # Convergence happens when points are no longer reassigned to a different cluster
        pass
        

        
    def predict(self, X):
        # Loop through the fitted centroids and the one with the least distance is the assignment
        # return/print the centroid coordinates
        pass


if __name__ == '__main__':
    print('Hello world')
