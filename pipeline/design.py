from pipeline.llm import generate_json

def design_system(intent: dict):

    with open("prompts/design_prompt.txt", "r") as file:
        system_prompt = file.read()

    result = generate_json(
        system_prompt=system_prompt,
        user_prompt=str(intent)
    )

    return result