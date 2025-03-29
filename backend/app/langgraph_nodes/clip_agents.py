from app.controllers import Grant
import asyncio

async def run_clip_agent(index, scene, grant_instance):
    prompt = (
        f"You are a code animator creating an educational video in 3Blue1Brown style. You are coding in the Manim library (Python).\n\n"
        f"Scene Description:\n{scene['scene_description']}\n"
        f"Subtitle:\n\"{scene['subtitle_script']}\"\n\n"
        "Generate code for this animation scene in manim. Make sure the code includes the subtitle as a text label"
        "Make it all in one scene, no need to break it down into smaller scenes.\n"
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
    return {
        "code_chunks": code_chunks
    }
    
def run_clip_agent_sync(index, scene, grant_instance):
    return asyncio.run(run_clip_agent(index, scene, grant_instance))