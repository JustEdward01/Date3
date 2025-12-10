from flask import Flask, render_template, request, jsonify
import sys
import logging

app = Flask(__name__)

# Configurare Logging pentru Render (ca să fii sigur că vezi tot)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

@app.route("/")
def index():
    # Asta apare cand cineva intra pe site
    print("--- 🟢 Cineva a accesat pagina de start ---", flush=True)
    return render_template("index.html")

@app.route("/choice", methods=["POST"])
def choice():
    try:
        data = request.get_json() or {}
        option = data.get("option", "Nicio optiune")
        date_picked = data.get("date", "Nicio data")

        # --- AICI ESTE SECRETUL: flush=True ---
        print(f"\n\n", flush=True)
        print(f"========================================", flush=True)
        print(f"💌  ALEGERE: {option}", flush=True)
        print(f"📅  DATA:    {date_picked}", flush=True)
        print(f"========================================", flush=True)
        print(f"\n\n", flush=True)
        # ---------------------------------------

        return jsonify({"status": "ok", "received": option})
    except Exception as e:
        print(f"❌ EROARE: {e}", flush=True)
        return jsonify({"status": "error"}), 500

if __name__ == "__main__":
    app.run(debug=True)