class Tree:
    def __init__(self,data):
        self.data=data
        self.leftnode=None
        self.rightnode=None

class Preorder:
    def pre_order_traversal(self, root):
        if(root==None):
            return 
        else:
            print(root.data, end=' ')
            self.pre_order_traversal(root.leftnode)
            self.pre_order_traversal(root.rightnode)

root = Tree(1)
root.leftnode = Tree(2) # type: ignore
root.rightnode = Tree(3) # type: ignore
root.leftnode.leftnode = Tree(4) # type: ignore
root.leftnode.leftnode.leftnode = Tree(5) # type: ignore
root.leftnode.rightnode = Tree(6) # type: ignore
root.rightnode.rightnode=Tree(7) # type: ignore

preorder = Preorder()
preorder.pre_order_traversal(root)


    