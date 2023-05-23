class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertathead(self, newNode):
        if (self.head == None):
            self.head = newNode
        else:
            tempnode = self.head
            self.head = newNode
            self.head.next = tempnode

    def printll(self):
        currentnode = self.head
        if (self.head == None):
            print("List is Empty")
        while True:
            if (currentnode is None):
                break
            print(currentnode.data)
            currentnode = currentnode.next


firstnode = Node("Nishant")
ll = LinkedList()
ll.insertathead(firstnode)
secondnode = Node("Shubrah")
ll.insertathead(secondnode)
thirdnode = Node("Pragya")
ll.insertathead(thirdnode)
fourthnode = Node("Yashika")
ll.insertathead(fourthnode)
ll.printll()
