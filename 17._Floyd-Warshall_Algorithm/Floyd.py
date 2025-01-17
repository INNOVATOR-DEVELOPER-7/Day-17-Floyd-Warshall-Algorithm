def floyd_warshall(graph):
    num_vertices = len(graph)
    # Initialize distance matrix with given graph distances
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))

    # Implementing Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    return distance

# Get the number of vertices from the user
num_vertices = int(input("Enter the number of vertices: "))

# Initialize the graph as an adjacency matrix
print("Enter the adjacency matrix (use 'inf' for infinity):")
graph = []
for i in range(num_vertices):
    row = input().split()
    row = [float(x) if x != 'inf' else float('inf') for x in row]
    graph.append(row)

# Perform Floyd-Warshall algorithm
distances = floyd_warshall(graph)

# Print the shortest distances between every pair of vertices
print("Shortest distances between every pair of vertices:")
for row in distances:
    print(" ".join(map(str, row)))
