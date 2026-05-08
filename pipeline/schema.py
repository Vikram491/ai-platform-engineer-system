from pipeline.llm import generate_json

def generate_schema(design: dict):

    with open("prompts/schema_prompt.txt", "r") as file:
        system_prompt = file.read()

    result = generate_json(
        system_prompt=system_prompt,
        user_prompt=str(design)
    )

    return result