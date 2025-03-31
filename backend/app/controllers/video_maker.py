# app/controllers/video_maker.py

import subprocess
import sys

class VideoMaker:
    def __init__(self, script_file, scene_name="MainScene", quality="l", preview=True):
        self.script_file = script_file
        self.scene_name = scene_name
        self.quality = quality
        self.preview = preview

    def render_video(self):
        command = ["manim", "render"]
        if self.preview:
            command.append("-p")
        
        # Map descriptive quality names to valid Manim quality flags.
        quality_map = {"low": "l", "medium": "m", "high": "h"}
        q = self.quality.lower()
        if q in quality_map:
            quality_flag = quality_map[q]
        else:
            # Assume a valid flag was provided.
            quality_flag = q

        # Use the '-q' flag with the mapped value.
        command.extend(["-q", quality_flag])
        
        # Append the script file and scene name.
        command.extend([self.script_file, self.scene_name])
        
        try:
            subprocess.run(command, check=True)
            print("Animation rendering complete. Check the media folder for the .mp4 output.")
        except subprocess.CalledProcessError as e:
            print("Error during Manim rendering:", e)
            sys.exit(1)
