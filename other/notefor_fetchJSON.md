Excellent — let’s make this a **clear, full-length guide** you can drop into any project’s documentation or readme.
Here’s a **verbose explanation** on how to use your `fetchJSON()` utility — written in a developer-friendly and professional way.

---

# 🧠 `fetchJSON(url, options)` — Universal JSON Fetch Utility

This function is a **robust, reusable helper** designed to fetch JSON data from any API endpoint or static JSON file, with built-in **error handling, timeout support**, and **customizable error callbacks**.

You can use it in **any front-end JavaScript project**, including plain JS, FastAPI templates, or frameworks like React, Vue, and Svelte.

---

## ⚙️ 1. Function Overview

```js
/**
 * Fetch JSON data from any given URL with robust error handling and timeout support.
 *
 * @param {string} url - The endpoint URL to fetch JSON from.
 * @param {Object} [options] - Optional settings.
 * @param {number} [options.timeout=8000] - Timeout in milliseconds (default: 8s).
 * @param {Function} [options.onError=alert] - Custom error handler (default: alert).
 * @returns {Promise<Object|null>} - Parsed JSON object if successful, or null if failed.
 */
async function fetchJSON(url, options = {}) {
  const { timeout = 8000, onError = alert } = options;

  try {
    if (typeof url !== "string" || !url.trim()) {
      onError("❌ Invalid URL provided.");
      return null;
    }

    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeout);

    const response = await fetch(url, { signal: controller.signal });
    clearTimeout(timer);

    if (!response.ok) {
      let message = `❌ Error ${response.status}: ${response.statusText}`;
      if (response.status === 404) message = "❌ Resource not found.";
      else if (response.status === 500)
        message = "❌ Server error. Please try again later.";
      else if (response.status === 403) message = "🚫 Access denied.";
      else if (response.status === 0) message = "🌐 Network connection failed.";

      onError(message);
      return null;
    }

    const data = await response.json();

    if (data === null || (typeof data !== "object" && !Array.isArray(data))) {
      onError("⚠️ The server did not return valid JSON data.");
      return null;
    }

    return data;
  } catch (error) {
    const message =
      error.name === "AbortError"
        ? "⏱️ Request timed out."
        : `⚠️ Failed to fetch data.\nReason: ${error.message}`;
    onError(message);
    return null;
  }
}
```

---

## 🧩 2. Basic Usage Example

### Fetching from a backend endpoint

```js
async function loadData() {
  const data = await fetchJSON("/api/icon-map");

  if (data) {
    console.log("✅ Received JSON:", data);
  } else {
    console.log("❌ No data received.");
  }
}

loadData();
```

When the URL responds correctly (e.g. your FastAPI endpoint `/api/icon-map`),
the function parses the JSON and returns it as a regular JavaScript object.

If something goes wrong (timeout, 404, bad JSON), it shows a readable alert like:

```
❌ Resource not found.
```

and returns `null`.

---

## ⚙️ 3. Customizing Behavior

### 🔸 Custom Timeout

You can specify a custom timeout (in milliseconds):

```js
const data = await fetchJSON("/api/slow-endpoint", { timeout: 12000 });
```

If the server takes longer than 12 seconds, the request automatically aborts and you’ll see:

```
⏱️ Request timed out.
```

---

### 🔸 Custom Error Handling

By default, the function shows errors using `alert()`.
You can override this by passing your own handler:

```js
await fetchJSON("/api/icon-map", {
  onError: (message) => {
    const errorBox = document.getElementById("error");
    if (errorBox) errorBox.textContent = message;
  },
});
```

This is useful for UI-based apps where you want to show the message inside your webpage instead of popup alerts.

---

## 🧠 4. What It Returns

- On **success:**
  → Returns the parsed JSON object or array.
  Example:

  ```js
  const data = await fetchJSON("/api/icon-map");
  console.log(data.icon_map);
  ```

- On **failure:**
  → Returns `null` and triggers your `onError` handler.

This allows clean conditional logic:

```js
const data = await fetchJSON("/api/icon-map");
if (!data) return; // stop if failed
// continue otherwise...
```

---

## 🔐 5. Handling Different Response Scenarios

| Scenario                  | Behavior                                                         |
| ------------------------- | ---------------------------------------------------------------- |
| Valid JSON (200 OK)       | Returns parsed object                                            |
| 404 Not Found             | Calls `onError("❌ Resource not found.")`, returns `null`        |
| 500 Internal Server Error | Calls `onError("❌ Server error. Please try again later.")`      |
| Timeout                   | Calls `onError("⏱️ Request timed out.")`                         |
| Network disconnected      | Calls `onError("🌐 Network connection failed.")`                 |
| Invalid JSON              | Calls `onError("⚠️ The server did not return valid JSON data.")` |

---

## 🛠️ 6. Example with FastAPI Backend

### Backend (`main.py`)

```python
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/api/icon-map")
def get_icon_map():
    return JSONResponse(content={
        "icon_map": {
            "image.png": ["jpg", "jpeg", "png"],
            "pdf.png": ["pdf"],
        }
    })
```

### Frontend (`index.html`)

```html
<script>
  (async () => {
    const data = await fetchJSON("/api/icon-map");
    if (data) {
      console.log("Got:", data.icon_map);
    }
  })();
</script>
```

✅ Works directly — FastAPI returns JSON, your function fetches and parses it safely.

---

## 🧱 7. Why Use This Utility

| Feature                 | Benefit                             |
| ----------------------- | ----------------------------------- |
| ✅ Timeout support      | Prevents hanging requests           |
| ✅ Custom error handler | Control how users see errors        |
| ✅ Detailed messages    | Easier debugging                    |
| ✅ Works anywhere       | Vanilla JS, React, Vue, etc.        |
| ✅ No dependencies      | 100% native JavaScript              |
| ✅ Robust validation    | Detects bad URLs and malformed JSON |

---

## 💡 8. Tips for Real-World Use

- Always **await** the function (it’s asynchronous).
- Prefer relative URLs (`/api/...`) for same-origin requests.
- For APIs requiring authentication, you can extend it easily by adding headers:

  ```js
  const response = await fetch(url, {
    signal: controller.signal,
    headers: { Authorization: "Bearer " + token },
  });
  ```

---

## ✅ In Short

| You want to...              | How to do it                                          |
| --------------------------- | ----------------------------------------------------- |
| Fetch JSON                  | `await fetchJSON("/api/data")`                        |
| Change timeout              | `{ timeout: 5000 }`                                   |
| Handle errors in custom way | `{ onError: (msg) => showError(msg) }`                |
| Use anywhere                | Drop this function into any project — no setup needed |

---

Would you like me to show how to **extend it for POST/PUT requests** (to also send JSON data to the backend in the same style)?
