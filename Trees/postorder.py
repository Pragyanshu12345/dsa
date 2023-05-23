class Tree:
    def __init__(self, data):
        self.data = data
        self.leftnode = None
        self.rightnode = None


class Postorder:
    def post_order_traversal(self, root):
        if (root == None):
            return
        else:
            self.post_order_traversal(root.leftnode)
            self.post_order_traversal(root.rightnode)
            print(root.data, end=' ')


root = Tree(1)
root.leftnode = Tree(2)  # type: ignore
root.rightnode = Tree(3)  # type: ignore
root.leftnode.leftnode = Tree(4)  # type: ignore
root.leftnode.leftnode.leftnode = Tree(5)  # type: ignore
root.leftnode.rightnode = Tree(6)  # type: ignore
root.rightnode.rightnode = Tree(7)  # type: ignore
root.rightnode.leftnode = Tree(8)  # type: ignore
postorder = Postorder()
postorder.post_order_traversal(root)
