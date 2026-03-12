import subprocess
from tools.registry import register_tool


def run_command(command):

    subprocess.Popen(command, shell=True)

    return f"Running command: {command}"


register_tool(
    "run_command",
    run_command,
    "Runs a system command. Argument: command"
)
