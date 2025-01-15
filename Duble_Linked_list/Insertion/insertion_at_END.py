class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to insert a new node at the end of the 
#doubly linked list
def insert_end(head, new_data):
      
    # Create a new node
    new_node = Node(new_data)
    
    # If the linked list is empty, set the new node
    #as the head
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        # Set the next of the last node to the new node
        curr.next = new_node
        
        # Set the prev of the new node to the last node
        new_node.prev = curr
    
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

    # Print the original list
    print("Original Linked List: ", end="")
    print_list(head)

    # Insert a new node with data 4 at the end
    print("Inserting Node with data 4 at the end: ", end="")
    data = 4
    head = insert_end(head, data)

    # Print the updated list
    print_list(head)