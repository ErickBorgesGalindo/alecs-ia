import webbrowser
from tools.registry import register_tool


def open_browser(url):

    webbrowser.open(url)

    return f"Opening {url}"


register_tool(
    "open_browser",
    open_browser,
    "Opens a website in the default browser. Argument: url"
)
