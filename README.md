🇭🇺 [Magyar verzió](README_hu.md)
# Knowledge-injection-ai
 AI should not remember. Your system should.


A simple concept for providing structured knowledge to AI systems at runtime.

This repository explores an alternative to model training: instead of teaching 
the model permanently, the system provides the required knowledge for each 
task in a structured way.

The injected knowledge includes:
- rules
- constraints
- validation requirements
- examples
- task definition

This makes the behavior of the AI system easier to control,
inspect, and compare across models.

## Why not fine-tuning?

- hard to control
- not auditable
- not versionable

## Why runtime knowledge?

- controllable
- testable
- model independent


---
## use case archtecture
knowledge/ -> prompt builder -> LLM -> validation -> result

## How it works


## Repository structure

- knowledge/
  - examples/
  - constraints.md
  - rules.md
  - validation.md
  - task.md
- main.py

---

## Components

### examples/
Contains executable examples that define expected behavior.  
Each example describes an input and the expected output.

### task.md
Defines the task the AI must perform.

### constraints.md
Defines what the AI is NOT allowed to do (e.g. no hallucination, no guessing).

### rules.md
Defines how the AI should behave and format the output.

### validation.md
Defines what a correct output means.

---

## Example usage

```python
from prompt_builder import build_prompt

prompt = build_prompt(
    knowledge_path="knowledge",
    input_text="user: Alice"
)

print(prompt)
```
## Example
This project contains an example of how to use the knowledge injection system.

## Good to know
If the LLM supports your native language, you can use it in that as well.   
I tested it in Hungarian, and it worked well.