# Algorithms — Trees (split modules)

This repository contains educational implementations and demos of several tree
and heap data structures used for learning and visualization.

Modules
- `utils.py` — helpers and ASCII tree printer
- `bst.py` — binary search tree (BST)
- `heap.py` — max-heap (array-backed) and ASCII view
- `avl.py` — AVL balanced BST with rotations and verification
- `demos.py` — runnable demos that show step-by-step behavior
- `trees.py` — compatibility wrapper that re-exports main classes and runs demos

Usage

Run demos (prints step-by-step operations):

```sh
python3 trees.py
# or
python3 demos.py
```

Import individual modules for interactive learning:

```py
from bst import BST
b = BST(); b.insert(10); b.printer()(b.root)
```

Next steps
- If you want this pushed to a remote (GitHub/GitLab), provide the remote URL
  and I can add it and push, or you can add it yourself with:

```sh
git remote add origin <REMOTE_URL>
git push -u origin main
```
