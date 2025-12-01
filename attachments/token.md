Perfect 👏 — that’s a **smart, lightweight idea** for a small LAN (local network) server — no need for full-blown OAuth or JWT if you just want simple user authentication with **random numbers (tokens)**.

Let’s design a **secure, clean workflow** that fits your exact use case.

---

## 🧩 **Goal**

You want:

* A **local FastAPI backend**
* Only **limited users** can connect
* Each user gets a **random code/token** for authentication
* Requests must include that token to be accepted

So — we’ll design a simple **Random Token Authentication System** ✅

---

## ⚙️ **Recommended Workflow**

### **1️⃣ Server generates and stores a random token**

When you (the admin) start the server, you generate a random token for each allowed user.

Example:

```python
import secrets

users = {
    "alice": secrets.token_hex(8),  # e.g., 'b3fa9d82acbe1d9e'
    "bob":   secrets.token_hex(8)
}
print("User tokens:", users)
```

You can print or share these short random numbers manually.

Each token acts as a **temporary password** for that LAN session.

---

### **2️⃣ Client uses token for every request**

The client (user) must include this in their requests — for example, in a header:

```
Authorization: Bearer b3fa9d82acbe1d9e
```

Or, for simplicity on a LAN, you can use a query param:

```
GET http://192.168.0.10:8000/data?token=b3fa9d82acbe1d9e
```

---

### **3️⃣ Backend validates token on every request**

You check whether the token exists in your `users` dictionary.

Example:

```python
from fastapi import FastAPI, HTTPException, Request

app = FastAPI()

# Example token store (in memory)
tokens = {
    "b3fa9d82acbe1d9e": "alice",
    "c2de98b7fe92f341": "bob"
}

@app.get("/data")
async def get_data(request: Request):
    # Option 1: from header
    auth = request.headers.get("Authorization")
    if auth and auth.startswith("Bearer "):
        token = auth.split(" ")[1]
    else:
        # Option 2: from query param
        token = request.query_params.get("token")

    if token not in tokens:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = tokens[token]
    return {"message": f"Hello {user}, here is your data!"}
```

✅ Works perfectly for LAN use — simple, fast, no heavy crypto.

---

### **4️⃣ (Optional) Add token expiry**

You can make tokens expire after, say, 1 hour:

```python
from datetime import datetime, timedelta

tokens = {
    "b3fa9d82acbe1d9e": {"user": "alice", "expires": datetime.utcnow() + timedelta(hours=1)}
}

def is_valid_token(token: str):
    info = tokens.get(token)
    if not info:
        return False
    if datetime.utcnow() > info["expires"]:
        del tokens[token]
        return False
    return True
```

---

### **5️⃣ (Optional) Add simple endpoint to get new token**

You can create a login endpoint (protected by a shared secret, password, or MAC address).

```python
from fastapi import Form

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "alice" and password == "mypassword":
        token = secrets.token_hex(8)
        tokens[token] = {"user": username, "expires": datetime.utcnow() + timedelta(hours=1)}
        return {"token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")
```

---

## 🧠 **Summary of the flow**

| Step                         | Description                              |
| ---------------------------- | ---------------------------------------- |
| **1. Generate tokens**       | Random numbers for each LAN user         |
| **2. Distribute tokens**     | Manually or via login endpoint           |
| **3. Clients send token**    | In `Authorization` header or query param |
| **4. Server verifies token** | Checks against stored token list         |
| **5. (Optional)**            | Add expiry, refresh, or revoke logic     |

---

### 🧾 Example request (curl)

```bash
curl -H "Authorization: Bearer b3fa9d82acbe1d9e" http://192.168.0.10:8000/data
```

Response:

```json
{
  "message": "Hello alice, here is your data!"
}
```

---

### ⚡ **Bonus ideas**

* Store tokens in a **JSON file** if you want them to persist between restarts.
* You can identify users by **IP + token** for even tighter control.
* Add a **simple web admin** route to list or revoke tokens manually.

---

Would you like me to show you a **complete ready-to-run FastAPI app** implementing this full LAN token system (with generation, expiry, and verification)?
