import shutil
from pathlib import Path
from string import ascii_lowercase

import pyperclip

print("input contest name.")
print("example: abc284")
print()

contest_name = input("type here: ")
contest_dir_path = Path() / "atcoder.jp" / "contests" / contest_name / "tasks"
templates_py_path = Path() / "templates" / "main.py"

for ch in ascii_lowercase[:5]:
    problem_dir_name = contest_name + "_" + ch
    problem_dir_path = contest_dir_path / problem_dir_name
    problem_dir_path.mkdir(parents=True, exist_ok=True)
    shutil.copy(templates_py_path, problem_dir_path)

problem_a = contest_name + "_a"
to_copied = ["acac", "https://" + str(contest_dir_path / problem_a), "-m"]
pyperclip.copy(" ".join(to_copied))  # type: ignore
