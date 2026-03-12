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

If you use a tool you MUST wait for the result.

After receiving the tool result you MUST respond normally
to the user explaining what happened.

Only use a tool once per request.

Tool format:

{{
 "tool": "tool_name",
 "args": {{ }}
}}
IMPORTANT:

When calling a tool respond ONLY with JSON.
Do not include explanations.
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

        if not tool_call:

            self.history.append({
                "role": "assistant",
                "content": response
            })

            return response

        tool_name = tool_call["tool"]
        args = tool_call.get("args", {})

        tool = get_tool(tool_name)

        if not tool:
            return "Tool not found."

        result = tool(**args)

        self.history.append({
            "role": "assistant",
            "content": f"Tool result: {result}"
        })

        messages = [self.system_prompt] + self.history

        final_response = ask_llm(messages)

        self.history.append({
            "role": "assistant",
            "content": final_response
        })

        return final_response
