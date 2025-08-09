class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example usage:
# Creating a linked list with a cycle
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node1  # Creates a cycle

print(has_cycle(node1))  # Output: True

# Creating a linked list without a cycle
node4 = Node(4)
node5 = Node(5)
node4.next = node5