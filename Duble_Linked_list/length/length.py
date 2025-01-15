class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None


def find_length(head):
    count = 0
    cur = head
    while cur is not None:
        count += 1
        cur = cur.next
    return count


if __name__ == "__main__":
  
    # Create a doubly linked list 

    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Length of the doubly linked list: " +
          str(find_length(head)))