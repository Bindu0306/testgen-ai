# TestGen AI — LLM Powered Unit Test Generator

TestGen AI is a research prototype that evaluates how well Large Language Models (LLMs) generate Python unit tests.

The system automatically generates pytest test cases using local LLMs and evaluates them through syntax validation, test execution, code coverage analysis, and model benchmarking.

The goal of this project is to explore how reliable LLMs are at generating **correct and meaningful automated tests for software systems**.

---

# Overview

LLM-generated code is becoming common in modern development workflows. However, evaluating the **quality of generated unit tests** is still an open problem.

This project builds an automated evaluation pipeline that measures:

• Syntax correctness of generated tests  
• Logical correctness using pytest execution  
• Code coverage achieved by generated tests  
• Comparative performance across multiple LLMs  

The system provides a simple interface to generate tests, validate them, and benchmark different models.

---

# Architecture

Python Source Code  
↓  
LLM generates pytest tests  
↓  
Syntax validation  
↓  
Execute tests using pytest  
↓  
Measure coverage  
↓  
Benchmark models  

This pipeline enables automated evaluation of test quality produced by different LLMs.

---

# Features

• LLM-powered pytest unit test generation  
• Syntax validation for generated code  
• Automated execution of generated tests using pytest  
• Code coverage measurement using coverage.py  
• Multi-model benchmarking framework  
• Leaderboard scoring system for model comparison  
• Interactive UI built with Gradio  

---

# Models Evaluated

This project currently benchmarks the following open-source models:

- Qwen2.5 Coder
- DeepSeek Coder
- Gemma2
- Phi3 Mini

These models are evaluated on their ability to generate valid and logically correct unit tests.

---

# Example Leaderboard

| Model | Syntax Valid | Tests Passed | Coverage | Score |
|------|------|------|------|------|
| gemma2:2b | ✓ | ✓ | 100% | 100 |
| qwen2.5-coder | ✓ | ✗ | 100% | 60 |
| deepseek-coder | ✓ | ✗ | 100% | 60 |
| phi3-mini | ✗ | ✗ | 0% | 0 |

Score is calculated based on:

- Syntax correctness
- Test execution success
- Code coverage

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Bindu0306/testgen-ai.git
cd testgen-ai
Install dependencies:Install dependencies: pip install -r requirements.txt
Run the Application :python app.py

How the System Works:
User provides a Python function.
The LLM generates pytest unit tests.
Generated tests are validated for syntax.
Tests are executed using pytest.
Code coverage is calculated.
Benchmark results are displayed in a leaderboard.
This pipeline allows automated evaluation of test generation quality across different models.

Project Structure:
testgen-ai
│
├── app.py            # Gradio user interface
├── benchmark.py      # Model benchmarking logic
├── llm.py            # LLM inference module
├── validator.py      # Syntax validation, pytest execution, coverage
├── prompts.py        # Prompt templates used for test generation
├── styles.py         # UI styling for the Gradio app
├── requirements.txt  # Python dependencies
└── README.md

Research Motivation:
Evaluating LLM-generated tests requires more than verifying whether the code compiles.
This project focuses on measuring the quality and usefulness of generated tests through automated evaluation.
Key evaluation metrics include:
Syntax correctness
Test pass rate
Code coverage
Model reliability
The system helps identify which LLMs produce the most reliable automated tests.

Future Improvements

Possible extensions of this research project include:
• Benchmark models across larger datasets of functions
• Introduce mutation testing for deeper evaluation
• Support additional programming languages
• Build a standardized LLM test generation benchmark suite
• Integrate more open-source models for comparison
