from app.controllers import Chunky

def chat_response(state):
    user_input = state.get("user_input")
    chat_summary = state.get("chat_summary", "")
    print("user_input for chat response", user_input)
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
    
    print ("chat response", response)
    
    return {
        "chat_response": response,
    }