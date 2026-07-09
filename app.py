from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 把你刚才复制的 DeepSeek API Key 填在这里
DEEPSEEK_API_KEY = "sk-你的key放这里"

DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

@app.route('/v1/chat/completions', methods=['POST'])
def proxy():
    data = request.get_json()
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    # 转发请求到 DeepSeek
    resp = requests.post(DEEPSEEK_URL, headers=headers, json=data)
    return jsonify(resp.json()), resp.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
