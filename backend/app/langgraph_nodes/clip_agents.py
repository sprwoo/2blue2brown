from app.controllers.grant import Grant
import asyncio

async def run_clip_agent(index, scene, grant_instance):
    prompt = (
        "You are an expert code animator creating a single Manim (Python) scene\n\n"
        f"Use the following scene description and script to generate the code:\n\n"
        f"Scene Description:\n{scene['scene_description']}\n"
        "❗Important:\n"
        "- Output **only** the complete Python code as plain text. Do NOT include any explanations, comments, or markdown (no ```python).\n"
        "- Do NOT include phrases like 'Here is the code:' or 'This code creates...'.\n"
        "- Your output will be compiled directly, so it must be a standalone, valid Python script using the Manim library.\n"
        "- Use a single Scene class with the name `LSTMScene`.\n"
        "- The subtitle must appear on screen using a `Text` object.\n\n"
        "- Your code should not have any overlapping elements, and all graphics should be legible. Clear any pre-existing elements before adding new ones. \n\n"
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