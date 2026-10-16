import numpy as np
import pandas as pd

SUBJECTS = ["Python", "NumPy", "Pandas", "AI_Basics"]
PASS_MARK = 40
MIN_ATTENDANCE = 75

def load_data(file_path="students.csv"):
    """Load the student CSV and perform basic validation."""
    df = pd.read_csv(file_path)
    required = ["Student_ID", "Name", "Department", *SUBJECTS, "Attendance"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")
    return df

def grade_from_average(avg):
    """Return a grade from the student's average marks."""
    if avg >= 90: return "A+"
    if avg >= 80: return "A"
    if avg >= 70: return "B"
    if avg >= 60: return "C"
    if avg >= 50: return "D"
    if avg >= 40: return "E"
    return "F"

def process_students(df):
    """Calculate totals, averages, grades and pass/fail status."""
    marks = df[SUBJECTS].to_numpy(dtype=float)
    df = df.copy()
    df["Total"] = np.sum(marks, axis=1).astype(int)
    df["Average"] = np.round(np.mean(marks, axis=1), 2)

    # A loop is intentionally used because the assignment evaluates loop usage.
    grades, statuses = [], []
    for _, row in df.iterrows():
        grades.append(grade_from_average(row["Average"]))
        subject_pass = all(row[s] >= PASS_MARK for s in SUBJECTS)
        attendance_ok = row["Attendance"] >= MIN_ATTENDANCE
        statuses.append("Pass" if subject_pass and attendance_ok else "Fail")

    df["Grade"] = grades
    df["Status"] = statuses
    return df

def subject_analysis(df):
    """Build subject-wise highest, lowest and average statistics."""
    return pd.DataFrame({
        "Subject": SUBJECTS,
        "Highest": [df[s].max() for s in SUBJECTS],
        "Lowest": [df[s].min() for s in SUBJECTS],
        "Average": [round(float(np.mean(df[s].to_numpy())), 2) for s in SUBJECTS],
    })

def overall_summary(df):
    top = df.loc[df["Average"].idxmax()]
    low = df.loc[df["Average"].idxmin()]
    return {
        "highest_student": top["Name"],
        "highest_average": float(top["Average"]),
        "lowest_student": low["Name"],
        "lowest_average": float(low["Average"]),
        "class_average": round(float(np.mean(df["Average"].to_numpy())), 2),
        "passed": int((df["Status"] == "Pass").sum()),
        "failed": int((df["Status"] == "Fail").sum()),
    }
