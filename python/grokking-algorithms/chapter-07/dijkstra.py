"""
The graph used on this example is at the file "definition.png".

In the implementation, we will need 3 hash tables: graph, costs and parents.
The graph hash table has the input data, and the costs and parents
hash tables will be updated as the algorithm progresses.
"""
from pprint import pprint


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def main():
    # TODO: adapt this algorithm to work with any input

    graph = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2
    # to get all the neighbors for start: graph['start'].keys()

    graph["a"] = {}
    graph["a"]["end"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["end"] = 5

    graph["end"] = {}  # the finish node does not have neightbors

    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["end"] = infinity

    parents = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["end"] = None

    processed = []  # all the nodes that were already processed

    node = find_lowest_cost_node(costs, processed)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    print("\nGRAPH HASH TABLE:")
    pprint(graph, width=1)

    print("\nFINAL PARENTS HASH TABLE:")
    pprint(parents, width=1)

    print("\nFINAL COSTS HASH TABLE:")
    pprint(costs, width=1)


if __name__ == "__main__":
    main()
