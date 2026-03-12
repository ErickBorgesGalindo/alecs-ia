from tools.registry import list_tools


def generate_tool_prompt():

    tools = list_tools()

    prompt = "Available tools:\n\n"

    for name, data in tools.items():

        prompt += f"{name}: {data['description']}\n"

    return prompt
