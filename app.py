from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Send the message to Rasa server and get the response
    try:
        response = requests.post(
            "http://localhost:5005/webhooks/rest/webhook",
            json={"sender": "user", "message": user_message},
        )
        
        # Raise an error for bad responses
        response.raise_for_status()
        
        # Get response from Rasa
        rasa_response = response.json()

        # Extract the text from Rasa's response
        if rasa_response:
            bot_message = " ".join([msg.get("text") for msg in rasa_response if "text" in msg])
        else:
            bot_message = "Sorry, I didn't understand that."

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Rasa: {e}")
        bot_message = "Sorry, I couldn't reach the server. Please try again later."

    return jsonify({"message": bot_message})

if __name__ == "__main__":
    app.run(port=8000, debug=True)
