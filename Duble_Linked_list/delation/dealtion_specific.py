class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Function to delete a node at a specific position 
#in the doubly linked list
def del_pos(head, pos):
    # If the list is empty
    if head is None:
        return head

    curr = head

    # Traverse to the node at the given position
    for i in range(1, pos):
        if curr is None:
            return head
        curr = curr.next

    # If the position is out of range
    if curr is None:
        return head

    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = curr.next

    # Update the next node's prev pointer
    if curr.next is not None:
        curr.next.prev = curr.prev

    # If the node to be deleted is the head node
    if head == curr:
        head = curr.next

    # Return the updated head
    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    print("Original Linked List: ", end="")
    print_list(head)

    print("After Deletion at the position 2: ", end="")
    head = del_pos(head, 2)

    print_list(head)