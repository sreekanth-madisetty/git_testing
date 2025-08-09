class Node:
    def __init__(self, data):
        # self.data = data
        # self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #This comment is added in remote branch of Ruchitha

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if not curr:
            return  # Node not found
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()         # Output: 1 -> 2 -> 3 -> None
ll.delete_node(2)
ll.display()         # Output: 1 -> 3 ->
