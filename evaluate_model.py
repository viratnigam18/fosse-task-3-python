from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Your choice
# Choose a code-capable open-source model
# You can swap this with "meta-llama/CodeLlama-7b-hf" or "tiiuae/falcon-7b-instruct"
model_name = "bigcode/starcoder2-15b"

print(f"Loading model: {model_name}")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Example of a student code which has a bug
student_code = """
for i in range(1,10):
print(i)
"""

prompt = f"""You are a teacher. Read this student's Python code and list 3 hints (not the full solution) to debug it:
```python
{student_code}
