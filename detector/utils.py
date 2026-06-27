import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TERRAFORM_DIR = os.path.join(BASE_DIR, "..", "terraform")


def run_terraform_plan():
    result = subprocess.run(
        ["terraform", "plan"],
        cwd=TERRAFORM_DIR,
        capture_output=True,
        text=True
    )

    return result.stdout