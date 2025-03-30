import time
time1 = time.time()

"""
Start of Singly Linked List
"""
class Node:
    # for creating new node -used in linked list
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    # creating linked list
    def __init__(self):
        self.head = None

    def show_linked_list(self):
        # printing list on shell
        if self.head is None:
            print("[]")
        else:
            pointer_1 = self.head
            print("[", end="")
            while pointer_1 is not None:
                if pointer_1.next is not None:
                    print(f"{pointer_1.data},", end=" ")
                    pointer_1 = pointer_1.next
                else:
                    print(f"{pointer_1.data}]", end="\n")
                    break

    def add_start(self, data):
        # adding node at the start
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        # adding node at the end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer_2 = self.head
            while pointer_2.next is not None:
                pointer_2 = pointer_2.next
            pointer_2.next = new_node

    def add_between(self, index, data):
        # using index to add anywhere
        new_node = Node(data)
        if self.head is None or index <= 0:
            self.add_start(data)
        else:
            try:
                pointer_3 = self.head
                for _ in range(index-1):
                    pointer_3 = pointer_3.next
                new_node.next = pointer_3.next
                pointer_3.next = new_node
            except AttributeError:
                self.add_end(data)

    def del_end(self):
        # deleting last node
        if self.head is None:
            print("Couldn't remove! Linked List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            pointer_4 = self.head
            while pointer_4.next.next is not None:
                pointer_4 = pointer_4.next
            pointer_4.next = None

    def del_start(self):
        # deleting fist node
        if self.head is None:
            print("Couldn't remove! Linked List is empty")
        else:
            self.head = self.head.next

    def del_by_data(self, data_to_remove):
        # deleting all nodes of given data
        times_to_loop = 0
        if self.head is not None:
            n = self.head
            while n is not None:
                if n.data == data_to_remove:
                    times_to_loop += 1
                n = n.next

        for _ in range(times_to_loop):
            if self.head.data == data_to_remove:
                self.head = self.head.next
            else:
                pointer_5 = self.head
                while pointer_5.next is not None:
                    if pointer_5.next.data == data_to_remove:
                        break
                    pointer_5 = pointer_5.next
                pointer_5.next = pointer_5.next.next
            
        
#-------------------
LL1 = LinkedList()
LL1.add_start(5)
LL1.add_end(9)
LL1.add_start(58)
LL1.add_end(67)
LL1.add_start(7)
LL1.add_between(2, 876)
LL1.add_between(3, 39)
LL1.add_between(1, 666)
LL1.add_between(0, 777)
LL1.del_end()
LL1.del_end()
LL1.del_start()
LL1.del_start()
LL1.del_by_data(39)

LL2 = LinkedList()
LL2.add_start(78)
LL2.add_between(1, 45)
LL2.add_end(980)
LL2.add_between(2, 88)
LL2.del_end()
LL2.del_start()
LL2.add_end("Aasher")
LL2.add_end(45)
LL2.add_end(67)
LL2.add_end(45)
LL2.del_by_data(45)

LL3 = LinkedList()
LL3.add_start("01")
LL3.add_end("02")
LL3.del_by_data("0d")

#----------------------
LL1.show_linked_list()
LL2.show_linked_list()
LL3.show_linked_list()

print(f"\n{time.time() - time1} seconds\n")
#---------------------

"""
End of singly Linked List
AND
Start of doubly Linked List
"""

time2 = time.time()

class Node_DLL:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_LL:
    def __init__(self):
        self.head = None

    def show_doublyLL_forward(self):
        if self.head is None:
            print("[]")
        else:
            pointer_6 = self.head
            print("[", end="")
            while pointer_6 is not None:
                if pointer_6.next is not None:
                    print(f"{pointer_6.data},", end=" ")
                    pointer_6 = pointer_6.next
                else:
                    print(f"{pointer_6.data}]", end="\n")
                    break

    def show_doublyLL_backward(self):
        if self.head is None:
            print("[]")
        else:
            pointer_7 = self.head
            while pointer_7.next is not None:
                pointer_7 = pointer_7.next
            print("[", end="")
            while pointer_7 is not None:
                if pointer_7.prev is not None:
                    print(f"{pointer_7.data},", end=" ")
                    pointer_7 = pointer_7.prev
                else:
                    print(f"{pointer_7.data}]", end="\n")
                    break

    def add_start(self, data):
        new_node = Node_DLL(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def add_end(self, data):
        new_node = Node_DLL(data)
        if self.head is None:
            self.head = new_node
        else:
            pointer_8 = self.head
            while pointer_8.next is not None:
                pointer_8 = pointer_8.next
            new_node.prev = pointer_8
            pointer_8.next = new_node

    def add_between(self, index, data):
        new_node = Node_DLL(data)
        if self.head is None or index <= 0:
            self.add_start(data)
        else:
            pointer_9 = self.head
            try:
                for _ in range(index-1):
                    pointer_9 = pointer_9.next
                new_node.next = pointer_9.next
                new_node.prev = pointer_9
                pointer_9.next.prev = new_node
                pointer_9.next = new_node
            except AttributeError:
                self.add_end(data)

    def del_end(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
        else:
            pointer_10 = self.head
            while pointer_10.next.next is not None:
                pointer_10 = pointer_10.next
            pointer_10.next = None

    def del_start(self):
        if self.head is None:
            return
        else:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

    def del_by_data(self, data_to_remove):
        times_to_loop = 0
        if self.head is not None:
            n = self.head
            while n is not None:
                if n.data == data_to_remove:
                    times_to_loop += 1
                n = n.next

        for _ in range(times_to_loop):
            if self.head.data == data_to_remove:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
            else:
                pointer_11 = self.head
                while pointer_11.next is not None:
                    if pointer_11.next.data == data_to_remove:
                        break
                    pointer_11 = pointer_11.next
                pointer_11.next = pointer_11.next.next
                if pointer_11.next is not None:
                    pointer_11.next.prev = pointer_11
                    
#---------------------
dll_1 = Doubly_LL()
dll_1.add_start(6)
dll_1.add_start(56)
dll_1.add_start(98)
dll_1.add_start(678)
dll_1.add_end(143)
dll_1.add_end(341)
dll_1.add_between(1, 16)
dll_1.add_between(7, 10)
dll_1.del_end()
dll_1.del_end()
dll_1.del_start()
dll_1.del_by_data(56)

#---------------------
dll_1.show_doublyLL_forward()
dll_1.show_doublyLL_backward()

print(f"\n{time.time()-time2} seconds\n")
#----------------------

"""
End of Doubly Linked List
AND
Start of Circular Linked List
"""

time3 = time.time()

class Circular_LL:
    def __init__(self):
        self.head = None

    def show_circularLL_0(self):
        print("Circular_LL from index (0)")
        if self.head is None:
            print("[]")
        else:
            print("[", end="")
            pointer_12 = self.head
            while pointer_12.next != self.head:
                print(f"{pointer_12.data},", end=" ")
                pointer_12 = pointer_12.next
            print(f"{pointer_12.data}]")

    def show_circularLL_1(self):
        print("Circular_LL from index (1)")
        if self.head is None:
            print("[]")
        elif self.head.next == self.head:
            print("Index (1) not exist")
        else:
            print("[", end="")
            pointer_13 = self.head.next
            while pointer_13 != self.head:
                print(f"{pointer_13.data},", end=" ")
                pointer_13 = pointer_13.next
            print(f"{pointer_13.data}]")

    def add_start(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            n = self.head
            while n.next != self.head:
                n = n.next
            self.head, n.next = new_node, new_node
        else:
            self.head, new_node.next = new_node, new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head, new_node.next = new_node, new_node
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = new_node
            new_node.next = self.head


#-------------------------
cll1 = Circular_LL()
cll1.add_start(5)
cll1.add_start(23)
cll1.add_start(45)
cll1.add_start(87)
cll1.add_end(6)
cll1.add_end(56)


#-------------------------
cll1.show_circularLL_0()
cll1.show_circularLL_1()

print(f"\n{time.time()-time3} seconds\n")
