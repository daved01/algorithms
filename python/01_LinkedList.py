# =================================================================== #
# Linked list                                                         #
#                                                                     #
# Operations:                                                         #
# Insertion, deletion O(1)                                            #
#                                                                     #
# =================================================================== #

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, node):
        self.head = node

    def add_first_node(self, node):
        node.next = self.head
        self.head = node

    def add_last_node(self, node):
        current_node = self.head
        
        if current_node is None:
            self.addHead(node)
        else:
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

    def add_at_index(self, node, index):
        current_node = self.head
        
        for i in range(index - 1):
            current_node = current_node.next
            
            if current_node.next is None:
                print("Error. Index exceeds list length!")
                return
        
        temp = current_node.next
        current_node.next = node
        node.next = temp

    def delete_at_index(self, index):
        current_node = self.head

        for i in range(index - 1):
            current_node = current_node.next
            
            if current_node.next is None:
                print("Error. Index exceeds list length!")
                return
            
            prev_node = current_node
        current_node = current_node.next
        prev_node.next = current_node.next

    def get_at_index(self, index):
        current_node = self.head

        for i in range(index):
            current_node = current_node.next
            
            if current_node.next is None:
                print("Error. Index exceeds list length!")
                return
        
        print("Value at {}: {}".format(index, current_node.data))
        
    def print_list(self):
        if self.head is None:
            print("List is empty!")
            return
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
        print("End")
        
        
if __name__ == "__main__":
    mylist = LinkedList()
    mylist.add_head(Node("B"))
    mylist.add_first_node(Node("A"))
    mylist.add_last_node(Node("C"))
    mylist.add_last_node(Node("D"))
    mylist.add_last_node(Node("Z"))
    mylist.add_at_index(Node("Y"), 4)
    mylist.get_at_index(3)
    mylist.print_list()
    mylist.delete_at_index(2)
    mylist.print_list()
