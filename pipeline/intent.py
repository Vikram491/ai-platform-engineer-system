from pipeline.llm import generate_json

def extract_intent(prompt: str):

    with open("prompts/intent_prompt.txt", "r") as file:
        system_prompt = file.read()

    result = generate_json(
        system_prompt=system_prompt,
        user_prompt=prompt
    )

    return result