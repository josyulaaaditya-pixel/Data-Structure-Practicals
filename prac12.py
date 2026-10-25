# Group D - Practical 2: Pizza Delivery (Minimum Time)

# Dijkstra's algorithm using basic Python only

 

n = int(input('Enter number of locations: '))

if n <= 0:

    print('Number of locations must be positive.')

else:

    names = []

    for i in range(n):

        names.append(input('Enter location ' + str(i + 1) + ': '))

 

    graph = [[0] * n for _ in range(n)]

    e = int(input('Enter number of roads: '))

    for i in range(e):

        print('Road', i + 1)

        a = int(input('From location number: ')) - 1

        b = int(input('To location number: ')) - 1

        time = int(input('Travel time (minutes): '))

        if 0 <= a < n and 0 <= b < n and a != b and time > 0:

            graph[a][b] = time

            graph[b][a] = time

        else:

            print('Invalid road; skipped.')

 

    start = int(input('Pizza shop location number: ')) - 1

    if not 0 <= start < n:

        print('Invalid pizza shop location.')

    else:

        distance = [float('inf')] * n

        visited = [False] * n

        previous = [-1] * n

        distance[start] = 0

 

        for _ in range(n):

            u = -1

            for i in range(n):

                if not visited[i] and (u == -1 or distance[i] < distance[u]):

                    u = i

            if u == -1 or distance[u] == float('inf'):

                break

            visited[u] = True

            for v in range(n):

                if graph[u][v] > 0 and not visited[v]:

                    new_time = distance[u] + graph[u][v]

                    if new_time < distance[v]:

                        distance[v] = new_time

                        previous[v] = u

 

        print('\nMinimum delivery times from', names[start])

        for i in range(n):

            if distance[i] == float('inf'):

                print(names[i] + ': No route available')

            else:

                path = []

                current = i

                while current != -1:

                    path.insert(0, names[current])

                    current = previous[current]

                print(names[i] + ':', distance[i], 'minutes | Route:', ' -> '.join(path))

