import json
import re


def parse_tool_response(text):

    try:
        # buscar bloque JSON dentro del texto
        json_match = re.search(r'\{.*\}', text, re.DOTALL)

        if not json_match:
            return None

        json_str = json_match.group(0)

        data = json.loads(json_str)

        if "tool" in data:
            return data

    except Exception:
        pass

    return None
