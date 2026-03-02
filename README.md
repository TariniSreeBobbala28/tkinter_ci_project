# Tkinter Unit Converter with CI Pipeline

## 🚀 Project Overview
This is a professional **Multi-Unit Converter** built with Python. I developed this to demonstrate a full **CI/CD lifecycle**, ensuring that every code change is automatically tested before deployment.

## 🛠️ Features
* **Accurate Conversions**: Celsius to Fahrenheit and Meters to Feet.
* **Automated Testing**: Built-in unit tests using `pytest`.
* **CI/CD Integration**: Fully automated workflow via **GitHub Actions**.
* **Environment Portability**: Uses `requirements.txt` for easy setup on any machine.

## 💻 Technical Stack
* **Language**: Python 3.11+
* **GUI Framework**: Tkinter
* **DevOps Tools**: Git, GitHub Actions, Pytest
* **OS Environment**: Windows (Local) / Ubuntu (GitHub Runner)

## ⚙️ Setup & Installation
To run this project on your local machine:

1. **Clone the Repo**:
   `git clone https://github.com/TariniSreeBobbala28/tkinter_ci_project.git`
2. **Create Virtual Environment**:
   `python -m venv venv`
3. **Activate Environment**:
   * CMD: `venv\Scripts\activate.bat`
   * PowerShell: `powershell -ExecutionPolicy ByPass -File venv\Scripts\Activate.ps1`
4. **Install Requirements**:
   `pip install -r requirements.txt`
5. **Run App**:
   `python app.py`

## 🛡️ DevOps Proof (GitHub Actions)
The `.github/workflows/ci.yml` file ensures that every `git push` triggers:
1. A fresh Ubuntu build.
2. Dependency installation.
3. Automated test execution.
**Current Status**: Passing (Green Checkmark ✅)
