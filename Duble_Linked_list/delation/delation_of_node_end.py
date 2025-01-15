class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def del_last(head):
  
    # Corner cases
    if head is None:
        return None
    if head.next is None:
        return None

    # Traverse to the last node
    curr = head
    while curr.next is not None:
        curr = curr.next

    # Update the previous node's next pointer
    if curr.prev is not None:
        curr.prev.next = None

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

    print("After Deletion at the end: ", end="")
    head = del_last(head)

    print_list(head)