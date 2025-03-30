import os
import re
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

def extract_python_code(text):
    """
    Extracts Python code from the API response.
    If a '</think>' tag is present, returns only everything after that tag.
    Otherwise, tries to extract a code block delimited by triple backticks,
    or returns everything starting from 'from manim import *'.
    """
    # Check if '</think>' tag is present and return code after it.
    if '</think>' in text:
        index = text.find('</think>') + len('</think>')
        return text[index:].strip()
    
    # Try to find a code block using triple backticks and optional 'python'
    code_block_pattern = r"```(?:python)?\s*(.*?)\s*```"
    match = re.search(code_block_pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    
    # Fallback: look for the start of valid code starting with 'from manim import *'
    start_index = text.find("from manim import *")
    if start_index != -1:
        return text[start_index:].strip()
    
    return text.strip()

def main():
    # Step 1: Get a topic or group of ideas from the user.
    user_topic = input("Enter the topic or ideas for your Manim scene: ")

    # Revised system prompt: force output of ONLY Manim code, no extra text or tags.
    system_prompt = (
        "You are an expert in Manim. Generate only valid, self-contained Python code that defines a complete Manim scene. "
        "The code must start with 'from manim import *' and include all necessary imports. "
        "It should define a Manim Scene class named 'MainScene' that demonstrates a neural network with layers, neurons, and connections using VGroup. "
        "Animate the network's forward pass with LaggedStart, display a loss equation, then animate backpropagation with gradient arrows. "
        "Include equations for the forward pass, loss, and gradient computation, and animate them as needed. "
        "Use colors to differentiate phases and add labels with text objects. "
        "Do not output any extra text, markdown formatting, or tags—output only the code."
    )

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

    # Prepare the conversation messages with a system message and the user prompt.
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_topic}
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
    
    # Step 3: Extract and clean the generated code.
    try:
        raw_response = response.choices[0].message.content
        manim_code = extract_python_code(raw_response)
        # Replace any undefined reference to 'output_animation' with 'output_activation'
        manim_code = manim_code.replace("output_animation", "output_activation")
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
    # Running Manim as a module via the current Python interpreter to ensure the correct environment is used.
    command = [sys.executable, "-m", "manim", "-p", "-ql", code_filename, "MainScene"]
    try:
        subprocess.run(command, check=True)
        print("Animation rendering complete. Check the media folder for the .mp4 output.")
    except subprocess.CalledProcessError as e:
        print("Error during Manim rendering:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
