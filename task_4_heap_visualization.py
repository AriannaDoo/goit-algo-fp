import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap, index=0):
    """Створює бінарне дерево з масиву-купи"""
    if index >= len(heap):
        return None

    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, label=node.val, color=node.color)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, l, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, r, y - 1, layer + 1)
    return graph


def draw_tree(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)

    colors = [n[1]["color"] for n in tree.nodes(data=True)]
    labels = {n[0]: n[1]["label"] for n in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos, labels=labels, node_color=colors, node_size=2500, arrows=False)
    plt.show()


# Приклад купи
heap = [1, 3, 5, 7, 9, 11, 13]

root = build_heap_tree(heap)
draw_tree(root)
