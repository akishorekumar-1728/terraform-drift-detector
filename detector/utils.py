import subprocess

def run_terraform_plan():
    result = subprocess.run(
        ["terraform", "plan"],
        cwd="../terraform",
        capture_output=True,
        text=True
    )

    return result.stdout