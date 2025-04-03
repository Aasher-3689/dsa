# BINARY SEARCH TREE
import time
time1 = time.time()

class Node_BST:
    # create a node. used in class Binary Search Tree
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def _show_in_order_(self, n):
        # traversing in in_order. (left_child, root, right_child)
        try:
            if n.left_child:
                self._show_in_order_(n=n.left_child)
            print(n.data, end=", ")
            if n.right_child:
                self._show_in_order_(n=n.right_child)
        except Exception:
            return

    def show_in_order(self):
        # in_order traversing (this func is to be called by the user).
        # it calls the real func that contains code for in_order traversing
        # and initially gives self.root value to n parameter.
        print("In Order Traversing\n[", end="")
        self._show_in_order_(self.root)
        print("]\n")

    #-----------------------------------------------------------------

    def _show_pre_order_(self, n):
        # traversing in pre_order. (root, left_child, right_child)
        try:
            print(n.data, end=", ")
            if n.left_child:
                self._show_pre_order_(n=n.left_child)
            if n.right_child:
                self._show_pre_order_(n=n.right_child)
        except Exception:
            return

    def show_pre_order(self):
        # pre_order traversing (this func is to be called by the user).
        # it calls the real func that contains code for pre_order traversing
        # and initially gives self.root value to n parameter.
        print("Pre Order Traversing\n[", end="")
        self._show_pre_order_(self.root)
        print("]\n")

    #-----------------------------------------------------------------

    def insert(self, value_to_add):
        # inserting new node according to binary search tree rules
        new_node = Node_BST(value_to_add)
        if self.root is None:
            self.root = new_node
            return
        else:
            n = self.root
            while True:
                if value_to_add == n.data:
                    print(f"{value_to_add} already exist!")
                    break
                elif value_to_add < n.data:
                    if n.left_child is None:
                        n.left_child = new_node
                        break
                    n = n.left_child
                elif value_to_add > n.data:
                    if n.right_child is None:
                        n.right_child = new_node
                        break
                    n = n.right_child

    #-----------------------------------------------------------------

    def search(self, value_to_search):
        # To search either value is present in tree or not.
        # returning True if value is present and vice versa.
        n = self.root
        while n is not None:
            if value_to_search == n.data:
                print(f"True! {value_to_search} exist.")
                return
            elif value_to_search < n.data:
                n = n.left_child
            elif value_to_search > n.data:
                n = n.right_child
        return print(f"False! {value_to_search} doesn't exist.")

    #-----------------------------------------------------------------

    def remove(self, value_to_remove):
        # removing the data from tree keeping BST rules
        if self.root is None:
            return
        n = self.root
        parent = None
        while n is not None and n.data != value_to_remove:
            # moving to the correct node having value to remove
            parent = n
            if value_to_remove < n.data:
                n = n.left_child
            else:
                n = n.right_child
        # APPLYING CASES FOR DELETION
        if n is None:
            # (1) if value not found
            return
        elif n.left_child is None and n.right_child is None:
            # (2) if value is in leaf node
            if parent is None:
                self.root = None
            elif parent.left_child == n:
                parent.left_child = None
            else:
                parent.right_child = None
        elif n.right_child is None:
            # (3) if n node has only left node
            if parent is None:
                self.root = n.left_child
            elif parent.left_child == n:
                parent.left_child = n.left_child
            else:
                parent.right_child = n.left_child
        elif n.left_child is None:
            # (4) if n node has only right node
            if parent is None:
                self.root = n.right_child
            elif parent.right_child == n:
                parent.right_child = n.right_child
            else:
                parent.left_child = n.right_child
        else:
            # (5) if n has both left and right nodes.
            successor_parent = n
            successor = n.right_child
            while successor.left_child is not None:
                successor_parent = successor
                successor = successor.left_child
            n.data = successor.data
            if successor_parent.left_child == successor:
                successor_parent.left_child = successor.right_child
            else:
                successor_parent.right_child = successor.right_child

    #-----------------------------------------------------------------

    def min_value(self):
        # finding minimum value in the tree. the leftmost value
        n = self.root
        if n is not None:
            while n.left_child is not None:
                n = n.left_child
            print(f"Minimum value in tree is: {n.data}")
        else:
            print("Minimum Value can't be find in empty tree :(")

    def max_value(self):
        # finding minimum value in the tree. the leftmost value
        n = self.root
        if n is not None:
            while n.right_child is not None:
                n = n.right_child
            print(f"Maximum value in tree is: {n.data}")
        else:
            print("Maximum Value can't be find in empty tree :(")

#-----------------------
bst1 = Binary_Search_Tree()
bst1.insert(34)
bst1.insert(24)
bst1.insert(55)
bst1.insert(40)
bst1.insert(58)
bst1.insert(12)
bst1.insert(1)
bst1.remove(24)
bst1.remove(1)
bst1.remove(55)
bst1.remove(34)

#-----------------------
bst1.show_in_order()
bst1.show_pre_order()
bst1.min_value()
bst1.max_value()
bst1.search(58)
bst1.search(33)

#-----------------------
print(f"\n{time.time() - time1} seconds")
