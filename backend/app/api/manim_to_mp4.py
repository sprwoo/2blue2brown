import requests
import subprocess
import sys

def main():
    # Step 1: Get a prompt from the user
    prompt = input("Enter your prompt for the Nebius Studio Deepseek R1 API: ")

    # Step 2: Make an API call to get the LaTeX/Manim code.
    # Replace this URL with the actual API endpoint.
    api_url = "https://api.nebiusstudio.com/deepseekR1"
    payload = {"prompt": prompt}
    
    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print("Error calling API:", e)
        sys.exit(1)
    
    # Expecting a JSON response with the LaTeX/Manim code
    data = response.json()
    manim_code = data.get("latex_manim_code")
    if not manim_code:
        print("API response did not contain the expected LaTeX/Manim code.")
        sys.exit(1)
    
    # Step 3: Save the code to a Python file (e.g., generated_manim.py)
    code_filename = "generated_manim.py"
    try:
        with open(code_filename, "w") as file:
            file.write(manim_code)
        print(f"Generated Manim code saved to {code_filename}")
    except IOError as e:
        print("Error writing the code file:", e)
        sys.exit(1)
    
    # Step 4: Use Manim to render the scene.
    # This assumes the generated code defines a scene class named "MainScene".
    # The flags used here:
    #   -p : Preview the video after rendering.
    #   -ql : Render in low quality.
    command = ["manim", "-p", "-ql", code_filename, "MainScene"]
    try:
        subprocess.run(command, check=True)
        print("Animation rendering complete. Check the media folder for the .mp4 output.")
    except subprocess.CalledProcessError as e:
        print("Error during Manim rendering:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
