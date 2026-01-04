from collections import deque


def generate_color(step, total):
    intensity = int(255 * step / total)
    return f"#{intensity:02x}{100:02x}{255-intensity:02x}"


def dfs_visual(root):
    stack = [root]
    visited = []
    order = 0

    while stack:
        node = stack.pop()
        visited.append(node)
        node.color = generate_color(order, 10)
        order += 1

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited


def bfs_visual(root):
    queue = deque([root])
    visited = []
    order = 0

    while queue:
        node = queue.popleft()
        visited.append(node)
        node.color = generate_color(order, 10)
        order += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited
