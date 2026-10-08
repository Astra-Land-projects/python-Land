from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Initialize Gemini Client
client = genai.Client(api_key="AQ.Ab8RN6LH3Sy_esFLj-sbd4wGicTb5uyXufvxZjsTOJW-NcLONw")

# Create a chat session with system instruction for English responses
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=genai.types.GenerateContentConfig(
        system_instruction="You are Astra AI, a helpful, friendly, and intelligent AI assistant. Always respond in English."
    )
)

@app.route('/')
def home():
    return render_template('templates.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'response': 'Please enter a message.'})
   
    # Send message to Gemini
    response = chat.send_message(user_message)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)