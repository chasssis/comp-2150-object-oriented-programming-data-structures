class Node:
    ##single node
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    ##linked list
    def __init__(self):
        self.head = None

    def append(self, data):
        ##new node
        new_node = Node(data)
        
        ##empty list
        if not self.head:
            self.head = new_node
            return
        
        ##goto end of lsit
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def print_list(self):
        ##print elements in order
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print(" -> ".join(elements) + " -> None")

##test

ll = LinkedList()

##append vaues
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ll.print_list()

print(f"Find 20: {ll.find(20)}")
print(f"Find 99: {ll.find(99)}")