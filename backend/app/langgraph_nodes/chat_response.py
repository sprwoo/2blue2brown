from app.controllers import Chunky

def chat_response(state):
    user_input = state.get("user_input")
    chat_summary = state.get("chat_summary", "")
    
    prompt = (
        "You are a helpful tutor. Based on the following conversation summary and the user's latest message, "
        "respond clearly and concisely to help them understand the concept.\n\n"
        f"Chat Summary:\n{chat_summary}\n\n"
        f"User Message:\n{user_input}"
    )
    
    chunky = Chunky()
    response = chunky.basic_response(prompt)
    
    return {
        "chat_response": response,
    }