class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, data, position):
        if position == 0:
            self.insert_head(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("Position out of range")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove_head(self):
        if self.head is None:
            raise Exception("LinkedList is empty")
        removed = self.head
        self.head = self.head.next
        removed.next = None
        return removed.data

    def remove_tail(self):
        if self.head is None:
            raise Exception("LinkedList is empty")
        if self.head.next is None:
            removed = self.head
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            removed = current.next
            current.next = None
        return removed.data

    def remove(self, position):
        if position == 0:
            return self.remove_head()
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("Position out of range")
                current = current.next
            removed = current.next
            if removed is None:
                raise IndexError("Position out of range")
            current.next = removed.next
            removed.next = None
            return removed.data

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        return self.head is None


def find_middle_element(linked_list):
    slow_ptr = linked_list.head
    fast_ptr = linked_list.head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.data


"""
In this solution, we use the two-pointer technique to find the middle element. We initialize two pointers, slow_ptr and fast_ptr, to the head of the linked list. The slow_ptr moves one step at a time, while the fast_ptr moves two steps at a time. By the time the fast_ptr reaches the end of the list (or None), the slow_ptr will be pointing to the middle element.

To handle the case of an even number of elements, we check if the fast_ptr and its next node are not None. If they are not None, we move the slow_ptr and fast_ptr as usual. Otherwise, we stop at the current position of the slow_ptr, which represents the second middle element.
"""


# Sample Test Cases (may not be comprehensive)
print("\n=========== PROBLEM TESTS ===========")
linked_list = LinkedList()
linked_list.insert_tail(1)
linked_list.insert_tail(2)
linked_list.insert_tail(3)
linked_list.insert_tail(4)
linked_list.insert_tail(5)
middle_element = find_middle_element(linked_list)
print(middle_element)
# Expected output: 3

linked_list.insert_tail(6)
middle_element = find_middle_element(linked_list)
print(middle_element)
# Expected output: 4

linked_list.insert_tail(1)
linked_list.insert_tail(2)
linked_list.insert_tail(3)
linked_list.insert_tail(4)
linked_list.insert_tail(5)
linked_list.insert_tail(6)
middle_element = find_middle_element(linked_list)
print(middle_element)
# Expected output: 1
