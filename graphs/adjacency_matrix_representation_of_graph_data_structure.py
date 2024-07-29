"""
In this method, the graph is stored in the form of the 2D matrix where rows and columns denote vertices.
Each entry in the matrix represents the weight of the edge between those vertices.
"""


def create_adjacency_matrix(graph):
    # Get the number of vertices in the graph
    num_vertices = len(graph)

    # Initialize the adjacency matrix with zeros
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Fill the adjacency matrix based on the edges in the graph
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                adj_matrix[i][j] = 1
                # For undirected graph, set symmetric entries
                adj_matrix[j][i] = 1

    return adj_matrix


# The indices represent the vertices, and the values are lists of neighboring vertices
graph = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

# Create the adjacency matrix
adj_matrix = create_adjacency_matrix(graph)

# Print the adjacency matrix
for row in adj_matrix:
    print(' '.join(map(str, row)))
