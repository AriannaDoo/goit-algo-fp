import uuid
import time
from collections import deque

import networkx as nx
import matplotlib.pyplot as plt


# ---------- Node class (из задания 4) ----------
class Node:
    def __init__(self, key, color="#1a1a1a"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


# ---------- Tree drawing logic (из задания 4) ----------
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)

        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)

        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

    return graph


def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(
        tree,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
        font_size=10,
    )
    plt.show(block=True)


# ---------- Color generator ----------
def generate_colors(n):
    colors = []
    for i in range(n):
        intensity = int(40 + (215 * i / max(1, n - 1)))
        hex_color = f"#{intensity:02x}{intensity:02x}ff"
        colors.append(hex_color)
    return colors


# ---------- DFS (stack) ----------
def dfs_visualization(root):
    stack = [root]
    visited = []
    colors = generate_colors(10)

    step = 0
    while stack:
        node = stack.pop()
        node.color = colors[min(step, len(colors) - 1)]
        visited.append(node)

        draw_tree(root, f"DFS traversal — step {step + 1}")
        time.sleep(0.7)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        step += 1


# ---------- BFS (queue) ----------
def bfs_visualization(root):
    queue = deque([root])
    colors = generate_colors(10)

    step = 0
    while queue:
        node = queue.popleft()
        node.color = colors[min(step, len(colors) - 1)]

        draw_tree(root, f"BFS traversal — step {step + 1}")
        time.sleep(0.7)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        step += 1


# ---------- Build example tree ----------
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


# ---------- Run visualizations ----------
print("DFS visualization started")
dfs_visualization(root)

# reset colors
for n in [root, root.left, root.left.left, root.left.right, root.right, root.right.left]:
    n.color = "#1a1a1a"

print("BFS visualization started")
bfs_visualization(root)
