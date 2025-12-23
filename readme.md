# Knowledge Base & Search Tool

This repository serves as a **personal knowledge base and learning assistant**, containing notes, tools, cloned GitHub repositories, and a fast search utility to quickly access information across the entire project.

The core idea of this project is to **store, organize, and search learning materials efficiently**.

---

## Project Structure

```text
.
├── .Olevel/
├── github_repo/
├── other/
├── tested_tools/
├── text_notes/
├── clone_repo.py
├── config.json
├── helper.py
└── search.py
```

---

## Folder Descriptions

### `.Olevel/`

Contains all files, projects, and learning materials created during the **O-Level course**.

---

### `github_repo/`

Stores cloned GitHub repositories for **learning and content searching purposes**.

- The repositories inside this folder are used by `search.py`
- Content is **automatically updated** using the `clone_repo.py` script
- Helps in exploring real-world codebases and searching patterns across repositories

---

### `other/`

Contains notes and files that **do not fit** into the following categories:

- `tested_tools`
- `text_notes`

---

### `tested_tools/`

Contains **tested and reusable tools** written in any programming language.

- Tools in this folder are **production-ready**
- Can be directly reused in other projects
- Can be treated as a **Python package**

To use `tested_tools` in any Python project, add the following at the top of your script:

```python
import sys, os
sys.path.insert(1, os.path.join(os.path.dirname(__file__), "tested_tools"))
```

---

### `text_notes/`

A category for **human-readable, UTF-8 encoded, text-based notes**.

- Used for documentation
- Learning notes
- Concept explanations

---

## File Descriptions

### `clone_repo.py`

A Python script used to **clone and update GitHub repositories** into the `github_repo/` folder.

- Ensures repositories stay up-to-date
- Prepares content for searching and learning

---

### `config.json`

Configuration file used to **customize settings** for the search system.

- Acts as the **base configuration** for `search.py`
- Allows flexible tuning of search behavior

---

### `helper.py`

Contains **utility functions** and helper tools used by `search.py`.

---

### `search.py`

The **core of this project**.

- Provides fast searching across:

  - Notes
  - Tools
  - GitHub repositories

- Enables quick access to stored knowledge
- Designed for learning and productivity

---

## Purpose of This Project

- Centralize learning materials
- Store reusable tools
- Search across notes and real-world codebases
- Improve learning speed and accessibility
