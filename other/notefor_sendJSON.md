Perfect 👌 — since you liked the `fetchJSON()` function, let’s now make its **sibling utility** — a universal, robust, and developer-friendly function to **send JSON data** to your backend using `POST`, `PUT`, `PATCH`, or even `DELETE`.

This will follow the same philosophy:
✅ minimal boilerplate,
✅ human-readable errors,
✅ timeout handling,
✅ fully reusable across projects.

---

# 🚀 `sendJSON(url, payload, options)` — Universal JSON Sender Utility

This function allows you to **send JSON data** to an API endpoint safely and consistently.
It complements `fetchJSON()` by handling requests **with a body**, such as:

- `POST` (create data)
- `PUT` (replace data)
- `PATCH` (update data)
- `DELETE` (delete resource)

---

## 🧠 Full Function Code

```js
/**
 * Send JSON data to a backend endpoint with robust error handling and timeout support.
 *
 * @param {string} url - The endpoint URL to send the request to.
 * @param {Object} payload - The data object to send as JSON.
 * @param {Object} [options] - Optional settings.
 * @param {string} [options.method="POST"] - HTTP method (POST, PUT, PATCH, DELETE).
 * @param {number} [options.timeout=8000] - Timeout in milliseconds (default: 8s).
 * @param {Function} [options.onError=alert] - Custom error handler (default: alert).
 * @returns {Promise<Object|null>} - Parsed JSON response if available, or null if failed.
 *
 * Usage:
 *   const response = await sendJSON("/api/upload", { name: "Tirupati" }, { method: "POST" });
 */
async function sendJSON(url, payload = {}, options = {}) {
  const { method = "POST", timeout = 8000, onError = alert } = options;

  try {
    // ✅ Validate URL
    if (typeof url !== "string" || !url.trim()) {
      onError("❌ Invalid URL provided.");
      return null;
    }

    // ✅ Validate method
    const allowedMethods = ["POST", "PUT", "PATCH", "DELETE"];
    if (!allowedMethods.includes(method.toUpperCase())) {
      onError(
        `⚠️ Invalid HTTP method: ${method}. Use POST, PUT, PATCH, or DELETE.`
      );
      return null;
    }

    // ⏳ Setup timeout controller
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeout);

    // 🔄 Perform request
    const response = await fetch(url, {
      method,
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
      signal: controller.signal,
    });

    clearTimeout(timer);

    // ⚠️ Handle non-successful HTTP status codes
    if (!response.ok) {
      let message = `❌ Error ${response.status}: ${response.statusText}`;
      if (response.status === 404) message = "❌ Endpoint not found.";
      else if (response.status === 400)
        message = "⚠️ Bad request. Check your payload.";
      else if (response.status === 500) message = "💥 Server error.";
      else if (response.status === 403) message = "🚫 Access denied.";
      else if (response.status === 0) message = "🌐 Network error.";

      onError(message);
      return null;
    }

    // 🧩 Try parsing JSON response (if any)
    try {
      const data = await response.json();
      return data;
    } catch {
      // Some APIs respond with no JSON (e.g., 204 No Content)
      return null;
    }
  } catch (error) {
    const message =
      error.name === "AbortError"
        ? "⏱️ Request timed out."
        : `⚠️ Failed to send data.\nReason: ${error.message}`;
    onError(message);
    return null;
  }
}
```

---

## 💡 Example 1: POST (Create Data)

```js
(async () => {
  const payload = {
    name: "Tirupati Bala",
    email: "balaji274401@gmail.com",
  };

  const response = await sendJSON("/api/users", payload);

  if (response) {
    console.log("✅ Server replied:", response);
  } else {
    console.log("❌ Request failed.");
  }
})();
```

✅ Sends a `POST` request with your JSON object.
If the backend returns JSON, it’s parsed automatically.

---

## 💡 Example 2: PUT (Update Resource)

```js
await sendJSON("/api/users/42", { name: "Updated Name" }, { method: "PUT" });
```

---

## 💡 Example 3: DELETE

```js
await sendJSON("/api/users/42", {}, { method: "DELETE" });
```

Even though `DELETE` often doesn’t need a body, the function allows an optional payload if your backend expects one.

---

## 💡 Example 4: Custom Timeout & Error UI

```js
await sendJSON(
  "/api/submit",
  { message: "Hello!" },
  {
    timeout: 10000,
    onError: (msg) => {
      const errDiv = document.getElementById("error-box");
      errDiv.textContent = msg;
      errDiv.style.display = "block";
    },
  }
);
```

✅ This will show your custom message in the UI instead of an alert box.

---

## 🧱 How It Works (Step-by-Step)

1. **Validates** your inputs (URL, HTTP method).
2. Creates an **AbortController** for timeout safety.
3. Sends the request with `Content-Type: application/json`.
4. **Waits** for a response or times out.
5. If the response status is not 200–299, it calls your `onError` handler.
6. If the backend replies with JSON, it parses and returns it.
7. If the backend replies with no body (like HTTP 204), returns `null`.

---

## 🧰 Use Both Functions Together

Here’s how your toolkit might look in your projects:

```js
// fetchJSON.js
async function fetchJSON(...) { /* same as before */ }

// sendJSON.js
async function sendJSON(...) { /* as above */ }
```

You can import them both and use:

```js
const data = await fetchJSON("/api/settings");
const result = await sendJSON("/api/save", data);
```

---

## ✅ Summary Table

| Action                            | Function                          | Example                                           |
| --------------------------------- | --------------------------------- | ------------------------------------------------- |
| Fetch JSON (GET)                  | `fetchJSON(url)`                  | `await fetchJSON("/api/icon-map")`                |
| Send JSON (POST/PUT/PATCH/DELETE) | `sendJSON(url, payload, options)` | `await sendJSON("/api/upload", { name: "test" })` |
| Timeout                           | `timeout` option                  | `{ timeout: 5000 }`                               |
| Custom error                      | `onError` callback                | `{ onError: msg => showError(msg) }`              |

---

Would you like me to make a **common wrapper module** (e.g. `apiClient.js`) that exports both `fetchJSON()` and `sendJSON()` together — ready to import anywhere?
That way, you can just do:

```js
import { fetchJSON, sendJSON } from "./apiClient.js";
```
