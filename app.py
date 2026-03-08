import gradio as gr
from styles import CSS
from llm import generate_tests
from validator import validate_syntax, save_files, run_pytest, run_coverage
from benchmark import run_benchmark

MODELS = [
    "qwen2.5-coder:1.5b",
    "deepseek-coder:1.3b",
    "gemma2:2b",
    "phi3:mini"
]

sample_code = '''def add(a, b):
    return a + b
'''


def generate_unit_tests(model_name, source_code):
    try:
        tests = generate_tests(model_name, source_code)
        return tests
    except Exception as e:
        return f"Error generating tests: {e}"


def evaluate_tests(source_code, test_code):
    source_ok, source_msg = validate_syntax(source_code)
    test_ok, test_msg = validate_syntax(test_code)

    if not source_ok:
        return source_msg, "", ""

    if not test_ok:
        return "", test_msg, ""

    save_files(source_code, test_code)

    pytest_ok, pytest_output = run_pytest()
    coverage_ok, coverage_output = run_coverage()

    return (
        f"Source: {source_msg}\nTests: {test_msg}",
        pytest_output,
        coverage_output if coverage_ok else "Coverage failed"
    )


with gr.Blocks(css=CSS, theme=gr.themes.Monochrome(), title="TestGen AI") as ui:

    gr.Markdown("## TestGen AI — LLM-Powered Unit Test Generator")

    # Model selector
    with gr.Row():
        model_dropdown = gr.Dropdown(
            choices=MODELS,
            value=MODELS[0],
            label="Select Model"
        )

    # Code editors
    with gr.Row(equal_height=True):

        with gr.Column(scale=6):
            source_code = gr.Code(
                label="Python Source Code",
                value=sample_code,
                language="python",
                lines=22
            )

        with gr.Column(scale=6):
            generated_tests = gr.Code(
                label="Generated Pytest Tests",
                value="",
                language="python",
                lines=22
            )

    # Buttons
    with gr.Row():
        generate_btn = gr.Button("Generate Tests")
        evaluate_btn = gr.Button("Evaluate Tests")
        benchmark_btn = gr.Button("Run Benchmark")

    # Output panels
    with gr.Row():
        syntax_box = gr.TextArea(label="Syntax Validation", lines=4)
        pytest_box = gr.TextArea(label="Pytest Output", lines=10)
        coverage_box = gr.TextArea(label="Coverage Output", lines=10)

    # Leaderboard
    leaderboard_table = gr.Dataframe(
        headers=["Model", "Syntax Valid", "Tests Passed", "Coverage", "Score"],
        interactive=False,
        label="Model Leaderboard"
    )

    # Generate tests
    generate_btn.click(
        fn=generate_unit_tests,
        inputs=[model_dropdown, source_code],
        outputs=[generated_tests]
    )

    # Evaluate tests
    evaluate_btn.click(
        fn=evaluate_tests,
        inputs=[source_code, generated_tests],
        outputs=[syntax_box, pytest_box, coverage_box]
    )

    # Run benchmark across models
    benchmark_btn.click(
        fn=run_benchmark,
        inputs=[source_code],
        outputs=[leaderboard_table]
    )


ui.launch(inbrowser=True)