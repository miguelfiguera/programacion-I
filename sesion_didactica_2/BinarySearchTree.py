class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    
    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.root=None
    
    def insert(self,value):
        pass