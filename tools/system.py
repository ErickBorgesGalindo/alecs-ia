import subprocess
from tools.registry import register_tool

def run_command(command):

    try:
        subprocess.Popen(command, shell=True)
        return f"Running command: {command}"
    except Exception as e:
        return str(e)

register_tool("run_command", run_command)
