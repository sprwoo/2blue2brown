from app.services import get_chat_histories
from app.controllers import Chunky

# session id: 1828e6f9-707d-4d04-b5e5-5d036698b9d6

def load_context(state):
    session_id = state.get("session_id")
    print("Loading context for session_id:", session_id)
    if not session_id:
        print("No session_id provided")
        return {"chat_history": [], "chat_summary": ""}
    
    messages = get_chat_histories(session_id)
    print("Messages:", messages)
    if isinstance(messages, dict) and "error" in messages:
        print("Error fetching chat history:", messages)
        return {"chat_history": [], "chat_summary": ""}
    
    # assuming for now, the messages are just texts and not images and code for now
    cleaned = [{"role": msg["sender"], "content": msg["message"]} for msg in messages]
    print("Cleaned chat history:", cleaned)
    
    recent_msgs = cleaned[-6:]
    print("Recent messages:", recent_msgs)
    
    conversation_text = "\n".join([f"{m['role']}: {m['content']}" for m in recent_msgs])
    prompt = (
        "Based on the following conversation texts, provide a summary of the conversation. Go through each message given by the ai and user and summarize each interaction, responding in a json like this: "
        "[{'sender': <ai or user>, 'interaction': <summary of their response>}, {'sender': <ai or user>, 'interaction': <summary of their response>}, ...]"
        f": \n\n{conversation_text}"
    )
    
    chunky = Chunky()
    summary = chunky.basic_response(prompt)
    print("Chat summary:", summary)
    
    return {
        "chat_history": cleaned,
        "chat_summary": summary,
    }