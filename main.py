from flask import Flask, jsonify
from pydantic import BaseModel
import requests

app = Flask(__name__)

class HealthResponse(BaseModel):
    status: str
    healthy: bool

@app.route("/")
def index():
    return jsonify({"status": "ok", "message": "Bad version test"})

@app.route("/health")
def health():
    resp = HealthResponse(status="ok", healthy=True)
    return jsonify(resp.model_dump())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
