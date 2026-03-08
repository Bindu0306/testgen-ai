from llm import generate_tests
from validator import validate_syntax, save_files, run_pytest, run_coverage

MODELS = [
    "qwen2.5-coder:1.5b",
    "deepseek-coder:1.3b",
    "gemma2:2b",
    "phi3:mini"
]


def extract_coverage_percent(coverage_output):
    try:
        lines = coverage_output.split("\n")
        for line in lines:
            if "TOTAL" in line:
                parts = line.split()
                return int(parts[-1].replace("%", ""))
    except:
        return 0
    return 0


def compute_score(syntax_ok, pytest_ok, coverage_percent):
    score = 0
    if syntax_ok:
        score += 30
    if pytest_ok:
        score += 40

    score += int((coverage_percent / 100) * 30)

    return score


def run_benchmark(source_code):

    leaderboard = []

    for model in MODELS:

        tests = generate_tests(model, source_code)

        src_valid, _ = validate_syntax(source_code)
        test_valid, _ = validate_syntax(tests)

        syntax_ok = src_valid and test_valid

        save_files(source_code, tests)

        pytest_ok, _ = run_pytest()

        coverage_ok, coverage_output = run_coverage()

        coverage_percent = extract_coverage_percent(coverage_output) if coverage_ok else 0

        score = compute_score(syntax_ok, pytest_ok, coverage_percent)

        leaderboard.append([
            model,
            syntax_ok,
            pytest_ok,
            f"{coverage_percent}%",
            score
        ])

    leaderboard.sort(key=lambda x: x[4], reverse=True)

    return leaderboard