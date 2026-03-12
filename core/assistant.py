from ai.llm import ask_llm
from tools.registry import get_tool
from utils.tool_parser import parse_tool_response
from utils.tool_prompt import generate_tool_prompt

import tools.open_browser
import tools.system


class AlecsIA:

    def __init__(self):

        self.history = []

        tools_description = generate_tool_prompt()

        self.system_prompt = {
            "role": "system",
            "content": f"""
You are AlecsIA, a personal assistant.

You can use tools to perform actions.

{tools_description}

If you need to use a tool respond ONLY in JSON.

Example:

{{
 "tool": "open_browser",
 "args": {{
   "url": "https://github.com"
 }}
}}
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
