from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message", "") if data else ""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # <-- fallback model
            messages=[
                {"role": "system", "content": "You are a helpful website assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"response": reply})
    except Exception as e:
        print("🔥 ERROR:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
