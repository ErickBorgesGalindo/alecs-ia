from ai.llm import ask_llm
from tools.registry import get_tool
from utils.tool_parser import parse_tool_response

import tools.open_browser
import tools.system


class AlecsIA:

    def __init__(self):

        self.history = []

        self.system_prompt = {
            "role": "system",
            "content": """
You are AlecsIA, a personal assistant.

If the user asks to perform an action like opening a website,
respond ONLY in JSON like this:

{
 "tool": "open_browser",
 "args": {
   "url": "https://example.com"
 }
}
"""
        }

    def chat(self, user_input):

        self.history.append({
            "role": "user",
            "content": user_input
        })

        messages = [self.system_prompt] + self.history

        response = ask_llm(messages)

        tool_call = parse_tool_response(response)

        if tool_call:

            tool_name = tool_call["tool"]
            args = tool_call.get("args", {})

            tool = get_tool(tool_name)

            if tool:
                result = tool(**args)

                return f"Tool executed: {result}"

            else:
                return "Tool not found."

        self.history.append({
            "role": "assistant",
            "content": response
        })

        return response
