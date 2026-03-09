# 2Blue2Brown

**Nebius Hackathon Project**

A chatbot that turns your questions into short, narrated educational animations inspired by [3Blue1Brown](https://www.youtube.com/c/3blue1brown). The name **2Blue2Brown** is a playful nod to that channel. Ask about any concept and receive a Manim-rendered video with a voiceover — powered by a network of LLM agents working in parallel.

---

## How it works — high-level flow

```
User question
    │
    ▼
load_context  ──►  decision_node
                        │
           ┌────────────┴────────────┐
      make_video?                chat-only?
           │                         │
           ▼                         ▼
    director_node            chat_response_node
  (parallel tasks)                   │
           │                        END
           ▼
   clip_agents_node
  (parallel threads)
           │
          END
  (Manim render + TTS voiceover + FFmpeg merge)
```

---

## How it is Agentic

The project is built around a **multi-agent architecture** orchestrated by a [LangGraph](https://github.com/langchain-ai/langgraph) state machine. Each node in the graph is a distinct autonomous agent with a well-defined role and its own LLM call(s).

### Agents

| Agent | Class / node | Model | Role |
|---|---|---|---|
| **Decision Agent** | `decision_node` → `Chunky` | Llama 3.1 405B | Reads the user message + chat history and decides: *generate a video* or *reply with text only*. |
| **Chat Agent** | `chat_response_node` → `Chunky` | Llama 3.1 405B | Produces a conversational text answer when no video is needed. |
| **Director Agent** | `director_node` → `Chunky` | Llama 3.1 405B | Breaks the concept into 5–9 self-contained scenes, each with a detailed Manim description and a short subtitle. Also generates an updated chat summary. |
| **Clip Agents** (one per scene) | `clip_agents_node` → `Grant` | Llama 3.1 405B | Converts a single scene description into a complete, runnable Manim Python script. A new `Grant` instance is spun up for each scene. |

#### LangGraph state machine (`backend/app/controllers/langgraph_flow.py`)

```python
graph.add_node("load_context",       load_context)
graph.add_node("decision_node",      should_generate_video)   # Decision Agent
graph.add_node("chat_response_node", chat_response)           # Chat Agent
graph.add_node("director_node",      run_director_and_summarizer)  # Director Agent
graph.add_node("clip_agents_node",   generate_clips)          # Clip Agents

graph.add_conditional_edges(
    "decision_node",
    lambda state: "director_node" if state.get("make_video") else "chat_response_node"
)
```

Each node receives the full **shared state** (user input, chat history, scene plan, generated code, …) and returns only the keys it updates — a classic agent handoff pattern.

---

## How it is Parallel

Two distinct parallelism mechanisms are used to reduce end-to-end latency.

### 1. Async concurrency — Director node (`backend/app/langgraph_nodes/director.py`)

When a video is requested the **Director node** must both (a) generate a scene plan and (b) produce an updated chat summary. These two LLM calls are independent, so they run concurrently with `asyncio.gather`:

```python
async def _run_parallel_tasks(state):
    summary_task = summary(state)               # LLM call A: chat summary
    script_task  = generate_script_chunks(state)  # LLM call B: scene plan

    summary_result, script_result = await asyncio.gather(summary_task, script_task)
    return {**summary_result, **script_result}
```

Both API requests are in-flight simultaneously; the node only returns once **both** have completed.

### 2. Thread-pool parallelism — Clip Agents (`backend/app/langgraph_nodes/clip_agents.py`)

Once the scene plan is ready, every scene needs its own Manim code. All scenes are independent, so a **`ThreadPoolExecutor`** is used to call one `Grant` agent per scene concurrently:

```python
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [
        executor.submit(run_clip_agent_sync, index, scene, Grant())
        for index, scene in enumerate(scene_plan)
    ]
    results = [f.result() for f in futures]

results.sort(key=lambda x: x[0])   # preserve scene order
code_chunks = [r[1] for r in results]
```

For a 7-scene video this means **7 LLM requests run in parallel** instead of sequentially, cutting the code-generation step from ~7× to ~1× the per-scene latency.

---

## Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 15 · React 19 · TypeScript · Tailwind CSS |
| Backend | Python · Flask · LangGraph |
| LLM | Nebius API — Meta-Llama 3.1 405B Instruct (text) · Google Gemma 3 27B (vision) |
| Animation | Manim 0.19 |
| Text-to-Speech | Coqui TTS |
| Audio/Video merge | FFmpeg |
| Database / Auth | Supabase (PostgreSQL) |

---

## Quick start

```bash
# Backend
cd backend
pip install -r requirements.txt
# create .env with LLM_KEY, SUPABASE_URL, SUPABASE_KEY
python run.py          # Flask on :5001

# Frontend (separate terminal)
cd frontend
npm install
npm run dev            # Next.js on :3000
```
