from core.assistant import AlecsIA

assistant = AlecsIA()

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit"]:
        break

    response = assistant.chat(user_input)
    print("AlecsIA:", response)
