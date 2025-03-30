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
    It looks for a code block delimited by triple backticks with an optional 'python' specifier.
    If no code block is found, it searches for the first occurrence of 'from manim'
    and returns everything from that point.
    """
    # Try to find a code block using triple backticks and optional 'python'
    code_block_pattern = r"```(?:python)?\s*(.*?)\s*```"
    match = re.search(code_block_pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    # Fallback: look for the start of valid code.
    start_index = text.find("from manim")
    if start_index != -1:
        return text[start_index:].strip()
    return text.strip()

def main():
    # Step 1: Get a topic or group of ideas from the user.
    user_topic = input("Enter the topic or ideas for your Manim scene: ")

    # The engineered prompt to generate a detailed, interesting script.
    system_prompt_script = (
        "You are an expert storyteller. Generate a detailed and interesting script about the given topic, ensuring that it is "
        "easy to understand and captivating for the viewer. The script should be structured with clear sections, and each section "
        "should build on the previous one to maintain engagement. Your output should only be text, with no Python code included. "
        "Do not output any additional explanations."
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
    messages_script = [
        {"role": "system", "content": system_prompt_script},
        {"role": "user", "content": user_topic}
    ]

    try:
        response_script = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            max_tokens=8192,
            temperature=0.6,
            top_p=0.95,
            messages=messages_script
        )
    except Exception as e:
        print("Error calling API for script:", e)
        sys.exit(1)
    
    # Step 3: Extract and clean the generated script.
    try:
        raw_response_script = response_script.choices[0].message.content
        print("Generated Script:\n")
        print(raw_response_script)  # Output the script in the terminal
    except (AttributeError, KeyError, IndexError) as e:
        print("API response did not contain the expected script.")
        sys.exit(1)

    # The engineered prompt to generate valid Manim code based on the generated script.
    system_prompt_code = (
        "You are an expert in Manim. Generate Python code that defines a complete Manim scene based on the following script. "
        "The code should include all relevant animations and transitions to visualize the ideas described in the script. "
        "Ensure that the generated code defines a class called 'MainScene'. "
        "The script should include visual elements such as geometric objects like 'Circle', 'Square', and 'Text' (no external SVG files). "
        "Do not use 'VGroup.index()' to reference elements in a group; instead, use direct indexing. "
        "Ensure proper use of animations like 'FadeIn', 'Write', and 'LaggedStart'. "
        "The scene should last from one to two minutes, and subtitles should appear throughout the scene to improve the flow of the narration. "
        "Only output the Python code, and do not include any other explanations."
    )

    # Prepare the conversation messages for Manim code generation using the generated script.
    messages_code = [
        {"role": "system", "content": system_prompt_code},
        {"role": "user", "content": raw_response_script}
    ]

    try:
        response_code = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            max_tokens=8192,
            temperature=0.6,
            top_p=0.95,
            messages=messages_code
        )
    except Exception as e:
        print("Error calling API for Manim code:", e)
        sys.exit(1)
    
    # Step 4: Extract and clean the generated Manim code.
    try:
        raw_response_code = response_code.choices[0].message.content
        manim_code = extract_python_code(raw_response_code)
    except (AttributeError, KeyError, IndexError) as e:
        print("API response did not contain the expected Manim code, using demo scene code instead.")
        manim_code = DEMO_SCENE_CODE
    
    # Step 5: Save the generated code to a Python file.
    code_filename = "generated_manim.py"
    try:
        with open(code_filename, "w", encoding="utf-8") as file:
            file.write(manim_code)
        print(f"Manim code saved to {code_filename}")
    except IOError as e:
        print("Error writing the code file:", e)
        sys.exit(1)
    
    # Step 6: Use Manim to render the scene.
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
