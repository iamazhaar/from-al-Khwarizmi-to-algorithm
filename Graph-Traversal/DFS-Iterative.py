'''

PROBLEM DESCRIPTION:

    1. You are given an undirected graph
    2. You have to print a valid DFS traversal order starting from a source

THOUGHT PROCESS:

    1. DFS keeps exploring a path until it finds a DEAD END
    2. When we can't go anywhere from a node -> DEAD END
    3. A node doesn't have any unvisited adjacent nodes -> DEAD END
    4. So, in DFS the distance from the source increases with each iteration
    5. Iterative DFS is implemented with the help of STACK (As it follows LIFO principal) & visited array
    6. First, put the source node into the Stack and mark it as visited
    7. Then, for each node from the Stack, print it and append the unvisited adjacent nodes into the Stack
    8. Continue as long as the Stack is not empty

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. DFS works for both directed & undirected graph
    2. There can be multiple valid DFS traversal order
    3. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm
    4. Assumed the graph might have multiple connected components

'''



from collections import defaultdict, deque

def iterative_dfs(graph, source, visited):
    visited[source] = 1
    stack = deque()
    stack.append(source)

    while stack:
        node = stack.pop()
        print(node, end=" ")
        for adj_node in graph[node]:
            if (not(visited[adj_node])):
                visited[adj_node] = 1
                stack.append(adj_node)



def traversal(graph, n):
    visited = [0]*(n+1)

    for node in range(1, n+1):
        if (not(visited[node])):
            iterative_dfs(graph, node, visited)



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

traversal(adjacency_list, vertices)
print()