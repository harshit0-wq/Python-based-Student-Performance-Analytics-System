# Project Documentation

## 1. Project Title
**Student Performance Analytics System**  
Student: **Harshit Aadarsh**

## 2. Objective
The project analyzes student academic records and converts raw marks and attendance into easy-to-understand results. It calculates each student's total, average, grade and pass/fail outcome and provides class-level and subject-level insights.

## 3. Technologies Used
- Python 3
- NumPy for numerical calculations
- Pandas for DataFrame-based loading, processing, filtering and export
- CSV for the student dataset

## 4. Dataset Description
The project uses 20 fictional student records. Columns are Student_ID, Name, Department, Python, NumPy, Pandas, AI_Basics and Attendance. The data is synthetic and contains no real personal student information.

## 5. Implementation
1. `students.csv` is read with `pandas.read_csv()`.
2. Required columns are validated.
3. Subject marks are converted to a NumPy array.
4. NumPy calculates row-wise totals and averages.
5. A reusable function assigns grades from each average.
6. A loop checks every record for subject pass marks and attendance.
7. Pandas and NumPy calculate subject-wise high, low and mean marks.
8. Students are ranked by average to identify top performers.
9. The complete analyzed table is exported as `analysis_results.csv`.

## 6. Key Features
- Loads and displays 20 student records
- Total and average marks per student
- A+ to F grade assignment
- Pass/fail using marks and attendance
- Highest, lowest and class-average performance
- Subject-wise highest, lowest and average marks
- Best-performing subject
- Top five students
- CSV result export

## 7. Output / Screenshots
Run `python main.py` and capture the terminal sections titled Student Results, Subject-Wise Performance, Class Summary and Top 5 Performers if screenshots are requested by the trainer.

## 8. Final Outcome
The system successfully transforms a student CSV into student-level and class-level analytics. Results are printed clearly and also saved to CSV, making the analysis reproducible and easy to inspect.

## 9. Challenges & Learning
A key design task was defining unambiguous grade and pass/fail rules. The project separates reusable logic into functions, uses NumPy for numerical aggregation and Pandas for tabular analysis. It demonstrates how loops, conditions and vectorized data operations can be combined in one practical program.

## 10. GitHub Repository
Add the final public repository URL here after uploading:  
`https://github.com/YOUR_USERNAME/student-performance-analytics`
