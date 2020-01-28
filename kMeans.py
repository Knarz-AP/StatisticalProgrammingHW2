# Assignment Information
print("Data 51100- Spring 2020")
print("Alec Peterson, Juma Hamdan, Lovy George")
print("Programming Assignment #2")

# Ask user for number of clusters (k)
k = int(input("Enter the number of clusters: "))

# Grab data from file specified
data = [float(x.rstrip()) for x in open("prog2-input-data.txt")]

# Create variables to store centroids, clusters, and point assignments.
centroids = dict(zip(range(k), data[0:k]))
clusters = dict(zip(range(k), [[] for i in range(k)]))
# Create and initialize a dict mapping points to clusters
point_assignments = dict(zip(range(k), clusters))
# Create a variable to store old point assignments (from previous iteration)
old_point_assignments = dict()


# Define function to assign points to clusters, place each point in closest cluster
def assign_to_clusters(data, clusters, centroids, point_assignments):
    for key, point in enumerate(data):
        closest_index = float('inf')  # Setting an arbitrarily large value to start comparisons
        index = 0
        for i in range(len(centroids)):
            distance = (abs(point - centroids[i]))
            if distance < closest_index:
                closest_index = distance
                index = i
        clusters[index].append(point)
        point_assignments[index] = closest_index
    return point_assignments


# Define function to update location of points
def update_location(data, clusters, centroids):
    new_centroids = {k: sum(value) / float(len(value)) for k, value in clusters.items()}
    centroids.update(new_centroids)
    return centroids


point_assignments = assign_to_clusters(data, clusters, centroids, point_assignments)
oldpoints = dict(old_point_assignments)  # Set a baseline for where we store old points, right now its empty

# Set count to keep track of total iterations, and while loop to run iterations until complete
count = 0
while point_assignments != oldpoints:  # Loop until points no longer change
    count += 1
    print("Iteration", count)  # Print each iteration and clusters as they are calculated
    for tag, objects in clusters.items():
        print(tag, '', objects) # Print cluster tag and cluster objects
    new_centroids = update_location(data, clusters, centroids)
    old_point_assignments = point_assignments  # Assigning values to old_point_assignments we set up before
    oldpoints = dict(old_point_assignments)  # Set point assignments to oldpoints
    clusters = dict(zip(range(k), [[] for i in range(k)]))  # Updating clusters
    point_assignments = assign_to_clusters(data, clusters, new_centroids, point_assignments)

# Generate output file and end program
with open("prog2-output-data.txt", 'w') as f:
    for c, p in clusters.items():
        for points in p:
            f.write("Point " + str(points) + " in Cluster " + str(c) + "\n")
f.close()
