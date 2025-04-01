from app.controllers.grant import Grant
import asyncio

async def run_clip_agent(index, scene, grant_instance):
    print(f"prompt being passed in. {scene}")
    prompt = (
        "You are an expert code animator creating a single Manim (Python) scene in the style of 3Blue1Brown.\n\n"
        f"Use the following scene description and subtitle to generate the code:\n\n"
        f"Scene Description:\n{scene['scene_description']}\n"
        f"Subtitle:\n\"{scene['subtitle_script']}\"\n\n"
        "❗Important:\n"
        "- Output **only** the complete Python code as plain text. Do NOT include any explanations, comments, or markdown (no ```python).\n"
        "- Do NOT include phrases like 'Here is the code:' or 'This code creates...'.\n"
        "- Your output will be compiled directly, so it must be a standalone, valid Python script using the Manim library.\n"
        "- Use a single Scene class with the name `LSTMScene`.\n"
        #"- Give it some animations, and when the scene is finished, make the scene fade out.\n"
        "- Stay on each scene long enough so that all the information on that scene can be spoken before changing the scene.\n"
        "- The subtitle must appear on screen using a `Text` object.\n\n"
        "Begin your output now:"
    )

    
    return index, grant_instance.code_response(prompt)

def generate_clips(state):
    scene_plan = state.get("scene_plan", [])
    grant = Grant()
    
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for index, scene in enumerate(scene_plan):
            futures.append(executor.submit(run_clip_agent_sync, index, scene, Grant()))

        results = [f.result() for f in futures]

    results.sort(key=lambda x: x[0])
    code_chunks = [r[1] for r in results]
    for i, chunk in enumerate(code_chunks):
        print(f"Chunk {i}: {chunk}")
    return {
        "code_chunks": code_chunks
    }
    
def run_clip_agent_sync(index, scene, grant_instance):
    return asyncio.run(run_clip_agent(index, scene, grant_instance))