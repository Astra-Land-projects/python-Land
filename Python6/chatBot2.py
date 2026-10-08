from google import genai

# Initialize the Gemini Client with your API Key
client = genai.Client(api_key="AQ.Ab8RN6LH3Sy_esFLj-sbd4wGicTb5uyXufvxZjsTOJW-NcLONw")

# Create a chat session with system instructions to force English responses
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=genai.types.GenerateContentConfig(
        system_instruction="You are a helpful and friendly AI assistant. Always respond in English."
    )
)

print("--- Gemini AI Chatbot Initialized! (Type 'exit' or 'quit' to stop) ---\n")

while True:
    user_input = input("You: ")
   
    if user_input.lower() in ['exit', 'quit']:
        print("Goodbye!")
        break

    # Send message to Gemini and print the response
    response = chat.send_message(user_input)
    print(f"\nGemini: {response.text}\n")