class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastnode = self.head
            while lastnode.next is not None:
                lastnode=lastnode.next
            lastnode.next=newNode          
    def printll(self):
        currentnode = self.head
        if (self.head == None):
            print("List is Empty")
        while currentnode:
            print(currentnode.data)
            currentnode = currentnode.next


firstnode = Node("Nishant")
ll = LinkedList()
ll.insert(firstnode)
secondnode = Node("Shubrah")
ll.insert(secondnode)
thirdnode = Node("Pragya")
ll.insert(thirdnode)
fourthnode = Node("Yashika")
ll.insert(fourthnode)
fifthnode=Node("Akshay")
ll.insert(fifthnode)
ll.printll()
