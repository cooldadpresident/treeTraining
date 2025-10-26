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


# -----------------------------
# Interactive chooser / stepper
# -----------------------------
def _choose_tree():
    print_header("Choose tree type")
    print("1) BST (binary search tree)")
    print("2) AVL (self-balancing AVL tree)")
    print("3) Max-Heap (array-backed)")
    choice = input("Select (1-3, or q to quit): ").strip()
    if choice == "1":
        t = BST()
        return "bst", t
    if choice == "2":
        t = AVL(verbose=True)
        return "avl", t
    if choice == "3":
        t = MaxHeap(verbose=True)
        return "heap", t
    return None, None


def _print_after_insert(tree_type, tree, val):
    # Show the tree after an insertion (or other op)
    if tree_type == "bst":
        printer = tree.printer()
        printer(tree.root, title=f"BST after inserting {val}")
    elif tree_type == "avl":
        # AVL already prints local steps when verbose=True; still show full tree
        printer = tree.printer()
        printer(tree.root, title=f"AVL after inserting {val}")
    elif tree_type == "heap":
        tree.ascii_print(title=f"Heap after inserting {val}")


def _step_through_sequence(tree_type, tree, seq):
    print_subheader(f"Stepping through sequence: {seq}")
    for x in seq:
        print_subheader(f"Insert {x}")
        tree.insert(x)
        _print_after_insert(tree_type, tree, x)
        ans = input("Press Enter to continue, or type 'q' to stop: ").strip().lower()
        if ans == "q":
            break


def _manual_mode(tree_type, tree):
    print_subheader("Manual insert mode — enter integers one at a time. Type 'done' to finish.")
    while True:
        s = input("Insert value (or 'done'): ").strip()
        if not s:
            continue
        if s.lower() == "done":
            break
        try:
            v = int(s)
        except ValueError:
            print("Please enter an integer or 'done'.")
            continue
        tree.insert(v)
        _print_after_insert(tree_type, tree, v)


def interactive_demo():
    """Interactive chooser and stepper for trees."""
    try:
        while True:
            tree_type, tree = _choose_tree()
            if tree_type is None:
                print_note("No selection — exiting interactive demo.")
                break

            while True:
                print_subheader(f"Selected: {tree_type.upper()}")
                print("1) Step through a demo sequence")
                print("2) Manual inserts (step after each)")
                print("3) Run full auto demo (non-interactive)")
                print("4) Choose another tree")
                print("q) Quit")
                cmd = input("Select option: ").strip().lower()
                if cmd == "1":
                    if tree_type == "bst":
                        seq = [10, 5, 15, 3, 7, 18]
                    elif tree_type == "avl":
                        seq = [10, 20, 30, 5, 4, 6]
                    else:  # heap
                        seq = [10, 5, 15, 3, 7, 18]
                    _step_through_sequence(tree_type, tree, seq)
                elif cmd == "2":
                    _manual_mode(tree_type, tree)
                elif cmd == "3":
                    # call existing full demos where applicable
                    if tree_type == "bst":
                        demo_bst()
                    elif tree_type == "avl":
                        demo_avl_longer_sequence()
                    elif tree_type == "heap":
                        demo_heap()
                elif cmd == "4":
                    break  # go back to choose tree
                elif cmd == "q":
                    print_note("Exiting interactive demo.")
                    return
                else:
                    print("Unknown option")
    except KeyboardInterrupt:
        print_note("Interactive demo interrupted — exiting.")


def main():
    # Start interactive chooser by default so user can step through operations
    interactive_demo()


if __name__ == "__main__":
    main()
