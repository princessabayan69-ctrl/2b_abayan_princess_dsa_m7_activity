class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert a new key
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)

        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Search for a key
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False

        if key == node.key:
            return True

        elif key < node.key:
            return self._search(node.left, key)

        else:
            return self._search(node.right, key)

    # Find the smallest node
    def _find_min(self, node):
        while node.left is not None:
            node = node.left

        return node

    # Delete a key
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            elif node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            # Case 3: Two children
            else:
                successor = self._find_min(node.right)
                node.key = successor.key
                node.right = self._delete(node.right, successor.key)

        return node

    # Return inorder traversal as a list
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


# Main program
if __name__ == "__main__":

    bst = BST()

    for key in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        bst.insert(key)

    print(bst.inorder())  # line A

    print(bst.search(35))  # line B

    print(bst.search(99))  # line C

    bst.delete(20)  # leaf

    bst.delete(40)  # two children

    print(bst.inorder())  # line D