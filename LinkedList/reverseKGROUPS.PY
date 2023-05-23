class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, newNode):
        if (self.head == None):
            self.head = newNode
        else:
            lastnode = self.head
            while (True):
                if (lastnode.next is None):
                    break
                lastnode = lastnode.next
            lastnode.next = newNode

    def reversell(self,s,e):
        p = None
        q = s
        r = s.next
        while (p != e):
            q.next = p
            p=q
            q = r
            if(r!=None):
                r=r.next

    def reverseinK(self,head,k):
        dummy=Node(-1)
        dummy.next=head
        befstart=dummy
        e=head
        i=0
        while(e!=None):
            i+=1
            if(i%k==0):
                 s=befstart.next 
                 temp=e.next
                 self.reversell( s,e)
                 befstart.next=e
                 s.next=temp
                 befstart=s
                 e=temp
            else:
                e=e.next
        return dummy.next


    def printll(self):
        currentnode = self.head
        if (self.head == None):
            print("List is Empty")
        while True:
            if (currentnode is None):
                break
            print(currentnode.data)
            currentnode = currentnode.next


firstnode = Node(1)
ll = LinkedList()
ll.insert(firstnode)
secondnode = Node(2)
ll.insert(secondnode)
thirdnode = Node(3)
ll.insert(thirdnode)
fourthnode = Node(4)
ll.insert(fourthnode)
fifthnode = Node(5)
ll.insert(fifthnode)
ll.head=ll.reverseinK(ll.head,2)
ll.printll()
