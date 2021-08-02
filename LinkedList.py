class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        iterator = self.head
        if iterator == None:
            print("list is empty")
        while iterator:
            if iterator.data == data_after:
                new_node = Node(data_to_insert,iterator.next)
                iterator.next = new_node
                break
            if iterator.next == None:
                raise Exception(f"no such value in list {data_after}")
            iterator = iterator.next

    def removeElements(self, head: Node, val: int):
        iter = head
        cuurent_node = head
        while iter:
            if iter.next.val == val:
                iter = iter.next
                continue
            current_node.next = iter.next
            current_node = iter.next
            iter = iter.next
        if head.val == val:
            head = head.next


    def remove_by_value(self, data):
        iterator = self.head
        if iterator == None:
            print("list is empty")
        if iterator.data == data:
            self.head = iterator.next
            return
        while iterator:
            if iterator.next.data == data:
                iterator.next = iterator.next.next
                break
            if iterator.next == None:
                raise Exception(f"{data} not in the list ")
            iterator = iterator.next


    def reverse(self):


#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.insert_at_begining("adas")
#     # ll.insert_at(1,"blueberry")
#     # ll.remove_at(2)
#     ll.insert_after_value("mango", "apple")
#     ll.insert_after_value("orange","peanuts")
#     ll.remove_by_value("banana")
#     ll.remove_by_value("grapes")
#     ll.remove_by_value("orange")
#     ll.print()


    # ll.insert_values([45,7,12,567,99])
    # ll.insert_at_end(67)
    # ll.print()