import ast
import subprocess
import sys
from pathlib import Path

TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)

TARGET_FILE = TEMP_DIR / "target_code.py"
TEST_FILE = TEMP_DIR / "test_target_code.py"


def validate_syntax(code: str):
    try:
        ast.parse(code)
        return True, "Syntax valid"
    except SyntaxError as e:
        return False, f"Syntax error: {e}"


def save_files(source_code: str, test_code: str):
    TARGET_FILE.write_text(source_code, encoding="utf-8")

    # Ensure tests import the target code
    test_with_import = "from target_code import *\n\n" + test_code

    TEST_FILE.write_text(test_with_import, encoding="utf-8")


def run_pytest():
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(TEST_FILE), "-v"],
            capture_output=True,
            text=True,
            timeout=60,
            cwd="."
        )
        output = result.stdout + "\n" + result.stderr
        return result.returncode == 0, output
    except Exception as e:
        return False, str(e)


def run_coverage():
    try:
        subprocess.run(
            [sys.executable, "-m", "coverage", "run", "-m", "pytest", str(TEST_FILE)],
            capture_output=True,
            text=True,
            timeout=60,
            cwd="."
        )

        report = subprocess.run(
            [sys.executable, "-m", "coverage", "report", "-m"],
            capture_output=True,
            text=True,
            timeout=60,
            cwd="."
        )
        return True, report.stdout + "\n" + report.stderr
    except Exception as e:
        return False, str(e)