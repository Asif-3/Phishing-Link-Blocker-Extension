from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib.parse import urlparse
import re

app = Flask(__name__)
CORS(app)

SUSPICIOUS_DOMAINS = [
    "ngrok.io",
    "ngrok-free",
    "trycloudflare.com",
    "serveo.net",
    "localtunnel.me"
]

PHISHING_SYMBOLS = "@"

def symbol_score(url):
    score = 0
    reasons = []

    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

   
    for d in SUSPICIOUS_DOMAINS:
        if d in domain:
            score += 3
            reasons.append(f"Tunnel domain detected: {d}")

    
    symbol_count = sum(url.count(sym) for sym in PHISHING_SYMBOLS)
    if symbol_count >= 3:
        score += 2
        reasons.append(f"Excessive symbols detected ({symbol_count})")

    if re.search(r"[a-zA-Z]+[" + re.escape(PHISHING_SYMBOLS) + r"]+[a-zA-Z]+", url):
        score += 2
        reasons.append("Symbol-based obfuscation detected")

    
    if len(url) > 80:
        score += 1
        reasons.append("Unusually long URL")

    return score, reasons

def is_phishing(url):
    score, reasons = symbol_score(url)

    if score >= 3:
        return True, ", ".join(reasons)

    return False, "No symbol-based phishing patterns detected"

@app.route("/check", methods=["POST"])
def check_url():
    data = request.json
    url = data.get("url")

    phishing, reason = is_phishing(url)

    return jsonify({
        "phishing": phishing,
        "reason": reason
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)
