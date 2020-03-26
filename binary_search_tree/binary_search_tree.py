import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        inserted = False
        while (inserted == False) : 
            if value < node.value:
                if node.left == None:
                    node.left = BinarySearchTree(value)
                    inserted = True
                else:
                    node = node.left
            else:
                if node.right == None:
                    node.right = BinarySearchTree(value)
                    inserted = True
                else:
                    node = node.right

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        node = self
        while (target != node.value):
            if target < node.value:
                if node.left == None:
                    return False
                else:
                     node = node.left
            else:
                if node.right == None:
                    return False
                else:
                    node = node.right
        
        return True

    # Return the maximum value found in the tree
    def get_max(self):
        node = self
        while node.right != None:
            node = node.right
        
        return node.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
        cb(self.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
