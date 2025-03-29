from app.controllers import Chunky
import json

def generate_script_chunks(state):
    user_input = state.get("user_input")
    chat_summary = state.get("chat_summary", "")
    
    prompt = (
        "You're a video director for short educational videos in the style of 3Blue1Brown.\n\n"
        "Based on the following summary and user message, plan a video.\n"
        "Break it down into 5 to 9 short clip scenes. For each clip, include:\n"
        "1. A short animation description (what should be shown visually, has to one scene, ex. creating a graph, then a porabola, then a tangent to explain derivatives would be one scene)\n"
        "2. A subtitle script (text to appear on screen / be spoken), make sure it's not too long as to not fit in the screen aim for 4-9 words\n\n"
        f"Chat Summary:\n{chat_summary}\n\n"
        f"User Message:\n{user_input}\n\n"
        "Respond as a JSON list like this:\n"
        "[\n"
        "  {\"scene_description\": \"Define what should be happening on the screen\", "
        "\"subtitle_script\": \"Write the subtitle that should follow the scene\"},\n"
        "  {\"scene_description\": \"Define what should be happening on the screen.\", "
        "\"subtitle_script\": \"Write the subtitle that should follow the scene.\"}\n"
        "]"
    )
    
    chunky = Chunky()
    response = chunky.basic_response(prompt)

    try:
        scene_plan = json.loads(response)
        if not isinstance(scene_plan, list):
            raise ValueError
    except Exception:
        scene_plan = [{
            "scene_description": "Single-scene fallback based on user input",
            "subtitle_script": response.strip()
        }]

    return {
        "scene_plan": scene_plan
    }