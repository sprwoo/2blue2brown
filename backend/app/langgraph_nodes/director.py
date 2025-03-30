from app.controllers import Chunky
import json
import asyncio

async def summary(state):
    user_input = state.get("user_input")
    chat_summary = state.get("chat_summary", "")
    prompt = (
        "You are a helpful, conversational tutor.\n\n"
        "Below is a summary of the previous conversation. Use it to understand the user's background knowledge, tone, or recent topics if relevant.\n"
        "However, the user's latest message may shift topics — always prioritize answering their current request.\n\n"
        "Respond clearly and concisely, but feel free to build on earlier concepts if it seems useful.\n\n"
        f"Chat Summary:\n{chat_summary}\n\n"
        f"User Message:\n{user_input}\n\n"
        "Your response:"
    )
    
    chunky = Chunky()
    response = chunky.basic_response(prompt)
    
    print("summary response", response)
    
    return {
        "chat_response": response,
    }

async def generate_script_chunks(state):
    user_input = state.get("user_input")
    chat_summary = state.get("chat_summary", "")
    
    prompt = (
        "You are a video director creating a short educational animation using Manim — the animation engine behind 3Blue1Brown. "
        "Your task is to plan a series of 5–9 independent scenes that, when played in order, explain a progression from a single neuron, "
        "to a basic neural network, and finally to an LSTM cell as an example. Each scene is rendered on a blank canvas, so each scene must be completely self-contained. "
        "There should be no assumptions that a scene is a continuation of a previous one; instead, each scene should briefly restate necessary context.\n\n"
        
        "For each scene, provide very specific, step-by-step instructions that can be directly translated into Manim code using only basic primitives such as: "
        "circles, rectangles, arrows, lines, Text objects, and simple transformations (fade, shift, transform). "
        "Describe exactly what to draw, including positions, sizes, and labels if necessary. "
        "Do not assume any previous scene’s elements exist; every scene starts with a blank canvas.\n\n"
        
        "Guidelines for each scene:\n"
        "- **Progression & Consistency:** The series should progress logically. For example, begin with a scene that introduces a single neuron (a circle with a label), "
        "follow with a scene that shows multiple neurons forming a basic neural network (with clear spatial arrangements like circles in vertical or horizontal lines connected by arrows), "
        "and then a scene that explains an LSTM cell by illustrating its internal structure (e.g., separate sections for input, cell state, and output gates).\n"
        "- **Self-Containment:** Each scene must include a brief recap of the necessary context so that it makes sense on its own, you can't reference or build ontop of previous scenes, they are all independant, given that it starts on a blank canvas.\n"
        "- **Scene Description:** Provide precise, programmatic instructions for drawing the scene. For example, instead of saying \"draw a neural network diagram,\" say: "
        "\"Draw three circles of radius 0.5 evenly spaced vertically on the left side of the canvas; draw arrows connecting the top circle to the middle and the middle to the bottom; "
        "label the circles with Text objects 'Input', 'Hidden', and 'Output' respectively.\" \n"
        "- **Subtitle Script:** Include a short (4–9 word) caption that will appear on screen for the scene. This is the only place on-screen text should appear.\n\n"
        
        "Output requirements:\n"
        "- Output a valid JSON array. Each element must be an object with exactly two keys: 'scene_description' and 'subtitle_script'.\n"
        "- Do not include any additional commentary, explanations, or text outside of the JSON array.\n\n"
        
        "For example, a valid scene could be:\n"
        "{\"scene_description\": \"On a blank canvas, draw a circle of radius 0.5 at the center and add a Text object above it saying 'Neuron'.\", "
        "\"subtitle_script\": \"Introducing a single neuron\"}\n\n"
        
        "Now, using the following context, generate the JSON array of scenes:\n\n"
        f"Chat Summary:\n{chat_summary}\n\n"
        f"User Message:\n{user_input}\n\n"
        "Output:"
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
        
    print("scene_plan: ", scene_plan)
    return {
        "scene_plan": scene_plan
    }
    
def run_director_and_summarizer(state):
    return asyncio.run(_run_parallel_tasks(state))


async def _run_parallel_tasks(state):
    summary_task = summary(state)
    script_task = generate_script_chunks(state)

    summary_result, script_result = await asyncio.gather(summary_task, script_task)
    return {**summary_result, **script_result}