from ai.llm import ask_llm

class AlecsIA:

    def __init__(self):

        self.history = []

        self.system_prompt = {
            "role": "system",
            "content": "You are AlecsIA, a personal AI assistant created by Alecs."
        }

    def chat(self, user_input):

        self.history.append({
            "role": "user",
            "content": user_input
        })

        messages = [self.system_prompt] + self.history

        response = ask_llm(messages)

        self.history.append({
            "role": "assistant",
            "content": response
        })

        return response
