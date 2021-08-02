class BST:
    def __init__(self):
        self.root = None
        self.k = 3

    def insert_node(self,key):
        new = BSTnode()
        new.key = key
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:

                    if node.key<key:
                        #Go Right
                        if node.right is None:
                            node.right = new
                            new.parent = node
                            break
                        node = node.right
                    else:
                        #Go left
                        if node.left is None:
                            node.left = new
                            new.parent = node
                            break
                        node = node.left

        return new
    def find(self,val):
        if self.root is None:
            return False
        node = self.root
        while True:
            if node.key == val:
                return True
            if node.key<val:
                if node.right is None:
                    return False
                node = node.right
            else:
                if node.left is None:
                    return False
                node = node.left

    def can_insert(self,key):
        if self.root is None:
            return True
        else:
            node = self.root
            while True:
                diff = abs(node.key-key)
                if diff<self.k:
                    return False
                else:
                    if key>node.key:
                        if node.right is None:
                            return True
                        node = node.right
                    else:
                        if node.left is None:
                            return True
                        node = node.left

        





class BSTnode:
    def __init__(self):
        self.root = None
        self.key = None
        self.disconnect()

    def disconnect(self):
        self.parent = None
        self.left = None
        self.right = None

#Airplane Reservation Problem

def reservation(a:[],k:int,n:int,t:int):
    bst = BST()
    for i in range(0,n):
        bst.insert_node(a[i])
    return bst.can_insert(t)

print(reservation([41,46,49,56],3,4,53))





