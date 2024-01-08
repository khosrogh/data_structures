class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Display the linked list
    def __repr__(self):
        temp = self.head
        nodes = []
        while temp:
            nodes.append(repr(temp))
            temp = temp.next
        return '[' + ', '.join(nodes) + ']'

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def search(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            else:
                current_node = current_node.next
        return False

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=', ')
            current_node = current_node.next

    # Reverse the linked list
    def reverse(self):
        temp = self.head
        prev_node = None
        next_node = None
        while temp:
            next_node = temp.next
            temp.next = prev_node
            prev_node = temp
            temp = next_node
        self.head = prev_node


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    persian_dish = LinkedList()
    persian_dish.insert_at_end("prepare")
    persian_dish.insert_at_end("stir")
    persian_dish.insert_at_beginning("assemble")
    persian_dish.search("stir")
    persian_dish.search("heating")
    persian_dish.print_list()
    print("", end='\n')
    persian_dish.reverse()
    persian_dish.print_list()
    # repr(persian_dish)
