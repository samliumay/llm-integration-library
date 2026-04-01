from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def basic_chat_generation():
    client = genai.Client()

    chat = client.chats.create(
        model='gemini-2.5-flash-lite',
        config=types.GenerateContentConfig(
            system_instruction= "You are an assistant to help homeworks about coding and CS topics."
        )
    )

    user_input = str(input('Enter what you want to ask to assistant: \n If you want to exit, just type "exit" \n\n'))
    
    while user_input.lower() != "exit":
        response = chat.send_message(user_input)
        print(f'answer: {response.text}\n\n')

        user_input = str(input('Ask if you want to continue or type "exit" to end the chat: \n\n'))
    

    