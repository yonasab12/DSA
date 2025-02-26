class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def del_pos(head, pos):
    if head is None:
        return head
    curr = head
    for i in range(1, pos):
        if curr is None:
            return head
        curr = curr.next
    if curr is None:
        return head
    if curr.prev is not None:
        curr.prev.next = curr.next
    if curr.next is not None:
        curr.next.prev = curr.prev
    if head == curr:
        head = curr.next
    return head

def del_head(head):
    if head is None:
        return None
    temp = head
    head = head.next
    if head is not None:
        head.prev = None
    return head

def del_last(head):
    if head is None:
        return None
    if head.next is None:
        return None
    curr = head
    while curr.next is not None:
        curr = curr.next
    if curr.prev is not None:
        curr.prev.next = None
    return head

def insert_end(head, new_data):
    new_node = Node(new_data)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    return head

def insertBegin(head, data):
    new_node = Node(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

def insert_at_position(head, pos, new_data):
    new_node = Node(new_data)
    if pos == 1:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        head = new_node
        return head
    curr = head
    for _ in range(1, pos - 1):
        if curr is None:
            print("Position out of bounds.")
            return head
        curr = curr.next
    if curr is None:
        print("Position out of bounds.")
        return head
    new_node.prev = curr
    new_node.next = curr.next
    curr.next = new_node
    if new_node.next is not None:
        new_node.next.prev = new_node
    return head

def find_length(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

def search_by_value(head, target):
    current = head
    pos = 1
    while current is not None:
        if current.data == target:
            return pos
        current = current.next
        pos += 1
    return -1

if __name__ == "__main__":
    # Create a sample doubly linked list: 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    print("Original Linked List: ", end="")
    print_list(head)

    
    target = 2
    print(f"Position of {target}: {search_by_value(head, target)}")
    target = 5
    print(f"Position of {target}: {search_by_value(head, target)}")