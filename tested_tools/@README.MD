# tested_tools

`tested_tools` is a collection of **tested, reusable, and reliable tools** that can be directly used in projects.
Each tool in this directory has been verified through practical usage and is intended to save development time by avoiding reimplementation of common functionality.

This directory can be treated as a **lightweight Python package** and easily integrated into other projects.

---

## Purpose

- Store **production-ready** utilities
- Reuse common tools across multiple projects
- Maintain a clean separation between experiments and tested code
- Provide quick access to frequently used helpers

---

## Usage

You can use `tested_tools` in any Python project by adding it to your Python path.

Add the following lines at the top of your Python script:

```python
import sys
import os

sys.path.insert(1, os.path.join(os.path.dirname(__file__), "tested_tools"))
```

After this, you can directly import any module from `tested_tools`:

```python
from my_tool import some_function
```

---

## Structure Guidelines

- Each tool should be placed in its **own file or folder**
- Code must be:

  - Tested
  - Reusable
  - Well-documented

- Avoid experimental or unfinished code

Example structure:

```text
tested_tools/
├── file_utils.py
├── string_helpers.py
├── network_tools/
│   └── downloader.py
└── README.md
```

---

## Supported Languages

Although primarily used as a **Python utility package**, this folder may also contain tools written in other programming languages if they are:

- Well-tested
- Self-contained
- Clearly documented

---

## Best Practices

- Keep functions generic and configurable
- Avoid hardcoded paths or values
- Add docstrings and comments where necessary
- Update this README when adding major tools

---

## Notes

- This folder is intended for **stable tools only**
- Experimental or learning code should go elsewhere
- Tools here should be safe to reuse without modification
