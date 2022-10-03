

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



def DFS(GRAPH, start, end, path=[], visited=[]):

    path.append(start)
    visited.append(start)
    if (start==end):
        # return path
        print("Destination Reached")
        print(path)
    for (adjacent,w) in GRAPH[start]:
        if (adjacent not in visited):
            result = DFS(GRAPH,adjacent,end,path,visited)   # recursive dfs with start as adjacent
            # print(result)
            if result is not None:
                return result
    path.pop()
    return None

DFS(GRAPH,'Arad','Bucharest')