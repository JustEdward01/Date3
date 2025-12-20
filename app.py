from flask import Flask, render_template, request, jsonify
import sys
import logging

app = Flask(__name__)

# Configurare Logging (Ca să vezi mesajele în Render)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

@app.route("/")
def index():
    # Asta se intampla cand intra pe site
    print("--- 🟢 Cineva a accesat pagina de start (Puzzle) ---", flush=True)
    return render_template("index.html")

@app.route("/claim", methods=["POST"])
def claim():
    try:
        # 1. Primim datele de la telefonul ei
        data = request.get_json() or {}
        moves = data.get("moves", 0)
        time_spent = data.get("time", 0)
        used_bypass = data.get("used_bypass", False) # Verificam daca a trisat

        # 2. Scriem RAPORTUL in consola ta
        print(f"\n\n", flush=True)
        print(f"========================================", flush=True)
        print(f"🏆  MISSION ACCOMPLISHED! DATE #4 SECURED!", flush=True)
        print(f"========================================", flush=True)
        
        if used_bypass:
            print(f"⚠️  METODA:  EMERGENCY OVERRIDE (A folosit butonul Stuck)", flush=True)
            print(f"🤖  STATUS:  HACKED THE SYSTEM", flush=True)
        else:
            print(f"🧠  METODA:  PURE SKILL (Rezolvat corect)", flush=True)
            print(f"🧩  MUTARI:  {moves}", flush=True)
            print(f"⏱️  TIMP:    {time_spent} secunde", flush=True)
            
        print(f"========================================", flush=True)
        print(f"\n\n", flush=True)

        # 3. Trimitem confirmarea inapoi la telefon ca sa apara "Claimed ✅"
        return jsonify({"status": "ok", "message": "Date secured"})
    
    except Exception as e:
        print(f"❌ EROARE: {e}", flush=True)
        return jsonify({"status": "error"}), 500

if __name__ == "__main__":

    app.run(debug=True)
