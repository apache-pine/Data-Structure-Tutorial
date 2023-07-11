class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("Value already in tree.")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, current_node):
        if data > current_node.data and current_node.right:
            return self._find(data, current_node.right)
        elif data < current_node.data and current_node.left:
            return self._find(data, current_node.left)
        if data == current_node.data:
            return True

    def remove(self, data):
        if self.root:
            self.root = self._remove(data, self.root)

    def _remove(self, data, current_node):
        if not current_node:
            return current_node
        elif data < current_node.data:
            current_node.left = self._remove(data, current_node.left)
        elif data > current_node.data:
            current_node.right = self._remove(data, current_node.right)
        else:
            # removing node with no or single child
            if not current_node.right:
                return current_node.left
            if not current_node.left:
                return current_node.right

            # removing node with two children
            temp_val = self._find_min(current_node.right)
            current_node.data = temp_val
            current_node.right = self._remove(temp_val, current_node.right)
        return current_node

    def _find_min(self, current_node):
        if current_node.left:
            return self._find_min(current_node.left)
        return current_node.data

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, current_node):
        if current_node:
            self._inorder_print_tree(current_node.left)
            print(str(current_node.data))
            self._inorder_print_tree(current_node.right)

    def preorder_print_tree(self):
        if self.root:
            self._preorder_print_tree(self.root)

    def _preorder_print_tree(self, current_node):
        if current_node:
            print(str(current_node.data))
            self._preorder_print_tree(current_node.left)
            self._preorder_print_tree(current_node.right)

    def postorder_print_tree(self):
        if self.root:
            self._postorder_print_tree(self.root)

    def _postorder_print_tree(self, current_node):
        if current_node:
            self._postorder_print_tree(current_node.left)
            self._postorder_print_tree(current_node.right)
            print(str(current_node.data))

    def height(self):
        if self.root:
            return self._height(self.root)
        else:
            return 0

    def _height(self, current_node):
        if current_node is None:
            return -1
        left_height = self._height(current_node.left)
        right_height = self._height(current_node.right)
        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.size(node.left) + self.size(node.right)

    def is_empty(self):
        return not bool(self.root)

    ########################
    # Solution starts here #
    ########################

    def count_leaves(self):
        return self._count_leaves(self.root)

    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        else:
            return self._count_leaves(node.left) + self._count_leaves(node.right)

    ######################
    # Solution ends here #
    ######################


# Sample Test Cases (may not be comprehensive)
print("\n=========== PROBLEM TESTS ===========")
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.count_leaves())
# Expected output: 4
