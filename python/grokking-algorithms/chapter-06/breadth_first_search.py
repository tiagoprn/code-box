"""
Breadth-first search is an algorithm to find
the shortest distance between 2 nodes.

Given a graph (that must be represented by a dict),
finds the closest (first) person which is a seller.
"""
from collections import deque


def person_is_seller(person):
    return person.endswith('m')


def search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []  # keep track of people searched before
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            print('-' * 20)
            print(f'Searching {person}...')
            if person_is_seller(person):
                print(f'Person {person} is a seller!')
                return True
            search_queue += graph[person]
            searched.append(person)
            print(f'Searched {person}.')
    return False


def get_graph() -> dict:
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'johnny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['johnny'] = []
    return graph


def main():
    graph = get_graph()
    search(graph, 'you')


if __name__ == '__main__':
    main()
