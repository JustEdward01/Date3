from flask import Flask, render_template, request, jsonify
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/choice", methods=["POST"])
def choice():
    data = request.get_json() or {}
    option = data.get("option")
    date_picked = data.get("date")  # <--- Aici prindem data

    # Printeaza in Log-urile serverului
    print(f"========================================", file=sys.stderr)
    print(f"💌 ALEGERE: {option}", file=sys.stderr)
    print(f"📅 DATA:    {date_picked}", file=sys.stderr)
    print(f"========================================", file=sys.stderr)

    return jsonify({"status": "ok", "received": option})

if __name__ == "__main__":
    app.run(debug=True)