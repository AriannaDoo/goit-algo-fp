from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterable, Tuple


@dataclass
class Node:
    value: int
    next: Optional["Node"] = None


class SinglyLinkedList:
    def __init__(self, values: Optional[Iterable[int]] = None):
        self.head: Optional[Node] = None
        if values:
            for v in values:
                self.append(v)

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def to_list(self) -> list[int]:
        out = []
        cur = self.head
        while cur:
            out.append(cur.value)
            cur = cur.next
        return out

    # Reverse: меняем ссылки между узлами
    def reverse(self) -> None:
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    # Sort: merge sort для связного списка 
    def sort(self) -> None:
        self.head = merge_sort(self.head)

    # Merge: объединить два отсортированных списка в один отсортированный
    @staticmethod
    def merge_sorted(a: "SinglyLinkedList", b: "SinglyLinkedList") -> "SinglyLinkedList":
        merged_head = merge_two_sorted(a.head, b.head)
        result = SinglyLinkedList()
        result.head = merged_head
        return result


def split_list(head: Optional[Node]) -> Tuple[Optional[Node], Optional[Node]]:
    """Разделение списка на 2 половины (slow/fast pointers)."""
    if head is None or head.next is None:
        return head, None

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next  # type: ignore
        fast = fast.next.next

    mid = slow.next  # type: ignore
    slow.next = None  # type: ignore
    return head, mid


def merge_two_sorted(a: Optional[Node], b: Optional[Node]) -> Optional[Node]:
    """Слияние двух отсортированных связных списков."""
    dummy = Node(0)
    tail = dummy

    while a and b:
        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a else b
    return dummy.next


def merge_sort(head: Optional[Node]) -> Optional[Node]:
    """Merge sort для связного списка."""
    if head is None or head.next is None:
        return head

    left, right = split_list(head)
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge_two_sorted(left_sorted, right_sorted)


if __name__ == "__main__":
    # Demo 
    ll = SinglyLinkedList([4, 2, 5, 1, 3])
    print("Original:", ll.to_list())

    ll.reverse()
    print("Reversed:", ll.to_list())

    ll.sort()
    print("Sorted:", ll.to_list())

    a = SinglyLinkedList([1, 3, 5, 7])
    b = SinglyLinkedList([2, 4, 6, 8])
    merged = SinglyLinkedList.merge_sorted(a, b)
    print("Merged:", merged.to_list())
