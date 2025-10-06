# 🛠️ MLOps_repo

This repository is a hands-on collection of practical MLOps tasks and examples, designed to help you learn and apply core concepts in machine learning operations through simple, modular code.

## 📂 Structure

The repo is organized into task-based folders:

- `ex_1/` – Intro to MLOps and basic automation
- `ex_2/` – Environment setup, dependency management, and CI/CD basics
- `ex_3/` – Cloud deployment, testing, and containerization with FastAPI

Each folder contains self-contained code and instructions for completing a specific MLOps milestone.

---

## 🚀 Current Focus: `ex_3`

In `ex_3`, we build and deploy a minimal FastAPI app:

- ✅ FastAPI Hello World endpoint
- ✅ Pytest-based unit testing
- ✅ Docker containerization
- ✅ GitHub Actions for CI testing
- ✅ Deployment to Google Cloud Run (GCP)

### 🔧 Technologies Used

- Python 3.10
- FastAPI
- Uvicorn
- Pytest
- Docker
- GitHub Actions
- Google Cloud Platform (Cloud Run)

---

## 📦 How to Run Locally

```bash
cd ex_3
pip install -r requirements.txt
uvicorn app:app --reload
