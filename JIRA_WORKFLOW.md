# Question 3: Jira evidence

Create a Jira Scrum project and add this story:

**Story:** As a user, I want to enter study hours, attendance, and previous score and receive a predicted performance category.

**Acceptance criteria**
- `/health` returns status `ok`.
- `/predict` accepts valid values.
- Attendance and scores outside 0–100 are rejected; study hours outside 0–24 are rejected.
- Automated tests pass in GitHub Actions.
- Docker Compose starts the API and monitoring services.
- Prometheus scrapes API metrics and Grafana visualizes them.
- MLflow records model parameters and accuracy.

**Tasks**
1. Build the prediction API.
2. Create synthetic training data and train a model.
3. Add tests.
4. Add Docker and Compose.
5. Configure GitHub Actions.
6. Configure MLflow.
7. Configure Prometheus and Grafana.
8. Capture actual execution evidence.

Move the issue through To Do, In Progress, and Done as the work is completed. Capture your own screenshots from Jira.
