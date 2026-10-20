from time import perf_counter
from fastapi import FastAPI
from pydantic import BaseModel, Field
from prometheus_client import Counter, Histogram, make_asgi_app
from app.model import get_model

app = FastAPI(title="Student Performance Prediction API", version="1.0.0")
REQUESTS = Counter("api_requests_total", "Total API requests", ["endpoint", "method"])
PREDICTION_LATENCY = Histogram("prediction_latency_seconds", "Prediction processing time")

class StudentInput(BaseModel):
    study_hours: float = Field(ge=0, le=24, examples=[4])
    attendance: float = Field(ge=0, le=100, examples=[85])
    previous_score: float = Field(ge=0, le=100, examples=[72])

@app.middleware("http")
async def count_requests(request, call_next):
    response = await call_next(request)
    if request.url.path != "/metrics":
        REQUESTS.labels(request.url.path, request.method).inc()
    return response

app.mount("/metrics", make_asgi_app())

@app.get("/")
def root():
    return {"message": "Student Performance Prediction API", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(student: StudentInput):
    with PREDICTION_LATENCY.time():
        model = get_model()
        prediction = str(model.predict([[
            student.study_hours, student.attendance, student.previous_score
        ]])[0])
    return {
        "predicted_category": prediction,
        "input": student.model_dump()
    }
