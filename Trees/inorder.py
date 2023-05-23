class Tree:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None

class Inorder:
    def in_order_traversal(self, root):
        if(root==None):
            return 
        else:
            self.in_order_traversal(root.leftnode)
            print(root.data, end=' ')
            self.in_order_traversal(root.rightnode)

root = Tree(1)
root.leftnode = Tree(2) # type: ignore
root.rightnode = Tree(3) # type: ignore
root.leftnode.leftnode = Tree(4) # type: ignore
root.leftnode.leftnode.leftnode = Tree(5) # type: ignore
root.leftnode.rightnode = Tree(6) # type: ignore
root.rightnode.rightnode=Tree(7) # type: ignore

inorder = Inorder()
inorder.in_order_traversal(root)


    