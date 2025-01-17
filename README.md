# Day-17-Floyd-Warshall-Algorithm
Here's python Program for Floyd Warshall Algorithm. Day 17 of Day 365.
- Initial Setup: Start with a graph represented as nodes (vertices) and edges with weights. Create a distance matrix `dist` where `dist[i][j]` is the weight of the edge from vertex `i` to vertex `j`. If there is no edge between vertices, set the distance to infinity (`INF`). The distance from a vertex to itself is zero.
- Algorithm Execution: Use three nested loops to iterate through each vertex as an intermediate vertex:
  - For each pair of vertices `(i, j)`, update the distance `dist[i][j]` to be the minimum of the current distance `dist[i][j]` and the sum of the distances `dist[i][k]` and `dist[k][j]`, where `k` is the intermediate vertex.
- Completion: Continue the process until all pairs of vertices have been considered with every vertex as an intermediate vertex.

Here's a visual representation using an example graph with 4 vertices (A, B, C, D):

Graph:

```
    A       B       C       D
A   0       ∞       ∞       ∞
B   ∞       0       3       ∞
C   ∞       ∞       0       1
D   ∞       ∞       ∞       0
```

Edges:
- (A, B) = 1
- (B, C) = 3
- (C, D) = 1
- (A, D) = 10

1. Initial Distance Matrix:

```
    A   B   C   D
A   0   1  ∞   10
B   ∞   0   3   ∞
C   ∞  ∞   0   1
D   ∞  ∞   ∞   0
```

2. Intermediate Vertex: A

```
    A   B   C   D
A   0   1  ∞   10
B   ∞   0   3   ∞
C   ∞  ∞   0   1
D   ∞  ∞   ∞   0
```

3. Intermediate Vertex: B

```
    A   B   C   D
A   0   1   4   10
B   ∞   0   3   ∞
C   ∞  ∞   0   1
D   ∞  ∞   ∞   0
```

4. Intermediate Vertex: C

```
    A   B   C   D
A   0   1   4   5
B   ∞   0   3   4
C   ∞  ∞   0   1
D   ∞  ∞   ∞   0
```

5. Intermediate Vertex: D

```
    A   B   C   D
A   0   1   4   5
B   ∞   0   3   4
C   ∞  ∞   0   1
D   ∞  ∞   ∞   0
```

Final Distance Matrix:

```
    A   B   C   D
A   0   1   4   5
B   ∞   0   3   4
C   ∞  ∞   0   1
D   ∞  ∞   ∞   0
```
