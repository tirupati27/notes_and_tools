# 📘 Notes & Tools Viewer

A lightweight, modern web application for displaying **rich notes**, **search tags**, and **file attachments** with built-in previews for images, audio, video, and code files.
This project is designed to make studying, documentation, and resource browsing fast and visually clean.

---

## 🛠️ Project Structure (Read carefully)

```
/
├── .Olevel/              # All practical and project files learned during olevel
├── attachments/          # tools, PDF, images, videos, code files, etc.
├── highlightjs/          # Highlight.js library and themes
├── run.py                # A shortcut to open this app into the default browser. (also supported in termux)
├── app.html              # Main app shell
├── notes_body.html       # The actual Note content, loaded dynamically, it can also be run to read the notes
├── theme_backup.css      # default theme backup, copy and paste in the main app.
├── serialize.py          # serialize the notes body sections (run "python serialize.py" when needed)
└── README.md             # (This file)
```

---

## 🚀 Features

### ✅ **Dynamic Notes Loader**

- Loads external `notes_body.html` dynamically
- Automatically formats headings
- Converts tag lists into styled “search labels”
- Generates attachment buttons with preview support
- Theme can be customize by css variable through code editor

### ✅ **Attachment Preview System**

Supports preview for:

| Type            | Extensions                                     | Preview                 |
| --------------- | ---------------------------------------------- | ----------------------- |
| **Images**      | png, jpg, jpeg, gif, webp                      | Thumbnail preview       |
| **Audio**       | mp3, wav, ogg                                  | In-browser audio player |
| **Video**       | mp4, webm                                      | In-browser video player |
| **PDFs**        | pdf                                            | Embedded viewer         |
| **Code & Text** | py, js, ts, css, html, json, c, cpp, java, txt | Highlighted code block  |
| **Others**      | —                                              | Fallback iframe preview |

Built-in loading spinner for smooth UX.

### ✅ **Highlight.js Integration**

- Automatic code syntax highlighting
- Safe rendering with HTML escaping to prevent injection

### ✅ **Custom UI Elements**

- Custom “heading”, “search labels”, and “attachments” markup
- Automatic numbering of headings
- Smooth, minimal dark UI

---

## 📄 How It Works

### 1. **Loading Notes**

`app.html` fetches `notes_body.html`, parses it into DOM, and then:

- Processes `<heading>` → turns them into numbered section headers
- Processes `<searching_labels>` → transforms `tag1,, tag2` into styled chips
- Processes `<attachments>` → converts file list into previewable items

### 2. **Attachment Previewer**

On clicking an attachment:

- The selected file is sanitized
- A proper preview component is selected
- Loader shows until file is ready
- highlight.js is applied to code blocks

---

## 🔐 Security & Safety

This project includes:

- Filename sanitization to prevent HTML/JS injection
- Escaped code rendering
- Blocked dangerous characters in preview URLs
- Protection from malformed attachment names

---

## 📦 Setup & Usage

### 1. **Run locally**

Because the app uses `fetch()`, you must run it on a local server:

```sh
# Using Python 3
python3 -m http.server 9000
```

Then open:

```
http://127.0.0.1:9000/app.html
```

or simply `python run.py`

### 2. **Add Notes**

Edit `notes_body.html` and use these custom markup blocks:

```html
<section id="सेक्शन_1">
  <heading>my heading</heading>
  <searching_labels>tag1,, tag2,, tag3</searching_labels>
  <attachments>example.pdf,, image.png</attachments>
</section>
```

### 3. **Add Attachments**

Place any supported file inside the `/attachments/` folder.

---

## 🧪 Supported Custom Tags

| Tag                  | Purpose                                   |
| -------------------- | ----------------------------------------- |
| `<heading>`          | Automatically numbered title              |
| `<searching_labels>` | Converts text into search tag chips       |
| `<attachments>`      | Generates clickable attachments + preview |

---

## 🎨 Theme

Uses a dark theme inspired by:

- StackOverflow Dark (for code)
- Minimal neutral dark UI elements
- Custom highlight borders

---

## 📜 License

© 2025 Tirupati. All Rights Reserved
