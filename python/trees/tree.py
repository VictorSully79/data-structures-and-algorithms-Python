class Node:
    """
    Class contains the properties of the NODE
    """

    def _init_(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def _init_(self, root=None):
            self.root = root

    def pre_order(self):

        elements = []

        if self.root is None:
            return "The Tree is Empty"

        def traverse_tree(root):
                elements.append(root.value)

                if root.left:
                    traverse_tree(root.left)

                if root.right:
                    traverse_tree(root.right)

        traverse_tree(self.root)

        return elements

            # Traverse a Binary Tree from left, root, right

    def search_in_order(self):

        elements = []

        # Check to see if tree is empty
        if self.root is None:
            return "The Tree is Empty"


        def traverse_tree(root):
            if root.left:
                traverse_tree(root.left)

            elements.append(root.value)

            if root.right:
                traverse_tree(root.right)


            traverse_tree(self.root)

            return elements

        # Search Tree Left, Right, Root
    def post_order(self):

        if self.root is None:
            return "The Tree is Empty"

        elements = []

        def traverse_tree(root):
            if root.left:
                traverse_tree(root.left)

            if root.right:
                traverse_tree(root.right)

            elements.append(root.value)

            traverse_tree(self.root)

            return elements



class Binary_Search_Tree(BinaryTree):
    # Add a node to a tree. Tree contains only integers

    def _init_(self, root=None, value=None):
        self.root = root
        self.value = value
        self.left = None
        self. right = None


    def add(self, value):

        if value is None or type(value) == str:
            return "Only numbers allowed in Node"

        node = Node(value)

        if self.root is None:
            self.root = node

        current = self.root

        while current != None:
            if current.value > value:
                if current.left is None:
                    current.left = node

                else:
                    current = current.left

            if current.value < value:
                if current.right is None:
                    current.right = node

                else:
                    current = current.right

            if current.value == value:
                return "Duplicate Value"


    def contains(self, value):
        # Search for a specific value in the tree

        current = self.root

        while current != None:
            if current.value > value:
                current = current.left
            if current.value < value:
                current = current.right
            if current.value == value:
                return True
            else:
                return False


    def find_max(self):
        find_max = self.root.value

        def traverse_tree(root):
            nonlocal find_max

            if root.value > find_max:
                find_max = root.value

            if root.left:
                traverse_tree(root.left)

            if root.right:
                traverse_tree(root.right)

        traverse_tree(self.root)
        return find_max


