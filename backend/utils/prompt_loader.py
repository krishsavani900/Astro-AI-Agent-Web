from pathlib import Path


def load_prompt(name: str) -> str:
    # Adjust parents index based on your actual folder structure.
    # If prompt_loader.py is in backend/utils/, parents[1] is backend/.
    base = Path(__file__).resolve().parents[1]
    prompt_path = base / "prompts" / name

    if not prompt_path.exists():
        raise FileNotFoundError(f"Prompt not found: {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")
