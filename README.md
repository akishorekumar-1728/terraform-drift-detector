# Terraform Drift Detector

## Overview

Terraform Drift Detector is an open-source DevOps project that detects infrastructure drift between the Terraform state and the actual deployed infrastructure.

The project provisions infrastructure using Terraform and Docker, intentionally introduces configuration drift, detects the drift automatically using Python, and generates detailed reports.

---

## Features

- Infrastructure as Code using Terraform
- Docker-based infrastructure deployment
- Automated drift detection
- HTML drift report generation
- JSON report generation
- GitHub Actions workflow
- Python automation
- Open-source project structure

---

## Project Architecture

```
                +----------------+
                | Terraform Code |
                +--------+-------+
                         |
                         v
                  terraform apply
                         |
                         v
                Docker Container
                         |
          Manual Infrastructure Change
                         |
                         v
                  terraform plan
                         |
                         v
             Python Drift Detector
                         |
             +-----------+-----------+
             |                       |
             v                       v
       HTML Report             JSON Report
```

---

## Project Structure

```
terraform-drift-detector/

├── .github/
│   └── workflows/
│       └── drift.yml
│
├── detector/
│   ├── drift_detector.py
│   ├── parser.py
│   ├── reporter.py
│   └── utils.py
│
├── terraform/
│   ├── provider.tf
│   ├── main.tf
│   ├── outputs.tf
│
├── reports/
├── screenshots/
├── tests/
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Technologies Used

- Python
- Terraform
- Docker
- Git
- GitHub Actions
- PowerShell

---

## Installation

Clone the repository.

```bash
git clone https://github.com/akishorekumar-1728/terraform-drift-detector.git

cd terraform-drift-detector
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Deploy Infrastructure

```bash
cd terraform

terraform init

terraform apply
```

---

## Simulate Drift

Delete the running container.

```bash
docker rm -f terraform-nginx
```

Run

```bash
terraform plan
```

Terraform will display:

```
Objects have changed outside of Terraform
```

---

## Run Drift Detector

```bash
cd detector

python drift_detector.py
```

---

## Reports

The detector generates:

```
reports/

drift_report.html

drift_report.json
```

---

## Screenshots

### Terraform detects infrastructure drift

![Terraform Drift](screenshots/terraform-plan-drift.png)

---

### Docker Infrastructure

![Docker](screenshots/docker-container.png)

---

### HTML Drift Report

![HTML Report](screenshots/html-report.png)

---

### GitHub Actions

![GitHub Actions](screenshots/github-actions.png)

---

## Future Enhancements

- Azure Support
- AWS Support
- Email Notifications
- Slack Integration
- Microsoft Teams Alerts
- Kubernetes Drift Detection
- Multi-cloud Support

---

## Skills Demonstrated

- Infrastructure as Code
- DevOps Automation
- Terraform
- Docker
- Python
- GitHub Actions
- Infrastructure Drift Detection
- Open Source Development

---

## Author

**A. Kishore Kumar**

GitHub:

https://github.com/akishorekumar-1728

---

## License

MIT License