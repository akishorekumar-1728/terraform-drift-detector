import os
import json
from datetime import datetime

REPORT_DIR = "../reports"
os.makedirs(REPORT_DIR, exist_ok=True)

def save_report(terraform_output, drift):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Terraform Drift Report</title>
        <style>
            body {{
                font-family: Arial;
                margin:40px;
                background:#f5f5f5;
            }}

            h1 {{
                color:#1565C0;
            }}

            .status {{
                padding:10px;
                font-size:18px;
                font-weight:bold;
                border-radius:6px;
                width:250px;
            }}

            .drift {{
                background:#ffdddd;
                color:red;
            }}

            .clean {{
                background:#ddffdd;
                color:green;
            }}

            pre {{
                background:white;
                padding:20px;
                overflow:auto;
            }}
        </style>
    </head>

    <body>

    <h1>Terraform Drift Report</h1>

    <p><b>Generated:</b> {timestamp}</p>

    <div class="status {'drift' if drift else 'clean'}">
        {" Drift Detected" if drift else " No Drift"}
    </div>

    <h2>Terraform Output</h2>

    <pre>{terraform_output}</pre>

    </body>

    </html>
    """

    with open(f"{REPORT_DIR}/drift_report.html","w",encoding="utf-8") as f:
        f.write(html)

    json_report = {
        "generated": timestamp,
        "drift_detected": drift,
        "terraform_output": terraform_output
    }

    with open(f"{REPORT_DIR}/drift_report.json","w") as f:
        json.dump(json_report,f,indent=4)