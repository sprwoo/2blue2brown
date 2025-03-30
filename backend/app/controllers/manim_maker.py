import os
import shutil

class ManimScriptGenerator:
    def __init__(self, output_filename="generated files/generated_manim.py"):
        self.output_filename = output_filename

    def generate_script(self, manim_code: str):
        # Ensure the output directory exists.
        output_dir = os.path.dirname(self.output_filename)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # Write the Manim code to the file.
        with open(self.output_filename, "w") as file:
            file.write(manim_code)