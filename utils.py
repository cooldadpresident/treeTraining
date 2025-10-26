from __future__ import annotations
from typing import Optional, Callable, Any

# =========
# Utilities
# =========

def print_header(title: str):
    print("\n" + "=" * len(title))
    print(title)
    print("=" * len(title))


def print_subheader(title: str):
    print("\n-- " + title)


def print_note(text: str):
    print(f"  • {text}")


def make_tree_printer(
    label: Callable[[Any], str],
    left: Callable[[Any], Optional[Any]],
    right: Callable[[Any], Optional[Any]],
):
    """
    Returns a function print_tree(node) that prints a binary tree with nice ASCII branches.
    """
    def print_tree(node: Optional[Any], title: Optional[str] = None):
        if title:
            print_subheader(title)
        if not node:
            print("(empty)")
            return

        def _print(n, prefix="", is_tail=True):
            print(prefix + ("└── " if is_tail else "├── ") + label(n))
            children = [c for c in [left(n), right(n)] if c is not None]
            for i, child in enumerate(children):
                last = (i == len(children) - 1)
                _print(child, prefix + ("    " if is_tail else "│   "), last)

        _print(node)
    return print_tree
