'''

PROBLEM DESCRIPTION:

    1. Given an undirected graph
    2. Return TRUE if it's a Bipartite Graph otherwise FALSE

DEFINITION OF A BIPARTITE GRAPH:

    -> If a graph (undirected/directed) can be colored with two colors
       such that no adjacent nodes have the  same color then it is known as a Bipartite Graph

THOUGHT PROCESS:

    1. Recall, BFS traverse the graph level wise -> Implemented with visited array & Q
    2. Here, instead of visited array initialize a color array with -1 (-1=not colored yet)
    3. Start from source, color it, push it into the Q
    4. While Q is not empty keep traversing the adjacent nodes and color it if yet not colored
    5. If already colored, check if adj_node has the same color as parent
    6. If so -> Not a Bipartite Graph (Return FALSE)
    7. If the loop end means successfully colored the graph using 2 colors -> Return True (Bipartite)

TIME & SPACE COMPLEXITY:

    1. Time Complexity: O(V+E)
    2. Space Complexity: O(V)

NOTES:

    1. We consider a directed graph to be a bipartite graph if it's underlying undirected graph is a Bipartite Graph
    2. The graph might have multiple connected components
    3. A linear graph with no cycles/acyclic graph is always a Bipartite Graph 
       As I can always color it with two colors
    4. Any graph with even cycle length can also be a Bipartite Graph
    5. But graph with an odd cycle length can never be a Bipartite Graph
    6. For calculating TC & SC, i assumed graph is stored using adjacency list
       & considered only the required auxiliary space for the algorithm

'''



from collections import defaultdict, deque

def detect(graph, source, color):
    color[source] = 0
    q = deque()
    q.append(source)

    while q:
        node = q.popleft()
        for adj_ver in graph[node]:
            if (color[adj_ver] == -1):
                color[adj_ver] = not(color[node])
                q.append(adj_ver)
            elif (color[adj_ver] == color[node]):
                return False
    
    return True



def isBipartite(graph, n):
    color = [-1]*(n+1)

    for node in range(1, n+1):
        if (color[node] == -1):
            if(not(detect(graph, node, color))):
                return False
    
    return True



vertices, edges = map(int, input().split())
adjacency_list = defaultdict(list)
for edge in range(edges):
    u, v = map(int, input().split())
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

print(isBipartite(adjacency_list, vertices))