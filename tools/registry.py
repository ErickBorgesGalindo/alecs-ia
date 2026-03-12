TOOLS = {}

def register_tool(name, func, description):

    TOOLS[name] = {
        "function": func,
        "description": description
    }


def get_tool(name):

    tool = TOOLS.get(name)

    if tool:
        return tool["function"]

    return None


def list_tools():

    return TOOLS
