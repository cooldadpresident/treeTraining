from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass
from utils import print_subheader, print_note, make_tree_printer

class MaxHeap:
    def __init__(self, verbose: bool = True):
        self.a: List[int] = []
        self.verbose = verbose

    def insert(self, x: int):
        self.a.append(x)
        if self.verbose:
            print_subheader(f"Insert {x} into heap (append at end)")
            self.print_levels()
        self._bubble_up(len(self.a)-1)

    def pop_max(self) -> Optional[int]:
        if not self.a:
            return None
        mx = self.a[0]
        last = self.a.pop()
        if self.a:
            self.a[0] = last
            if self.verbose:
                print_subheader(f"Pop max -> move last {last} to root and heapify down")
            self._bubble_down(0)
        if self.verbose:
            print_note(f"Returned {mx}")
            self.print_levels()
        return mx

    def _bubble_up(self, i: int):
        while i > 0:
            p = (i - 1) // 2
            if self.a[i] > self.a[p]:
                if self.verbose:
                    print_note(f"Bubble up: swap {self.a[i]} (idx {i}) with parent {self.a[p]} (idx {p})")
                self.a[i], self.a[p] = self.a[p], self.a[i]
                i = p
                if self.verbose:
                    self.print_levels()
            else:
                break

    def _bubble_down(self, i: int):
        n = len(self.a)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < n and self.a[l] > self.a[largest]:
                largest = l
            if r < n and self.a[r] > self.a[largest]:
                largest = r
            if largest == i:
                break
            if self.verbose:
                print_note(f"Bubble down: swap {self.a[i]} (idx {i}) with child {self.a[largest]} (idx {largest})")
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            i = largest
            if self.verbose:
                self.print_levels()

    def verify_heap(self) -> bool:
        for i in range(len(self.a)):
            l = 2 * i + 1
            r = 2 * i + 2
            if l < len(self.a) and self.a[i] < self.a[l]:
                return False
            if r < len(self.a) and self.a[i] < self.a[r]:
                return False
        return True

    def print_levels(self):
        # Level-wise display to visualize the complete tree shape
        n = len(self.a)
        if n == 0:
            print("(empty heap)")
            return
        level = 0
        start = 0
        while start < n:
            end = min(n, start + 2**level)
            level_vals = " ".join(f"{self.a[i]:>3}" for i in range(start, end))
            print(f"  level {level}: {level_vals}")
            start = end
            level += 1

    def to_tree_for_printing(self):
        # Build a temporary pointer-based tree to reuse the ASCII printer
        @dataclass
        class Node:
            key: int
            left: Optional['Node'] = None
            right: Optional['Node'] = None
        if not self.a:
            return None
        nodes = [Node(v) for v in self.a]
        for i in range(len(self.a)):
            l = 2*i + 1
            r = 2*i + 2
            if l < len(self.a):
                nodes[i].left = nodes[l]
            if r < len(self.a):
                nodes[i].right = nodes[r]
        return nodes[0]

    def ascii_print(self, title: Optional[str] = None):
        root = self.to_tree_for_printing()
        printer = make_tree_printer(
            label=lambda n: f"{n.key}",
            left=lambda n: n.left,
            right=lambda n: n.right,
        )
        printer(root, title=title)
