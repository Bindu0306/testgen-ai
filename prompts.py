TEST_GEN_PROMPT = """
You are an expert Python test engineer.

Your task is to generate high-quality pytest unit tests for the given Python code.

Rules:
1. Return only valid Python test code.
2. Use pytest style.
3. Cover normal cases, edge cases, and negative cases where appropriate.
4. Do not include explanations.
5. Do not wrap the answer in markdown code fences.
6. Assume the source code will be available in a module named target_code.

Python source code:
{code}
"""