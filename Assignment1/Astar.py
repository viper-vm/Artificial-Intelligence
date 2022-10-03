
from queue import PriorityQueue             

# graph input 
GRAPH = {
            'Arad': {'Sibiu': 140, 'Zerind': 75, 'Timisoara': 118},
            'Zerind': {'Arad': 75, 'Oradea': 71},
            'Oradea': {'Zerind': 71, 'Sibiu': 151},
            'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
            'Timisoara': {'Arad': 118, 'Lugoj': 111},
            'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
            'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
            'Drobeta': {'Mehadia': 75, 'Craiova': 120},
            'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
            'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
            'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
            'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
            'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
            'Giurgiu': {'Bucharest': 90},
            'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
            'Hirsova': {'Urziceni': 98, 'Eforie': 86},
            'Eforie': {'Hirsova': 86},
            'Vaslui': {'Iasi': 92, 'Urziceni': 142},
            'Iasi': {'Vaslui': 92, 'Neamt': 87},
            'Neamt': {'Iasi': 87}
        }




def Astar(start, end):
    # Straight line heuristic 
    straight_line = {
                        'Arad': 366,
                        'Zerind': 374,
                        'Oradea': 380,
                        'Sibiu': 253,
                        'Timisoara': 329,
                        'Lugoj': 244,
                        'Mehadia': 241,
                        'Drobeta': 242,
                        'Craiova': 160,
                        'Rimnicu': 193,
                        'Fagaras': 176,
                        'Pitesti': 100,
                        'Bucharest': 0,
                        'Giurgiu': 77,
                        'Urziceni': 80,
                        'Hirsova': 151,
                        'Eforie': 161,
                        'Vaslui': 199,
                        'Iasi': 226,
                        'Neamt': 234
                    }
    #priority queue for Astar
    priority_queue = PriorityQueue()
    visited = {}
    priority_queue.put((straight_line[start], 0, start, [start]))
    visited[start] = straight_line[start]
    while (priority_queue.empty()== False):
        (total_cost, cost, vertex, path) = priority_queue.get()
        # finalcost = heuristic + cost
        individual_heuristic = total_cost - cost
        # print (total_cost, cost, individual_heuristic, path)
        if vertex == end:
            print("destination reached")
            print (total_cost, cost, individual_heuristic, path)
            return total_cost, cost, path
        for adjacent in GRAPH[vertex].keys():                      ## iterate/search for adjacent node
            current_cost = cost + GRAPH[vertex][adjacent]
            Heuristic = straight_line[adjacent]                    ## Heuristic of straight line
            total_cost = current_cost + straight_line[adjacent]
            if not adjacent in visited or visited[adjacent] >= total_cost:          ## astar condition
                visited[adjacent] = total_cost
                priority_queue.put((total_cost, current_cost, adjacent, path + [adjacent]))


start = "Arad"
end = "Bucharest"
heuristic, cost, optimal_path = Astar(start, end)

