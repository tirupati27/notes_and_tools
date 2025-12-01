from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
            "ok": True,
            "detail": "welcome to home page."
        })

#*************************************************************
LOG_FILE_PATH = "uploads/user_activity_log.csv"
@app.route("/save_file", methods=["POST"])
def save_file():
    try:
        # Check if file is in the request
        if "file" not in request.files:
            return jsonify({"ok": False, "error": "No file part in request"})
        file = request.files["file"]
        # Save the file
        file.save(LOG_FILE_PATH)
        return jsonify({
            "ok": True,
            "message": "File saved successfully",
            "path": LOG_FILE_PATH
        })
    except Exception as e:
        return jsonify({
            "ok": False,
            "error": f"Server error: {str(e)}"
        })
@app.route("/get_file")
def return_log_file():
    try:
        return send_file(LOG_FILE_PATH)
    except Exception as e:
        return jsonify({
            "ok": False,
            "error": f"Server error: {str(e)}"
        })
#*************************************************************
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)