import os
import joblib
import mlflow
import mlflow.sklearn
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from app.data import training_data

def main():
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db"))
    mlflow.set_experiment("student-performance-prediction")
    X, y = training_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    n_estimators = 120
    model = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
    with mlflow.start_run() as run:
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        accuracy = float(accuracy_score(y_test, predictions))
        mlflow.log_param("model_type", "RandomForestClassifier")
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("training_rows", len(X_train))
        mlflow.log_param("test_rows", len(X_test))
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("number_of_classes", len(set(y)))
        output_path = Path("app") / "student_model.joblib"
        joblib.dump({"model": model}, output_path)
        mlflow.sklearn.log_model(
            sk_model=model,
            name="student_performance_model",
            registered_model_name="StudentPerformanceClassifier",
            skops_trusted_types=["sklearn.tree._tree.Tree"],
    )
        print(f"Run ID: {run.info.run_id}")
        print(f"Test accuracy: {accuracy:.4f}")
        print(f"Classes: {sorted(set(y))}")
        print(f"Saved model to: {output_path.resolve()}")
        print("Model version registration is attempted through MLflow Registry.")

if __name__ == "__main__":
    main()
