# Binary search tree
class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    def insert(self,newnode):
        if self.root is None: # creating the root node
            self.root = newnode
            return
        else:
            temp = self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right
    def inorder(self,rt): #recursive
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)
    def search(self,key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False
b = BST()
b.insert(Node(10))
b.insert(Node(5))
b.insert(Node(20))
b.insert(Node(-2))
b.insert(Node(7))
b.insert(Node(15))
b.insert(Node(30))
print("Display in inorder")
b.inorder(b.root)
print()
if(b.search(7)):
    print("Given node is present")
else:
    print("Given node is not present")

                
