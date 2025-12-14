'''

PROBLEM DESCRIPTION:

    1. You are given an undirected graph
    2. You have to print a valid BFS traversal order starting from a source

THOUGHT PROCESS:

    1. BFS (Breadth-First Search) traverse the graph level-wise (Level-Order Traversal)
    2. BFS visits all adjacent nodes of source before visiting neighboring nodes to the adjacent nodes
    3. So, nodes with the same distance from the source are visited before the nodes that are further
       away from the source nodes
    4. BFS is basically implemented with a QUEUE (As it follows FIFO principal) & visited array
    5. First, put the source node into the Q and mark it as visited
    6. Then, for each node from the Q, print it and append the unvisited adjacent nodes into the Q
    7. Continue as long as the Q is not empty

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. BFS works for both directed & undirected graph
    2. There can be multiple valid BFS traversal order
    3. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm

'''



from collections import defaultdict, deque

def bfs(graph, source, visited):
    visited[source] = 1
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        print(node, end=" ")
        for adj_node in graph[node]:
            if (not(visited[adj_node])):
                visited[adj_node] = 1
                q.append(adj_node)



def traversal(graph, n):
    visited = [0]*(n+1)

    for node in range(1, n+1):
        if (not(visited[node])):
            bfs(graph, node, visited)



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

traversal(adjacency_list, vertices)
print()