import subprocess
import sys
from TTS.api import TTS  # pip install TTS

class VoiceOverMaker:
    def __init__(self, script_text, output_audio_file="voiceover.wav"):
        self.script_text = script_text
        self.output_audio_file = output_audio_file
        self.tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)

    def generate_voiceover(self):
        """
        Generate an audio file from the provided script text.
        """
        print("Generating voiceover audio...")
        self.tts.tts_to_file(text=self.script_text, file_path=self.output_audio_file)
        print(f"Voiceover audio generated: {self.output_audio_file}")
        return self.output_audio_file

    def merge_audio_video(self, video_file, output_file):
        """
        Use ffmpeg to merge the generated audio with the given video file.
        """
        print("Merging voiceover audio with video...")
        # This command copies the video stream and encodes audio with AAC.
        command = [
            "ffmpeg", "-y", "-i", video_file, "-i", self.output_audio_file,
            "-c:v", "copy", "-c:a", "aac", output_file
        ]
        try:
            subprocess.run(command, check=True)
            print(f"Merged video with voiceover saved as: {output_file}")
        except subprocess.CalledProcessError as e:
            print("Error merging audio and video:", e)
            sys.exit(1)
