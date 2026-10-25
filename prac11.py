# Group D - Practical 1: BFS and DFS Traversal

 

def bfs(graph, start):

    visited = [start]

    queue = [start]

    while queue:

        node = queue.pop(0)

        for neighbour in graph[node]:

            if neighbour not in visited:

                visited.append(neighbour)

                queue.append(neighbour)

    return visited

 

 

def dfs(graph, start, visited=None):

    if visited is None:

        visited = []

    visited.append(start)

    for neighbour in graph[start]:

        if neighbour not in visited:

            dfs(graph, neighbour, visited)

    return visited

 

 

try:

    n = int(input('Enter number of vertices: '))

    if n <= 0:

        print('Number of vertices must be positive.')

    else:

        graph = {i: [] for i in range(n)}

        e = int(input('Enter number of edges: '))

        if e < 0:

            print('Number of edges cannot be negative.')

        else:

            for i in range(e):

                u, v = map(int, input('Enter edge (u v): ').split())

                if u not in graph or v not in graph:

                    print('Invalid vertex in edge. Try again.')

                    continue

                if v not in graph[u]:

                    graph[u].append(v)

                if u not in graph[v]:

                    graph[v].append(u)

            start = int(input('Enter starting vertex: '))

            if start not in graph:

                print('Invalid starting vertex.')

            else:

                print('BFS:', *bfs(graph, start))

                print('DFS:', *dfs(graph, start))

except ValueError:

    print('Invalid input. Enter numbers in the required format.')