import openai
from sk import my_sk

openai.api_key = my_sk

# Initialize the conversation history
conversation_history = [
    {"role": "system", "content": "You are a friendly assistant who loves to talk about basketball."}
]

def get_response(conversation):
    # Create a chat completion with the current conversation history
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=conversation
    )
    return response.choices[0]['message']['content']

while True:
    # Get user input
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit', 'stop']:
        print("Ending the conversation. Goodbye!")
        break
    
    # Add user input to the conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    # Get response from the chatbot
    response = get_response(conversation_history)
    
    # Add chatbot response to the conversation history
    conversation_history.append({"role": "assistant", "content": response})
    
    # Print the chatbot response
    print(f"Assistant: {response}")