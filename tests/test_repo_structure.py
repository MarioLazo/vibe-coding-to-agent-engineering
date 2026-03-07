from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


EXPECTED_FILES = [
    ROOT / "README.md",
    ROOT / "exercises" / "exercise1_hello.py",
    ROOT / "exercises" / "exercise2_script.py",
    ROOT / "exercises" / "exercise3_todo.py",
    ROOT / "exercises" / "exercise4_debug.py",
    ROOT / "exercises" / "exercise5_refactor.py",
    ROOT / "exercises" / "exercise6_ci.py",
    ROOT / "slides" / "index.html",
]


def test_expected_files_exist():
    missing = [path for path in EXPECTED_FILES if not path.exists()]
    assert not missing, f"Missing expected files: {missing}"


def test_exercise_files_have_shebang():
    exercise_files = [path for path in EXPECTED_FILES if path.suffix == ".py"]
    missing_shebang = []
    for path in exercise_files:
        first_line = path.read_text(encoding="utf-8").splitlines()[0]
        if not first_line.startswith("#!/usr/bin/env python3"):
            missing_shebang.append(path)
    assert not missing_shebang, f"Missing shebangs: {missing_shebang}"
