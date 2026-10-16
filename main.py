from pathlib import Path
from functions import load_data, process_students, subject_analysis, overall_summary

BASE_DIR = Path(__file__).resolve().parent

def main():
    df = load_data(BASE_DIR / "students.csv")
    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 72)
    print(f"Records loaded: {len(df)}")
    print(f"Columns: {', '.join(df.columns)}")

    result = process_students(df)
    subjects = subject_analysis(result)
    summary = overall_summary(result)

    print("\nSTUDENT RESULTS")
    print(result[["Student_ID", "Name", "Total", "Average", "Grade", "Status"]].to_string(index=False))

    print("\nSUBJECT-WISE PERFORMANCE")
    print(subjects.to_string(index=False))

    best = subjects.loc[subjects["Average"].idxmax()]
    print("\nCLASS SUMMARY")
    print(f"Highest average : {summary['highest_student']} ({summary['highest_average']:.2f})")
    print(f"Lowest average  : {summary['lowest_student']} ({summary['lowest_average']:.2f})")
    print(f"Overall average : {summary['class_average']:.2f}")
    print(f"Passed / Failed : {summary['passed']} / {summary['failed']}")
    print(f"Best subject    : {best['Subject']} ({best['Average']:.2f})")

    print("\nTOP 5 PERFORMERS")
    print(result.nlargest(5, "Average")[["Student_ID", "Name", "Average", "Grade"]].to_string(index=False))

    output = BASE_DIR / "analysis_results.csv"
    result.to_csv(output, index=False)
    print(f"\nDetailed analysis saved to: {output.name}")

if __name__ == "__main__":
    main()
