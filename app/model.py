from functools import lru_cache
from pathlib import Path
import joblib
from sklearn.ensemble import RandomForestClassifier
from app.data import training_data

MODEL_PATH = Path(__file__).resolve().parent / "student_model.joblib"

@lru_cache(maxsize=1)
def get_model():
    if MODEL_PATH.exists():
        saved = joblib.load(MODEL_PATH)
        return saved["model"] if isinstance(saved, dict) else saved
    X, y = training_data()
    model = RandomForestClassifier(n_estimators=120, random_state=42)
    model.fit(X, y)
    return model
