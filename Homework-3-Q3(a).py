#Abhijeet Solanki
#T00221273
#Class: CSC-6220
#Date: 04/15/2024
#Homework#3-Q3(a) : The three clusters and their points after the first iteration of the K-means algorithm.

import numpy as np

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((np.array(point1) - np.array(point2))**2))

# Function to assign points to the closest center
def assign_to_centers(points, centers):
    clusters = {center: [] for center in centers}
    for point in points:
        distances = {center: euclidean_distance(point, centers[center]) for center in centers}
        closest_center = min(distances, key=distances.get)
        clusters[closest_center].append(point)
    return clusters

# Function to update the cluster centers
def update_centers(clusters):
    new_centers = {}
    for center in clusters:
        new_centers[center] = np.mean(clusters[center], axis=0) if clusters[center] else centers[center]
    return new_centers

points = np.array([[2, 10], [2, 5], [8, 4], [5, 8], [7, 5], [6, 4], [1, 2], [4, 9]])
centers = {'A1': np.array([2, 10]), 'B1': np.array([5, 8]), 'C1': np.array([1, 2])}

# Step 1: Assign each point to the nearest center
clusters = assign_to_centers(points, centers)

# Output the assignment of points to clusters
print("Assignment of points to the nearest cluster center:")
for center, assigned_points in clusters.items():
    print(f"Center {center}:")
    for point in assigned_points:
        print(f"Point {point} assigned to center {centers[center]}")
    print()

# Step 2: Calculate the new cluster centers after the first iteration
new_centers = update_centers(clusters)

# Output the new centers
print("New cluster centers after the first round of execution:")
for center, new_center in new_centers.items():
    print(f"Center {center} updated to new center at coordinates: {new_center}")
    print()
