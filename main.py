import math

# Define a list of points in 2D space as tuples (x, y)
points = [(1, 2), (4, 6), (7, 8), (2, 3), (5, 9)]  # Example points, modify as needed

# Function to calculate Euclidean distance between two points
def euclideanDistance(point1, point2):
    """
    Calculate the Euclidean distance between two points in 2D space.
    
    Parameters:
    point1 (tuple): The first point as (x, y)
    point2 (tuple): The second point as (x, y)
    
    Returns:
    float: The Euclidean distance between point1 and point2
    """
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Calculate distances between each pair of points
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Find the minimum distance
min_distance = min(distances)

# Display the result
print("The minimum distance between any two points is:", min_distance)
