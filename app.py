from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

DEEPSEEK_API_KEY = "sk-53f5472de49545cfab6501c03cb2e985"
"

DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route('/v1/chat/completions', methods=['POST'])
def proxy():
    data = request.get_json()
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
  
    resp = requests.post(DEEPSEEK_URL, headers=headers, json=data)
    return jsonify(resp.json()), resp.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
