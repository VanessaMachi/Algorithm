# recursive

class Node(object):
    def __init__(self, value):
        self.value = value
        # pointer
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder(tree.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder(start.right, traversal)
        return traversal

    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
    #   if node == None:
            # return
        # visit(node)
        # preorder(node.left)
        # preorder(node.right)

    # def inorder(node):
        # if node == None:
            # return
        # inorder(node.left)
        # # visit(node)
        # inorder(node.right)

        # def postorder(node):
        #     if node == None:
        #         return
        # postorder(node.left)
        # postorder(node.right)
        # visit(node)

# post-order - 4, 5, 2, 8, 6, 7, 3, 1
# in-order   - 4, 2, 5, 1, 8, 6, 3, 7
# pre-order  - 1, 2, 4, 5, 3, 6, 8, 7
#
#        1
#      /   \
#     2     3
#    / \   / \ 
#   4   5 6   7
#        /
#       8

# Build the tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.left.left = Node(8)
tree.root
print(tree.print_tree("postorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("preorder"))

