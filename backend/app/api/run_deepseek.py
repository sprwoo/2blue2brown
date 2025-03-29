import os
import subprocess
import sys
from dotenv import load_dotenv
from openai import OpenAI  # Ensure you've installed the openai package

# Load environment variables from .env file.
load_dotenv()

# Define a demo Manim scene in case the API response doesn't include code.
DEMO_SCENE_CODE = '''
from manim import *

class MainScene(Scene):
    def construct(self):
        text = Text("Hello, Nebius Studio!")
        self.play(Write(text))
        self.wait(2)
'''

def main():
    # Step 1: Get a prompt from the user.
    prompt = input("Enter your prompt for the Nebius Studio Deepseek R1 API: ")

    # Retrieve your API key from the environment variable set in the .env file.
    api_key = os.getenv("NEBIUS_API_KEY")
    if not api_key:
        print("API key not set. Please add NEBIUS_API_KEY to your .env file.")
        sys.exit(1)

    # Step 2: Initialize the client with the specified base_url and API key.
    client = OpenAI(
        base_url="https://api.studio.nebius.com/v1/",
        api_key=api_key
    )

    # Prepare the conversation messages.
    messages = [
        {"role": "user", "content": prompt}
    ]

    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            max_tokens=8192,
            temperature=0.6,
            top_p=0.95,
            messages=messages
        )
    except Exception as e:
        print("Error calling API:", e)
        sys.exit(1)
    
    # Step 3: Extract the generated code.
    try:
        # Use attribute access instead of subscript notation.
        manim_code = response.choices[0].message["content"]
    except (AttributeError, KeyError, IndexError) as e:
        print("API response did not contain the expected code, using demo scene code instead.")
        manim_code = DEMO_SCENE_CODE
    
    # Step 4: Save the generated code to a Python file.
    code_filename = "generated_manim.py"
    try:
        with open(code_filename, "w", encoding="utf-8") as file:
            file.write(manim_code)
        print(f"Manim code saved to {code_filename}")
    except IOError as e:
        print("Error writing the code file:", e)
        sys.exit(1)
    
    # Step 5: Use Manim to render the scene.
    # Assumes that the generated code defines a scene class named "MainScene".
    command = ["manim", "-p", "-ql", code_filename, "MainScene"]
    try:
        subprocess.run(command, check=True)
        print("Animation rendering complete. Check the media folder for the .mp4 output.")
    except subprocess.CalledProcessError as e:
        print("Error during Manim rendering:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
