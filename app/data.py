# Small synthetic dataset created in code; no external dataset is downloaded.
# Features: study hours per day, attendance percentage, previous exam score.
# Labels: Needs Support, Satisfactory, Excellent.
def training_data():
    rows = []
    labels = []
    for study_hours in range(1, 9):
        for attendance in (50, 60, 70, 80, 90, 100):
            for previous_score in (35, 45, 55, 65, 75, 85, 95):
                # Transparent demonstration rule used only to create synthetic labels.
                score = 4.0 * study_hours + 0.25 * attendance + 0.35 * previous_score
                if score < 42:
                    label = "Needs Support"
                elif score < 58:
                    label = "Satisfactory"
                else:
                    label = "Excellent"
                rows.append([float(study_hours), float(attendance), float(previous_score)])
                labels.append(label)
    return rows, labels
