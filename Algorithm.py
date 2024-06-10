import heapq

def dijkstra(graph, start, end):
   
    distances = {node: float('inf') for node in graph}
   
    distances[start] = 0
    
    priority_queue = [(0, start)]
   
    previous_nodes = {node: None for node in graph}

    while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

    
        if current_distance > distances[current_node]:
            continue

        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    path = path[::-1] 

    return distances[end], path


graph = {
    'DBN': [('PMB', 89), ('RBY', 112)],
    'PMB': [('DBN', 89), ('HMT', 209), ('RBY', 70)],
    'RBY': [('DBN', 112), ('PMB', 70), ('HMT', 100), ('VRT', 106)],
    'RBY': [('DBN', 112), ('PMB', 70), ('HMT', 100), ('VRT', 106)],
    'HMT': [('PMB', 209), ('RBY', 100), ('VRT', 41), ('JHB', 210)],
    'VRT': [('RBY', 106), ('HMT', 41), ('JHB', 106)],
    'JHB': [('HMT', 210), ('VRT', 106)]
}


start_node = 'DBN'
end_node = 'JHB'

# Calculate the shortest path and distance
shortest_distance, path = dijkstra(graph, start_node, end_node)

# Print the result
print(f"The shortest path from {start_node} to {end_node} is {path} with a total cost of {shortest_distance}")
