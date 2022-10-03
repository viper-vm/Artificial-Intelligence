from queue import Queue

GRAPH = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Bucharest': [('Giurgiu', 90), ('Pitesti', 101), ('Fagaras', 211), ('Urziceni', 85)],
    'Craiova': [('Pitesti', 138), ('Dobreta', 120), ('Rimnicu Vilcea', 146)],
    'Dobreta': [('Craiova', 120), ('Mehadia', 75)],
    'Eforie': [('Hirsova', 86)],
    'Fagaras': [('Bucharest', 211), ('Sibiu', 99)],
    'Giurgiu': [('Bucharest', 90)],
    'Hirsova': [('Eforie', 86), ('Urziceni', 98)],
    'Iasi': [('Neamt', 87), ('Vaslui', 92)],
    'Lugoj': [('Mehadia', 70), ('Timisoara', 111)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Neamt': [('Iasi', 87)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Pitesti': [('Bucharest', 101), ('Craiova', 138), ('Rimnicu Vilcea', 97)],
    'Rimnicu Vilcea': [('Pitesti', 97), ('Craiova', 146), ('Sibiu', 80)],
    'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80), ('Arad', 140), ('Oradea', 151)],
    'Timisoara': [('Lugoj', 111), ('Arad', 118)],
    'Urziceni': [('Hirsova', 98), ('Bucharest', 85), ('Vaslui', 142)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Zerind': [('Oradea', 71), ('Arad', 75)]
}



def BFS(GRAPH, start, end):
    visited, path = [], []
    queue = Queue()

    queue.put(start)
    visited.append(start)

    parent = dict()                 ## parent to go back and forth at every child
    parent[start] = None

    while (queue.empty() == False):
        current_node = queue.get()
        if current_node == end:
            path.append(end)
            while parent[end] is not None:
                path.append(parent[end])
                end = parent[end]
            path.reverse()
            # return path
            print(path)
            # break

        for (adjacent, w) in GRAPH[current_node]:
            if adjacent not in visited:
                queue.put(adjacent)
                parent[adjacent] = current_node
                visited.append(adjacent)


BFS(GRAPH,'Arad','Bucharest')