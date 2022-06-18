class Node:
    def __init__(self, cargo=None, next = None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return str(self.cargo)

    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
    
    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
    
    def add_first(self,cargo):
        node = Node(cargo)
        node.next = self.head
        self.head = node
        self.length += 1


def print_list(node):
    while node is not None:
        if node.next is None:
            print(node,end="]")
        else:
            print(node,end=", ")
        node = node.next
    print()

def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail) #recursion
    print(head,end=" ")

def print_backward_nicely(list): #Wrapper
    print("[", end=" ")
    print_backward(list) #Helper
    print("]")

#Modifying lists

def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    #now make first refer to third node
    first.next = second.next
    #Separate second node from the rest of the list
    second.next = None
    return second

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

#To link these nodes - make first refer second, second refer third and so on
node1.next = node2
node2.next = node3

print_list(node1)