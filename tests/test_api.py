from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Student Performance" in response.json()["message"]

def test_prediction():
    response = client.post("/predict", json={
        "study_hours": 4,
        "attendance": 85,
        "previous_score": 72
    })
    assert response.status_code == 200
    assert response.json()["predicted_category"] in [
        "Needs Support", "Satisfactory", "Excellent"
    ]

def test_invalid_attendance():
    response = client.post("/predict", json={
        "study_hours": 4,
        "attendance": 150,
        "previous_score": 72
    })
    assert response.status_code == 422
