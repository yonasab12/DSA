class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Function to delete the first node (head) of the list
# and return the second node as the new head
def del_head(head):
  
    # If empty, return None
    if head is None:
        return None

    # Store in temp for deletion later
    temp = head

    # Move head to the next node
    head = head.next

    # Set prev of the new head
    if head is not None:
        head.prev = None

    # Return new head
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

    print("After Deletion at the beginning: ", end="")
    head = del_head(head)