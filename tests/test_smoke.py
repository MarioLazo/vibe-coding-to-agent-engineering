from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_readme_mentions_openhands():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "OpenHands" in readme


def test_exercises_readme_lists_exercises():
    exercises_readme = (ROOT / "exercises" / "README.md").read_text(encoding="utf-8")
    assert "Exercise 1" in exercises_readme
    assert "Exercise 6" in exercises_readme
