from ai.llm import ask_llm

class AlecsIA:

    def chat(self, message: str) -> str:
        response = ask_llm(message)
        return response
