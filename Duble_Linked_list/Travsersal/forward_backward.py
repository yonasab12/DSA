class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Insert a node at the beginning
def insertBegin(head, data):
    
    # Create a new node
    new_node = Node(data)
    
    # Make next of it as head
    new_node.next = head
    
    # Set previous of head as new node
    if head is not None:
        head.prev = new_node
    
    # Return new node as new head
    return new_node

# Print the doubly linked list
def printList(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 2 <-> 3 <-> 4
    head = Node(2)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List:", end=' ')
    printList(head)

    # Insert a new node at the front of the list
    head = insertBegin(head, 1)

    # Print the updated list
    print("After inserting Node 1 at the front:", end=' ')
    printList(head)