# ChatGPT Conversation Bot

This project is a simple conversational bot that uses OpenAI's ChatGPT API to engage in dialogues with users. The bot is designed to discuss basketball and respond to user inputs in a friendly manner.

## Features

- Engage in conversation with the bot about basketball.
- Maintain conversation history to provide context-aware responses.
- Exit the conversation gracefully with simple commands.

## Requirements

- Python 3.6 or higher
- `openai` Python package

## Setup

1. **Install Dependencies**

   Make sure you have the required Python package. You can install it using pip:

   ```bash
   pip install openai
Get OpenAI API Key

Sign up for an API key at OpenAI's website.

Set Up Your API Key

Replace my_sk in the script with your actual API key. You can either store your API key in a file named sk.py (as shown in the script) or set it as an environment variable.

Run the Script

Save the script as chatbot.py and run it:

bash
Copy code
python chatbot.py
Usage
Start a Conversation

After running the script, you can start chatting with the bot. Simply type your message and press Enter.

Exit the Conversation

To end the conversation, type exit, quit, or stop, and press Enter. The bot will say goodbye and end the chat.

Code Explanation
Initialize the Conversation History

The conversation_history list stores the ongoing dialogue, starting with a system message that defines the bot's role.

Get Response Function

The get_response function sends the conversation history to the ChatGPT API and retrieves the bot's response.

Conversation Loop

The script continuously prompts the user for input, updates the conversation history, and prints the bot's response until the user decides to end the conversation.

Code
python
Copy code
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
Example
plaintext
Copy code
You: Hi there!
Assistant: Hello! I'm a friendly assistant who loves to talk about basketball. How can I help you today?
License
This project is licensed under the MIT License. See the LICENSE file for more details.
