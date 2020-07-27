"""
K-means clustering
https://www.naftaliharris.com/blog/visualizing-k-means-clustering/
https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a

DBSCAN clustering
https://towardsdatascience.com/dbscan-clustering-explained-97556a2ad556

# ONLY ALLOWED TO USE NUMPY AND SCIPY

model, node, centroid
"""

import numpy as np
from scipy.spatial import distance
from point import Point
from centroid import Centroid

class Model:

    def __init__(self, k):
        # Number of centroids & clusters based on the k value given 
        self.k = k
        self.points = None
        self.centroids = [] # List of centroid objects


    def fit(self, data):
        # Create a point object for each point and save to points list
        self.points = [Point(x) for x in data]

        # Get three random indices to make as the k starting centroids
        random_indices = np.random.randint(0, len(data), self.k)

        # Create these centroids
        for index in random_indices:
            centroid = Centroid(data[index])
            self.centroids.append(centroid)
            
        # Calculate which centroid each point belongs to
        for point in self.points:
            distances = []
            for centroid in self.centroids:
                dst = distance.euclidean(point.coordinates, centroid.coordinates)
                distances.append(dst)

            centroid_index = distances.index(min(distances))
            point.assigned_centroid = self.centroids[centroid_index]
        
        # Calculate new centroid by taking mean of points in that cluster
        for centroid in self.centroids:
            points = []
            for point in self.points:
                if point.assigned_centroid is centroid:
                    points.append(point.coordinates)
            # Updating centroid coordinates
            centroid = np.mean(points, axis=0)
            
        # Re-assign data points to the closest cluster center
        

        # Convergence happens when points are no longer reassigned to a different cluster
        pass
        

    def predict(self, X):
        # Loop through the fitted centroids and the one with the least distance is the assignment
        # return/print the centroid coordinates
        pass

    def test_function():
        return self.centroids



if __name__ == '__main__':
    print('Hello world')

    test_data = [[1.1, 7.8], [6, 5], [4, 2], [4, 1], [1.1, 9], [9, 7.8], [10, 7.8], [15, 7.8], [16, 3], [22, 4.2], [17, 2], [19, 9], [10, 2], [2, 4], [5, 19]]

    model = Model(2)
    model.fit(test_data)
    for point in model.points:
        print('POINT COORDS', point.coordinates)
        print('CENTROID COORDS', point.assigned_centroid.coordinates)
        print('--------------------')