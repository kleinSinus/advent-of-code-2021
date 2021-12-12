# import lib

from os import pathsep


def do_stuff(input_data, test_mode):
    cave_system = [line.split('-') for line in input_data]
    caves = {}
    for link in cave_system:
        if link[0] not in caves:
            caves[link[0]] = []
        caves[link[0]].append(link[1])
        if link[1] not in caves:
            caves[link[1]] = []
        caves[link[1]].append(link[0])
    # for k in caves.keys():
    #     print(k, " -> ", caves[k])
    paths = paths_to_end("start", False, [], False, caves)
    # for path in paths:
    #     output_text += str(path[::-1]) + "\n"
    output_text = "There are " + str(len(paths)) + " paths through the given cave system."
    return output_text

def paths_to_end(node, recursive_call, visited_small_nodes, double_visit, neighbors):
    # print(node, ", ", recursive_call, ", ", visited_small_nodes)
    if node == "end": # at the end
        return [["end"]]
    if node == "start" and recursive_call: # start is being traversed somewhere in the middle
        return []
    if node in visited_small_nodes and double_visit: # some small node is being traversed after a small node was already traversed twice
        return []
    if node in visited_small_nodes and not double_visit: # some small node is being traversed after a small node was already traversed twice
        double_visit = True
    if node == node.lower(): # some small node is visited
        visited_small_nodes.append(node)
    paths = []
    for neighbor in neighbors[node]:
        paths_from_neighbor = paths_to_end(neighbor, True, visited_small_nodes.copy(), double_visit, neighbors)
        for path in paths_from_neighbor:
            path.append(node)
            paths.append(path)
    return paths