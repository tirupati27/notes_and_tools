To perform **platform-independent file operations** (like rename, move, delete, copy, etc.) in **Python**, you should use the **standard library modules** — mainly `os`, `shutil`, and `pathlib`.
These work consistently across **Windows, macOS, and Linux**.

Here’s a breakdown of how to use them:

---

### 🧩 1. Using `os` module

#### ✅ Rename a file or directory

```python
import os

# Rename file
os.rename("old_name.txt", "new_name.txt")

# Rename directory
os.rename("old_folder", "new_folder")
```

#### ✅ Delete a file

```python
os.remove("file_to_delete.txt")
```

#### ✅ Delete an empty directory

```python
os.rmdir("empty_folder")
```

> ⚠️ `os.rmdir()` only removes _empty_ directories.

---

### 🧰 2. Using `shutil` module

For more advanced file operations (copying, moving, recursive deletion, etc.):

#### ✅ Move a file or directory

```python
import shutil

shutil.move("source.txt", "destination_folder/")
```

#### ✅ Copy a file

```python
shutil.copy("source.txt", "copy.txt")  # copy only content and permissions
```

#### ✅ Copy a directory (recursively)

```python
shutil.copytree("source_folder", "destination_folder")
```

#### ✅ Delete a directory (recursively)

```python
shutil.rmtree("folder_to_delete")
```

---

### 🪶 3. Using `pathlib` (modern & recommended)

`pathlib` provides an **object-oriented** and **cross-platform** interface for file paths.

#### ✅ Example:

```python
from pathlib import Path

# Define a path
p = Path("example.txt")

# Rename
p.rename("renamed_example.txt")

# Delete
p.unlink()  # same as os.remove()

# Move
p.replace("new_folder/renamed_example.txt")

# Create directories (if not exist)
Path("new_folder/sub_folder").mkdir(parents=True, exist_ok=True)
```

---

### 🧼 Summary Table

| Operation        | `os`          | `shutil`                             | `pathlib`                     |
| ---------------- | ------------- | ------------------------------------ | ----------------------------- |
| Rename           | `os.rename()` | —                                    | `Path.rename()`               |
| Move             | —             | `shutil.move()`                      | `Path.replace()`              |
| Delete file      | `os.remove()` | —                                    | `Path.unlink()`               |
| Delete folder    | `os.rmdir()`  | `shutil.rmtree()`                    | `Path.rmdir()` _(empty only)_ |
| Copy file/folder | —             | `shutil.copy()`, `shutil.copytree()` | —                             |

---

### ✅ Recommended Modern Approach

Use **`pathlib`** for most file operations — it’s readable, safe, and fully cross-platform:

```python
from pathlib import Path
import shutil

# Setup
src = Path("data.txt")
dst_dir = Path("backup")

# Move
dst_dir.mkdir(exist_ok=True)
src.replace(dst_dir / src.name)

# Copy
shutil.copy(dst_dir / src.name, Path("copy_of_data.txt"))

# Delete
(src.parent / "copy_of_data.txt").unlink()
```

---

Would you like me to show an **example script** that performs all these operations safely with error handling (try/except + existence checks)?
