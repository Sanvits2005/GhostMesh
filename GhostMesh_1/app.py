from flask import Flask, render_template, jsonify
from generator import generate_attack, update_attacker
from model import predict, update_defender
import threading
import time

app = Flask(__name__)

logs = []
attacker_score = 0
defender_score = 0

def auto_generate():
    global attacker_score, defender_score

    while True:
        attack_type, features = generate_attack()
        result = predict(features)

        success = not result["anomaly"]

        update_attacker(attack_type, success)
        update_defender(features, result["anomaly"])

        if success:
            attacker_score += 1
        else:
            defender_score += 1

        log = {
            "id": len(logs) + 1,
            "attack": attack_type,
            "status": "Breached ⚠️" if success else "Blocked",
            "confidence": result["confidence"]
        }

        logs.append(log)
        time.sleep(2)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/logs")
def get_logs():
    return jsonify({
        "logs": logs[-10:],
        "attacker": attacker_score,
        "defender": defender_score
    })

if __name__ == "__main__":
    threading.Thread(target=auto_generate, daemon=True).start()
    app.run(debug=True, use_reloader=False, port=5001)
    
    