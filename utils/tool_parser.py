import json

def parse_tool_response(text):

    try:
        data = json.loads(text)

        if "tool" in data:
            return data

    except:
        pass

    return None
