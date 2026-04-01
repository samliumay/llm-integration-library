from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()

# Basic text generation using the Gemini API.  Its a statless process.
def basic_text_generation(content):
    print("Starting the Gemini API...")

    client = genai.Client()

    response = client.models.generate_content(
        model = "gemini-2.5-flash-lite",
        contents = str(content)
    )

    return response 

# Text generation with well defined thinking process.
def text_generation_thinking(content):
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="How does AI work?",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_level="low")
        ),
    )

    return response 

# Text

def text_generation_with_system_prompts(content):
    client = genai.Client()

    response = client.models.generate_content(
        model = "gemini-2.5-flash-lite",
        contents = str(content),
        config= types.GenerateContentConfig(
            system_instruction="You are a cat. Your name is nemo."
        )
    )

    return response

def text_generation_with_dynamic_temprature(content, temp):
    client = genai.Client()

    response = client.models.generate_content(
        model = 'gemini-2.5-flash-lite',
        contents = [str(content)],
        config=types.GenerateContentConfig(
            temperature = float(temp)
        )
    )

    return response
    
def multimodel_input(content, path_of_image):
    client = genai.Client()

    image = Image.open(path_of_image)
    response = client.models.generate_content(
        model = 'gemini-2.5-flash-lite',
        contents = [image, str(content)]
    )

    return response
def straming_process(content):
    client = genai.Client()

    response = client.models.generate_content_stream(
        model="gemini-3-flash-preview",
        contents=[str(content)]
    )
    for chunk in response:
        print(chunk.text, end="")