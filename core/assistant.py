from ai.llm import ask_llm
from tools.registry import get_tool
import tools.open_browser
import tools.system


class AlecsIA:

    def __init__(self):

        self.history = []

        self.system_prompt = {
            "role": "system",
            "content": "You are AlecsIA, a personal AI assistant."
        }

    def handle_command(self, text):

        if text.startswith("abre "):

            target = text.replace("abre ", "")

            tool = get_tool("open_browser")

            return tool(f"https://{target}.com")

        return None


    def chat(self, user_input):

        tool_response = self.handle_command(user_input)

        if tool_response:
            return tool_response

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
