/**
 * 🌐 fetchUniversal()
 * ------------------------------------------------------------
 * A powerful, all-in-one HTTP request helper that:
 *   ✅ Supports GET, POST, PUT, PATCH, DELETE
 *   ✅ Can send JSON bodies or URL query parameters(in GET)
 *   ✅ Handles JSON, text, and binary (Blob) responses
 *   ✅ Automatically downloads blob responses with user confirmation
 *   ✅ Has timeout + error handling
 *   ✅ can be imported and used in any JS project.
 *   ✅ Usage:
let data = await fetchUniversal("url", {
  method: "GET",
  payload: {},
  headers: {
    "Content-Type": "application/json",
    Authorization: "Bearer token_here",
  },
  timeout: 8000,
  onError: console.error,
});
 * @param {string} url - Target endpoint or file URL.
 * @param {Object} [options] - Optional settings.
 * @param {string} [options.method='GET'] - HTTP method (GET, POST, etc.).
 * @param {Object} [options.payload] - Request body (JSON or query for GET).
 * @param {Object} [options.headers] - Extra headers.
 * @param {number} [options.timeout=8000] - Timeout in milliseconds.
 * @param {Function} [options.onError=console.error] - Custom error handler.
 * @returns {Promise<any|null>} Parsed JSON, text, or Blob (auto-downloaded).
 * ------------------------------------------------------------
 */
async function fetchUniversal(url, options = {}) {
  // 🧩 Step 1: Extract optional settings with safe defaults
  const {
    method = "GET", // Default method is GET (most common)
    payload, // Optional body or query parameters( for GET)
    headers = {}, // Extra request headers (like auth)
    timeout = 8000, // Timeout in milliseconds
    onError = console.error, // Custom error handler function (default: console.error)
  } = options;

  try {
    // ✅ Step 2: Validate URL
    // URL must be a non-empty string, otherwise we abort early.
    if (typeof url !== "string" || !url.trim()) {
      onError("❌ Invalid URL provided.");
      return null;
    }

    // ✅ Step 3: Validate method
    // Only allow standard HTTP methods — prevents typos or invalid verbs.
    const allowedMethods = ["GET", "POST", "PUT", "PATCH", "DELETE"];
    if (!allowedMethods.includes(method.toUpperCase())) {
      onError(`⚠️ Invalid HTTP method: ${method}`);
      return null;
    }

    // 🧭 Step 4: Prepare the request
    let finalURL = url; // The URL that will actually be fetched
    let body; // Will hold request body if needed

    // 👉 Case 1: GET request with query params
    // Convert payload object into URL parameters (e.g., ?key=value)
    if (method === "GET" && payload && typeof payload === "object") {
      const query = new URLSearchParams(payload).toString();
      finalURL += (url.includes("?") ? "&" : "?") + query;
    }
    // 👉 Case 2: Non-GET requests (POST, PUT, etc.)
    // Payload becomes a JSON body, with appropriate header.
    else if (payload !== undefined) {
      body = JSON.stringify(payload);
      headers["Content-Type"] = "application/json";
    }

    // ⏳ Step 5: Setup timeout controller
    // If the server takes too long to respond, AbortController stops the request.
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeout);

    // 🚀 Step 6: Perform the actual HTTP request using fetch()
    const response = await fetch(finalURL, {
      method,
      headers,
      body,
      signal: controller.signal, // Used to cancel on timeout
    });

    // ✅ Clear timeout once response is received
    clearTimeout(timer);

    // ⚠️ Step 7: Handle non-OK HTTP statuses
    // fetch() doesn’t throw errors for 404/500 — we must handle it manually.
    if (!response.ok) {
      const map = {
        400: "⚠️ Bad Request.",
        401: "🔒 Unauthorized.",
        403: "🚫 Forbidden.",
        404: "❌ Not Found.",
        408: "⏱️ Request Timeout.",
        500: "💥 Server Error.",
      };
      onError(map[response.status] || `❌ HTTP ${response.status}`);
      return null;
    }

    // 🧩 Step 8: Detect and handle response content type
    const contentType = response.headers.get("content-type") || "";

    /*
    NOTE: in case of any file response, the server decides the content-type based on the file type.
    it is also true for the static files like pdf, images, audio, video, etc.,
    */

    // 📦 Case 1: JSON data → parse it automatically
    if (contentType.includes("application/json")) {
      return await response.json();
    }

    // 📝 Case 2: Plain text or HTML → return as string
    else if (contentType.includes("text/")) {
      return await response.text();
    }

    // 🎞️ Case 3: Binary / file data → handle as Blob
    else if (
      contentType.includes("application/") ||
      contentType.includes("image/") ||
      contentType.includes("audio/") ||
      contentType.includes("video/")
    ) {
      const blob = await response.blob(); // Convert response to binary Blob object

      // 💬 Ask user before auto-downloading (to prevent surprises)
      const shouldDownload = confirm(
        "📁 The server returned a file. Do you want to download it?"
      );
      if (shouldDownload) {
        // 🏷️ Try to extract a filename from the Content-Disposition header
        const disposition = response.headers.get("content-disposition");
        let filename = "downloaded_file";
        const match = disposition && disposition.match(/filename="?([^"]+)"?/);
        if (match) filename = match[1];
        // If no filename in header, try guessing from MIME type (e.g. image/png → .png)
        else if (contentType.startsWith("image/"))
          filename += "." + contentType.split("/")[1];
        // TODO (optional): You could also extract filename from the URL here.

        // 🧠 Create a temporary invisible <a> link to trigger browser download
        const blobUrl = URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = blobUrl;
        a.download = filename;
        a.style.display = "none";
        document.body.appendChild(a);
        a.click(); // Simulate a click to start download
        a.remove(); // Clean up link
        URL.revokeObjectURL(blobUrl); // Release memory
      }

      return blob; // Return blob in case caller wants to use it manually
    }

    // 🚫 Case 4: Unknown or empty response → return null
    else {
      return null;
    }
  } catch (error) {
    // 🧨 Step 9: Handle unexpected errors (network issues, timeout, etc.)
    const message =
      error.name === "AbortError"
        ? "⏱️ Request timed out."
        : `⚠️ Request failed: ${error.message}`;
    onError(message);
    return null;
  }
}
