class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None

def insert_at_position(head, pos, new_data):
  
    # Create a new node
    new_node = Node(new_data)

    # Insertion at the beginning
    if pos == 1:
        new_node.next = head

        # If the linked list is not empty, set the
        #prev of head to new node
        if head is not None:
            head.prev = new_node

        # Set the new node as the head of the linked list
        head = new_node
        return head

    curr = head
    
    # Traverse the list to find the node before the 
    #insertion point
    for _ in range(1, pos - 1):
        if curr is None:
            print("Position is out of bounds.")
            return head
        curr = curr.next

    # If the position is out of bounds
    if curr is None:
        print("Position is out of bounds.")
        return head

    # Set the prev of new node to curr
    new_node.prev = curr

    # Set the next of new node to next of curr
    new_node.next = curr.next

    # Update the next of current node to new node
    curr.next = new_node

    # If the new node is not the last node, update 
    #prev of next node to new node
    if new_node.next is not None:
        new_node.next.prev = new_node

    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List: ", end="")
    print_list(head)

    # Insert new node with data 3 at position 3
    print("Inserting Node with data 3 at position 3: ", end="")
    data = 3
    pos = 3
    head = insert_at_position(head, pos, data)

    # Print the updated list
    print_list(head)