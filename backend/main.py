# main.py

import os
import sys

# Ensure the 'app' folder is in the Python path.
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import node functions for the pipeline.
from app.langgraph_nodes.context import load_context
from app.langgraph_nodes.decision import should_generate_video
from app.langgraph_nodes.director import run_director_and_summarizer
from app.langgraph_nodes.clip_agents import generate_clips
from app.langgraph_nodes.chat_response import chat_response

# Import supporting controllers.
from app.controllers.combiner import CombinedCodeGenerator
from app.controllers.video_maker import VideoMaker
from app.controllers.voiceover_maker import VoiceOverMaker

def execute_pipeline(state):
    # Run load_context node.
    state.update(load_context(state))
    # Run decision node to determine if a video is needed.
    state.update(should_generate_video(state))
    
    if state.get("make_video"):
        # Run director to get scene plan and summary.
        state.update(run_director_and_summarizer(state))
        # Generate code chunks for each scene.
        state.update(generate_clips(state))
    else:
        # Otherwise, simply get a chat response.
        state.update(chat_response(state))
    
    return state

def main():
    user_prompt = input("Enter a concept you'd like explained: ")
    
    # Initial pipeline state.
    state = {
        "user_input": user_prompt,
        "session_id": None  # No DB context for this demo.
    }
    
    # Execute the pipeline.
    final_state = execute_pipeline(state)
    
    # Check if video code chunks were generated.
    code_chunks = final_state.get("code_chunks", [])
    
    if code_chunks:
        # Combine the code chunks into one Manim script.
        combiner = CombinedCodeGenerator(code_chunks)
        combined_file = combiner.save_to_file(folder="generated_manim", filename="manim.py")
        print(f"Combined Manim script saved to: {combined_file}")
        
        # Render the video using VideoMaker.
        video_maker = VideoMaker(
            script_file=combined_file,
            scene_name="LSTMScene",  # The generated code defines a class called LSTMScene.
            quality="l",             # Use 'l' (low) quality flag.
            preview=False
        )
        video_maker.render_video()
        print("Video rendering complete. Check the media folder for the output MP4.")
        
        # Determine the rendered video file.
        # In your logs, Manim saved the video here:
        video_file = os.path.join("media", "videos", "manim", "480p15", "LSTMScene.mp4")
        
        # Use the director's response as the voiceover script.
        script_text = final_state.get("chat_response", "No voiceover script available")
        
        # Generate the voiceover using Coqui TTS.
        voiceover_maker = VoiceOverMaker(script_text=script_text, output_audio_file="voiceover.wav")
        voiceover_maker.generate_voiceover()
        
        # Merge the audio with the video.
        merged_video_file = os.path.join("media", "videos", "manim", "480p15", "LSTMScene_with_voiceover.mp4")
        voiceover_maker.merge_audio_video(video_file=video_file, output_file=merged_video_file)
        
        print("Final video with voiceover is ready:", merged_video_file)
    else:
        # If no video was generated, just output the chat response.
        print("No video generated. The chat response is:\n")
        print(final_state.get("chat_response", "No response available."))

if __name__ == "__main__":
    main()
