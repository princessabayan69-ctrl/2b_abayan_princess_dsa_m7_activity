class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create the tree
root = Node(15)

root.left = Node(10)
root.right = Node(25)

root.left.left = Node(4)
root.left.right = Node(12)

root.right.left = Node(20)
root.right.right = Node(30)

root.left.left.left = Node(2)
root.left.left.right = Node(6)


# Calculate the total number of nodes
def size(node):
    if node is None:
        return 0

    return 1 + size(node.left) + size(node.right)


# Calculate the height of the tree
def height(node):
    if node is None:
        return -1

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)


# Calculate size without recursion
def iterative_size(root):
    if root is None:
        return 0

    queue = [root]
    count = 0

    while queue:
        node = queue.pop(0)
        count += 1

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return count


# Display results
print("Size:", size(root))
print("Height:", height(root))
print("Iterative Size:", iterative_size(root))