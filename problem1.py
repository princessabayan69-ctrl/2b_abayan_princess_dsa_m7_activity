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


# Inorder: Left, Root, Right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)


# Preorder: Root, Left, Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)


# Postorder: Left, Right, Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")


# Level-order: Visit level by level
def level_order(root):
    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)


# Display results
print("Inorder:", end=" ")
inorder(root)

print("\nPreorder:", end=" ")
preorder(root)

print("\nPostorder:", end=" ")
postorder(root)

print("\nLevel-order:", end=" ")
level_order(root)

print() 

Output:
Inorder: 2 4 6 10 12 15 20 25 30 
Preorder: 15 10 4 2 6 12 25 20 30 
Postorder: 2 6 4 12 10 20 30 25 15 
Level-order: 15 10 25 4 12 20 30 2 6 
