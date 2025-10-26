#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List, Callable, Any, Tuple
import math

# =========
# Utilities
# =========

def print_header(title: str):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title))

def print_subheader(title: str):
    print("\n-- " + title)
"""
Compatibility wrapper. The original `trees.py` has been split into multiple
modules so individual tree implementations (BST, MaxHeap, AVL) can be studied
separately. This file re-exports the main classes for backward compatibility
and delegates demos to `demos.py`.
"""

from bst import BST, BSTNode
from heap import MaxHeap
from avl import AVL, AVLNode

# Re-exported helpers (optional)
from utils import print_header, print_subheader, print_note, make_tree_printer


if __name__ == "__main__":
    # Run demos (keeps previous behaviour)
    from demos import main
    main()