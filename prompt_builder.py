import os


def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def load_examples(path):
    examples = []

    for file in sorted(os.listdir(path)):
        if file.endswith(".py"):
            data = {}
            with open(os.path.join(path, file), "r", encoding="utf-8") as f:
                code = f.read()

            # ⚠️ prototípus: exec (trusted környezet!)
            exec(code, {}, data)

            # támogatjuk több formátumot
            if "case" in data:
                examples.append(data["case"])
            elif "input_data" in data and "expected_output" in data:
                examples.append({
                    "input": data["input_data"],
                    "expected": data["expected_output"]
                })

    return examples


def format_examples(examples):
    formatted = []

    for e in examples:
        formatted.append(
            f"Input:\n{e['input']}\n\nOutput:\n{e['expected']}"
        )

    return "\n\n---\n\n".join(formatted)


def build_prompt(knowledge_path, input_text):

    rules_md = load_file(os.path.join(knowledge_path, "rules.md"))
    task_md = load_file(os.path.join(knowledge_path, "task.md"))
    examples = load_examples(os.path.join(knowledge_path, "examples"))

    examples_text = format_examples(examples)

    prompt = f"""
You are a deterministic system that must follow strict rules.

# RULES
{rules_md}

# TASK
{task_md}

# EXAMPLES
{examples_text}

# INPUT
{input_text}

# OUTPUT REQUIREMENTS
- Follow the rules strictly
- Do not add explanations
- Return only the expected format
"""

    return prompt.strip()


#