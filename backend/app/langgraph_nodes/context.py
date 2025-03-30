from run import get_chat_histories
from app.controllers import Chunky

def load_context(state):
    session_id = state.get("session_id")
    if not session_id:
        return {"chat_history": [], "chat_summary": ""}
    
    messages = get_chat_histories(session_id)
    if isinstance(messages, dict) and "error" in messages:
        return {"chat_history": [], "chat_summary": ""}
    
    # assuming for now, the messages are just texts and not images and code for now
    cleaned = [{"role": msg["role"], "content": msg["message"]} for msg in messages]
    
    recent_msgs = cleaned[-6:]
    
    conversation_text = "\n".join([f"{m['role']}: {m['content']}" for m in recent_msgs])
    prompt = f"Summarize this chat in 1-2 sentances, but more emphasis on the later messages: \n\n{conversation_text}"
    
    chunky = Chunky()
    summary = chunky.basic_response(prompt)
    
    return {
        "chat_history": cleaned,
        "chat_summary": summary,
    }