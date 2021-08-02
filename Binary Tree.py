class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    def  calculate_sum(self):
        sum = 0
        if self.left:
            sum += self.left.calculate_sum()

        if self.right:
            sum += self.right.calculate_sum()
        sum += self.data

        return sum

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
           elements += self.left.pre_order_traversal()

        if self.right:
           elements += self.right.pre_order_traversal()

        return elements

    def find_min(self):
        min = 0
        if self.left:
            min = self.left.find_min()

        else:
            min = self.data

        return min


    def find_max(self):
        max = 0
        if self.right:
            max = self.right.find_max()

        else:
            max = self.data

        return max










def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print(numbers_tree.calculate_sum())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())