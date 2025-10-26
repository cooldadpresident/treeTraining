from utils import print_header, print_subheader, print_note
from bst import BST
from heap import MaxHeap
from avl import AVL


def demo_bst():
    print_header("BST demo")
    bst = BST()
    seq = [10, 5, 15, 3, 7, 18]
    for x in seq:
        print_subheader(f"Insert {x}")
        bst.insert(x)
        bst.printer()(bst.root, title=f"BST after inserting {x}")
    print_note(f"In-order traversal (sorted): {bst.inorder()}")
    print_note(f"BST property OK: {bst.verify_bst()}")


def demo_heap():
    print_header("Max-Heap demo (level-wise)")
    heap = MaxHeap(verbose=True)
    seq = [10, 5, 15, 3, 7, 18]
    for x in seq:
        heap.insert(x)
        heap.ascii_print(title="Heap as tree")
    print_note(f"Heap property OK: {heap.verify_heap()}")
    print_subheader("Pop max repeatedly")
    while heap.a:
        heap.pop_max()


def demo_avl_rotations():
    print_header("AVL demo with step-by-step rotations")
    # Each sequence chosen to trigger a specific imbalance
    cases = [
        ("RR case (expect single left rotation)", [10, 20, 30]),
        ("LL case (expect single right rotation)", [30, 20, 10]),
        ("LR case (expect left-right double rotation)", [30, 10, 20]),
        ("RL case (expect right-left double rotation)", [10, 30, 20]),
    ]
    for title, seq in cases:
        print_subheader(title)
        avl = AVL(verbose=True)
        for x in seq:
            avl.insert(x)
        print_note(f"In-order: {avl.inorder()}")
        print_note(f"AVL OK: {avl.verify_avl()}")


def demo_avl_longer_sequence():
    print_header("AVL demo on a longer sequence")
    avl = AVL(verbose=True)
    seq = [50, 25, 75, 10, 40, 60, 90, 5, 35, 45, 55, 65, 85, 95, 80]
    for x in seq:
        avl.insert(x)
    print_note(f"In-order: {avl.inorder()}")
    print_note(f"AVL OK: {avl.verify_avl()}")


def main():
    demo_bst()
    demo_heap()
    demo_avl_rotations()
    demo_avl_longer_sequence()


if __name__ == "__main__":
    main()
