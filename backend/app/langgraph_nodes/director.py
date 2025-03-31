from app.controllers.chunky import Chunky
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
        "You are a video director tasked with creating a short educational animation using Manim, the animation engine behind 3Blue1Brown. "
        "Your goal is to design a series of 5–9 independent scenes based on the user’s input and the chat context provided below. "
        "These scenes, when played in order, should explain a clear educational progression related to the user’s specified topic. "
        "Each scene starts on a blank canvas and must be fully self-contained, with no references to or dependencies on other scenes.\n\n"
        
        "For each scene, provide detailed, step-by-step instructions that can be directly translated into Manim code using only basic primitives: "
        "circles, rectangles, arrows, lines, Text objects, and simple transformations (e.g., fade, shift, transform). "
        "Include both a broad overview of the scene’s purpose (e.g., 'This scene introduces the concept of a single neuron') "
        "and specific, programmatic details about what to draw, where, and how (e.g., sizes, positions, colors, labels). "
        "Do not assume any elements from previous scenes exist—every scene begins from scratch.\n\n"
        
        "Guidelines for each scene:\n"
        "- **Logical Progression:** The series should follow a clear, educational sequence based on the user’s topic. "
        "For example, if the user asks for an explanation of neural networks, you might start with a single neuron, "
        "then show a simple network, and later introduce a more complex structure—all tailored to the user’s request.\n"
        "- **Self-Containment:** Each scene must include a brief recap of necessary context within its description "
        "(e.g., 'A neuron is a basic unit that processes inputs') so it stands alone, given its blank canvas starting point.\n"
        "- **Scene Description Details:** Provide precise instructions. For example, instead of 'draw a neuron,' say: "
        "'On a blank canvas, draw a circle of radius 0.5 at position (0, 0); add a Text object “Neuron” 1 unit above the circle; "
        "draw two arrows of length 1 entering from the left at (-2, 0.5) and (-2, -0.5), and one arrow exiting to the right at (2, 0).'\n"
        "- **Subtitle Script:** Include a concise subtitle (4–9 words) to appear on-screen, summarizing the scene’s focus. "
        "This is the only on-screen text allowed.\n\n"
        
        "Output requirements:\n"
        "- Output a valid JSON array where each element is an object with exactly two keys: 'scene_description' and 'subtitle_script'.\n"
        "- Do not include any additional commentary, explanations, or text outside the JSON array.\n\n"
        
        "Example scene:\n"
        "```json\n"
        "{\n"
        "  \"scene_description\": \"On a blank canvas, draw a circle of radius 0.5 at the center (0, 0). "
        "Add a Text object 'Neuron' positioned 1 unit above at (0, 1). "
        "Draw two arrows of length 1 entering from the left at (-2, 0.5) and (-2, -0.5), and one arrow of length 1 exiting to the right at (2, 0).\",\n"
        "  \"subtitle_script\": \"A single neuron processes inputs\"\n"
        "}\n"
        "```\n\n"
        
        "Now, using the following context, generate the JSON array of scenes:\n\n"
        f"Chat Summary:\n{chat_summary}\n\n"
        f"User Message:\n{user_input}\n\n"
        "Output:\n"
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