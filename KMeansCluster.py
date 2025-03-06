import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate sample data (2D points)
X = np.array([
    [1, 2], [2, 3], [3, 2], [8, 7], [8, 8], [7, 8], [1, 0], [2, 1], [3, 1]
])

# Create K-Means model (3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Get cluster labels and centroids
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o', edgecolor='k', s=100)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.legend()
plt.show()
