
from flask import Flask, jsonify, request

app = Flask(__name__)

STUDENTS = [
    {"id": 1, "name": "Aditi"},
    {"id": 2, "name": "Rohan"}
]

@app.get("/")
def home():
    return "<h1>Cloud Demo Flask App</h1><p>Running in Docker. Try /health or /students.</p>"

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get("/students")
def list_students():
    return jsonify(STUDENTS)

@app.post("/students")
def add_student():
    data = request.get_json(silent=True) or {}
    if "name" not in data:
        return jsonify({"error": "name is required"}), 400
    new_id = max([s["id"] for s in STUDENTS] + [0]) + 1
    STUDENTS.append({"id": new_id, "name": data["name"]})
    return jsonify({"id": new_id, "name": data["name"]}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
