import subprocess
import sys

class VideoMaker:
    def __init__(self, script_file, scene_name="MainScene", quality="ql", preview=True):
        self.script_file = script_file
        self.scene_name = scene_name
        self.quality = quality
        self.preview = preview

    def render_video(self):
        command = ["manim"]
        if self.preview:
            command.append("-p")
        command.append(f"-{self.quality}")
        command.extend([self.script_file, self.scene_name])
        
        try:
            subprocess.run(command, check=True)
            print("Animation rendering complete. Check the media folder for the .mp4 output.")
        except subprocess.CalledProcessError as e:
            print("Error during Manim rendering:", e)
            sys.exit(1)
