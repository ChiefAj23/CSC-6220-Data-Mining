#Abhijeet Solanki
#T00221273
#Class: CSC-6220
#Date: 04/15/2024
#Homework#3-Q3(b) : The final three clusters
import numpy as np
from itertools import combinations


points_with_labels = {
    'A1': np.array([2, 10]),
    'A2': np.array([2, 5]),
    'A3': np.array([8, 4]),
    'B1': np.array([5, 8]),
    'B2': np.array([7, 5]),
    'B3': np.array([6, 4]),
    'C1': np.array([1, 2]),
    'C2': np.array([4, 9])
}

initial_centers_with_labels = {
    'A1': points_with_labels['A1'],
    'B1': points_with_labels['B1'],
    'C1': points_with_labels['C1']
}


points = np.array(list(points_with_labels.values()))
initial_centers = np.array(list(initial_centers_with_labels.values()))

# Function to calculate Euclidean distance
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

# Function to assign points to the nearest center
def assign_points_to_centers(points, centers):
    clusters = {}
    for idx, point in enumerate(points):
        distances = [euclidean_distance(point, center) for center in centers]
        nearest_center_idx = np.argmin(distances)
        if nearest_center_idx not in clusters:
            clusters[nearest_center_idx] = []
        clusters[nearest_center_idx].append(point)
    return clusters

# Function to calculate new centers from clusters
def calculate_new_centers(clusters):
    new_centers = []
    for points in clusters.values():
        new_centers.append(np.mean(points, axis=0))
    return np.array(new_centers)

# Function to iterate the k-means process until convergence
def k_means_iterate(points, current_centers):
    previous_centers = np.zeros(current_centers.shape)
    while not np.allclose(current_centers, previous_centers):
        clusters = assign_points_to_centers(points, current_centers)
        previous_centers = current_centers
        current_centers = calculate_new_centers(clusters)
    return clusters, current_centers

# Run the k-means algorithm until convergence
final_clusters, final_centers = k_means_iterate(points, initial_centers)

# Map the final clusters back to the original labels
final_clusters_with_labels = {}
for cluster_idx, points_in_cluster in final_clusters.items():
    labels = [label for label, point in points_with_labels.items() if any(np.array_equal(point, cluster_point) for cluster_point in points_in_cluster)]
    final_clusters_with_labels[cluster_idx] = labels

# Convert final centers to a list of tuples for better readability
final_centers_tuples = [tuple(center) for center in final_centers]

# Printing the result
print("Final clusters after k-means convergence:")
for cluster_idx, labels in final_clusters_with_labels.items():
    print(f"Cluster {cluster_idx+1}: contains points {labels}")
    print(f"Center of Cluster {cluster_idx+1}: {final_centers_tuples[cluster_idx]}")
    print("\n" + "-"*60 + "\n")
