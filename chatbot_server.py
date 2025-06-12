from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

openai.api_key = "OPENAI_API_KEY"

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "") if data else ""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful website assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)

