from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Tuple
from utils import make_tree_printer, print_subheader, print_note

@dataclass
class AVLNode:
    key: int
    left: Optional['AVLNode'] = None
    right: Optional['AVLNode'] = None
    height: int = 1  # leaf height = 1

class AVL:
    """
    Balance Factor (BF) = height(right) - height(left)
    Valid BF in {-1, 0, +1}; if BF < -1 => left-heavy; if BF > +1 => right-heavy.
    """
    def __init__(self, verbose: bool = True):
        self.root: Optional[AVLNode] = None
        self.verbose = verbose

    # --- helpers ---
    def h(self, n: Optional[AVLNode]) -> int:
        return n.height if n else 0

    def bf(self, n: Optional[AVLNode]) -> int:
        return (self.h(n.right) - self.h(n.left)) if n else 0

    def update(self, n: AVLNode):
        n.height = max(self.h(n.left), self.h(n.right)) + 1

    # Pretty printer
    def printer(self):
        return make_tree_printer(
            label=lambda n: f"{n.key} [h={n.height}, bf={self.bf(n)}]",
            left=lambda n: n.left,
            right=lambda n: n.right,
        )

    # --- rotations ---
    def rotate_left(self, z: AVLNode) -> AVLNode:
        y = z.right
        assert y is not None, "rotate_left needs right child"
        T2 = y.left

        if self.verbose:
            self._print_local("Before rotate_left", z)

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights (child first, then parent)
        self.update(z)
        self.update(y)

        if self.verbose:
            print_note("Rotate left (RR case fix): pivot is right child becomes new root of this subtree")
            self._print_local("After rotate_left", y)

        return y

    def rotate_right(self, z: AVLNode) -> AVLNode:
        y = z.left
        assert y is not None, "rotate_right needs left child"
        T2 = y.right

        if self.verbose:
            self._print_local("Before rotate_right", z)

        # Perform rotation
        y.right = z
        z.left = T2

        # Update heights
        self.update(z)
        self.update(y)

        if self.verbose:
            print_note("Rotate right (LL case fix): pivot is left child becomes new root of this subtree")
            self._print_local("After rotate_right", y)

        return y

    def _rebalance(self, n: AVLNode) -> AVLNode:
        self.update(n)
        b = self.bf(n)
        if b < -1:
            # Left heavy: LL or LR
            if self.bf(n.left) <= 0:
                if self.verbose:
                    print_note(f"Imbalance at {n.key}: BF={b} (left-heavy), child BF={self.bf(n.left)} -> LL case")
                return self.rotate_right(n)
            else:
                if self.verbose:
                    print_note(f"Imbalance at {n.key}: BF={b} (left-heavy), child BF={self.bf(n.left)} -> LR case")
                n.left = self.rotate_left(n.left)  # first rotate child left
                return self.rotate_right(n)        # then rotate current right
        elif b > 1:
            # Right heavy: RR or RL
            if self.bf(n.right) >= 0:
                if self.verbose:
                    print_note(f"Imbalance at {n.key}: BF={b} (right-heavy), child BF={self.bf(n.right)} -> RR case")
                return self.rotate_left(n)
            else:
                if self.verbose:
                    print_note(f"Imbalance at {n.key}: BF={b} (right-heavy), child BF={self.bf(n.right)} -> RL case")
                n.right = self.rotate_right(n.right)  # first rotate child right
                return self.rotate_left(n)            # then rotate current left
        return n

    # --- insertion ---
    def insert(self, key: int):
        if self.verbose:
            print_subheader(f"Insert {key} into AVL")

        def _ins(n: Optional[AVLNode], k: int) -> AVLNode:
            if not n:
                if self.verbose:
                    print_note(f"Insert new leaf {k}")
                return AVLNode(k)
            if k < n.key:
                n.left = _ins(n.left, k)
            elif k > n.key:
                n.right = _ins(n.right, k)
            else:
                if self.verbose:
                    print_note(f"Duplicate {k} ignored")
                return n
            # Rebalance on unwind
            n = self._rebalance(n)
            return n

        self.root = _ins(self.root, key)
        if self.verbose:
            self.printer()(self.root, title=f"AVL after inserting {key}")

    # --- verification ---
    def inorder(self) -> List[int]:
        res: List[int] = []
        def _in(n: Optional[AVLNode]):
            if not n: return
            _in(n.left); res.append(n.key); _in(n.right)
        _in(self.root)
        return res

    def verify_bst(self) -> bool:
        a = self.inorder()
        return all(a[i] < a[i+1] for i in range(len(a)-1))

    def _verify_bf(self, n: Optional[AVLNode]) -> Tuple[bool, Optional[int]]:
        if not n: return True, 0
        okL, hL = self._verify_bf(n.left)
        okR, hR = self._verify_bf(n.right)
        if not okL or not okR:
            return False, None
        bf = hR - hL
        if bf < -1 or bf > 1:
            return False, None
        return True, max(hL, hR) + 1

    def verify_avl(self) -> bool:
        ok, _ = self._verify_bf(self.root)
        return ok and self.verify_bst()

    # local subtree pretty snapshot
    def _print_local(self, title: str, node: AVLNode):
        printer = self.printer()
        printer(node, title=title)
