from colorama import Fore, init

from utils import run_terraform_plan
from parser import detect_drift
from reporter import save_report

init(autoreset=True)

print("=" * 60)
print("Terraform Drift Detector")
print("=" * 60)

terraform_output = run_terraform_plan()

drift = detect_drift(terraform_output)

if drift:
    print(Fore.RED + "\n Drift Detected!\n")
else:
    print(Fore.GREEN + "\n No Drift Detected!\n")

save_report(terraform_output, drift)

print("HTML Report Generated")

print("=" * 60)