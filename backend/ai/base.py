class AIExplainer:
    def explain(self, phone, target, lens, settings) -> str:
        raise NotImplementedError

    def generate_content(self, prompt: str) -> str:
        """
        Generates raw text content from the AI based on a prompt.
        """
        raise NotImplementedError
