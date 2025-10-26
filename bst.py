from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List
from utils import make_tree_printer

@dataclass
class BSTNode:
    key: int
    left: Optional['BSTNode'] = None
    right: Optional['BSTNode'] = None

class BST:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: int):
        def _ins(n: Optional[BSTNode], k: int) -> BSTNode:
            if n is None:
                return BSTNode(k)
            if k < n.key:
                n.left = _ins(n.left, k)
            elif k > n.key:
                n.right = _ins(n.right, k)
            # duplicates ignored
            return n
        self.root = _ins(self.root, key)

    def inorder(self) -> List[int]:
        res: List[int] = []
        def _in(n: Optional[BSTNode]):
            if not n: return
            _in(n.left); res.append(n.key); _in(n.right)
        _in(self.root)
        return res

    def verify_bst(self) -> bool:
        arr = self.inorder()
        return all(arr[i] < arr[i+1] for i in range(len(arr)-1))

    def printer(self):
        return make_tree_printer(
            label=lambda n: f"{n.key}",
            left=lambda n: n.left,
            right=lambda n: n.right,
        )
