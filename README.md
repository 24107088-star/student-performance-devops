# Agile Assignment 2 — Student Performance Prediction

This project demonstrates the three assignment questions using synthetic training data generated in `app/data.py`. It does not download or use the Iris dataset.

## Requirements
Windows, Python 3.12 recommended, Git, VS Code, Docker Desktop with its engine running.

## 1. Open the project
Extract this ZIP, open the extracted folder in VS Code, and open Terminal > New Terminal. Ensure the terminal is in the folder containing `requirements.txt`.

## 2. Install packages
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```
If PowerShell blocks activation, use Command Prompt and `.venv\Scripts\activate.bat`.

## 3. Train model and run locally
```powershell
python train.py
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000/docs and test POST `/predict`. Health check: http://127.0.0.1:8000/health. Metrics: http://127.0.0.1:8000/metrics.

Sample prediction input:
```json
{"study_hours":4,"attendance":85,"previous_score":72}
```

In another terminal (activate `.venv` first):
```powershell
pytest -v
```

## Question 1: Docker Compose
Stop local Uvicorn with Ctrl+C. Ensure Docker Desktop is running:
```powershell
docker --version
docker compose version
docker compose up --build -d
docker compose ps
```
Open API http://localhost:8000/docs, Prometheus http://localhost:9090/targets, Grafana http://localhost:3000. Initial Grafana credentials: admin / admin. To stop: `docker compose down`.

GitHub Actions tests and builds the Docker image after pushing to GitHub. The workflow does not publish to a registry or deploy to a remote server; those require additional secrets and a deployment target.

## Question 2: MLflow
Start MLflow UI in a terminal with `.venv` active:
```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000
```
In another terminal:
```powershell
$env:MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
python train.py
```
Open http://127.0.0.1:5000. Review run parameters, accuracy, and model artifact. Model Registry availability depends on MLflow version and backend configuration.

Prometheus scrapes API metrics. Grafana is preconfigured with a basic API request/latency dashboard. Generate several requests in `/docs` before inspecting metrics.

## Question 3: End-to-end
Use `architecture.mmd` as the architecture diagram. Use `JIRA_WORKFLOW.md` to create your Jira story, acceptance criteria, and tasks. Capture actual screenshots of Jira, GitHub Actions, Docker Compose, MLflow, Prometheus, and Grafana.

## Evidence checklist
- API prediction response
- pytest passing
- GitHub Actions successful run
- Docker Compose services running
- MLflow experiment with parameters and accuracy
- Prometheus target UP
- Grafana metrics dashboard
- Jira sprint board and architecture diagram

Do not claim remote deployment or successful runs unless you have performed them and captured the evidence.
