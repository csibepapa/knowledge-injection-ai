import json
import os


def load_file(path: str) -> str:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file_handle:
            return file_handle.read().strip()
    else:
        return ""


def load_examples(path: str) -> list[dict]:
    examples = []

    if not os.path.isdir(path):
        return examples

    for file_name in sorted(os.listdir(path)):
        file_path = os.path.join(path, file_name)

        if not os.path.isfile(file_path):
            continue

        if not file_name.endswith(".py"):
            continue

        data = {}
        with open(file_path, "r", encoding="utf-8") as file_handle:
            code = file_handle.read()

        # trusted prototype only
        exec(code, {}, data)

        if "case" in data:
            case = data["case"]
            if isinstance(case, dict) and "input" in case and "expected" in case:
                examples.append(case)

        elif "input_data" in data and "expected_output" in data:
            examples.append(
                {
                    "input": data["input_data"],
                    "expected": data["expected_output"],
                }
            )

    return examples


def stringify_output(value) -> str:
    if isinstance(value, (dict, list)):
        return json.dumps(value, indent=2, ensure_ascii=False)

    return str(value)


def format_examples(examples: list[dict]) -> str:
    if not examples:
        return "No examples provided."

    blocks = []

    for index, example in enumerate(examples, 1):
        example_input = str(example["input"]).strip()
        example_expected = stringify_output(example["expected"]).strip()

        blocks.append(
            f"""Example {index}:
Input:
{example_input}

Output:
{example_expected}"""
        )

    return "\n\n---\n\n".join(blocks)

def build_tree(path: str, prefix: str = "") -> str:
    lines = []

    items = sorted(os.listdir(path))

    for index, name in enumerate(items):
        full_path = os.path.join(path, name)
        is_last = index == len(items) - 1

        connector = "└── " if is_last else "├── "
        lines.append(f"{prefix}{connector}{name}")

        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            lines.append(build_tree(full_path, prefix + extension))

    return "\n".join(lines)



def build_prompt(knowledge_path: str) -> str:
    rules_md = load_file(os.path.join(knowledge_path, "rules.md"))
    task_md = load_file(os.path.join(knowledge_path, "task.md"))
    constraint_md = load_file(os.path.join(knowledge_path, "constaraint.md"))
    validation_md = load_file(os.path.join(knowledge_path, "validation.md"))
    examples = load_examples(os.path.join(knowledge_path, "examples"))

    tree = build_tree(os.path.join(knowledge_path, "examples"))
    examples_text = format_examples(examples)

    prompt = f"""
You are a deterministic system that must follow strict rules.

# PROJECT STRUCTURE

{tree}



# RULES
{rules_md}

# TASK
{task_md}

#CONSTRAINTS
{constraint_md}

#VALIDATION
{validation_md}

# EXAMPLES
{examples_text}

# OUTPUT REQUIREMENTS
- Follow the rules strictly
- Do not add explanations
- Return only the expected format
"""

    return prompt.strip()


if __name__ == "__main__":
    print(build_prompt("knowledge"))