class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        if self.head == None:
            return None
        else:
            previous = prev
            current = node
            following = current.next_node
            while current:
                current.next_node = previous
                previous = current
                current = following
                if following:
                    following = following.next_node
            self.head = previous
        
    def print_list(self):
        cur_node = self.head
        while cur_node is not None:
            print(f'{cur_node.get_value()} -> {cur_node.get_next() if cur_node.get_next() == None else cur_node.get_next().get_value()}')
            cur_node = cur_node.get_next()

linked_list = LinkedList()
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)
linked_list.add_to_head(4)
linked_list.add_to_head(5)
linked_list.print_list()
linked_list.reverse_list(linked_list.head, None)
linked_list.print_list()
