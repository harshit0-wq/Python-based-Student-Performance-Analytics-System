# Student Performance Analytics System

Python data-analysis mini project using **NumPy** and **Pandas**. It loads 20 dummy student records, calculates total/average marks, assigns grades, decides pass/fail, performs subject-wise analysis, identifies top performers, and exports the final results.

## Grading and pass rules
- A+: 90-100, A: 80-89.99, B: 70-79.99, C: 60-69.99, D: 50-59.99, E: 40-49.99, F: below 40.
- Pass requires **at least 40 in every subject** and **attendance of at least 75%**.

## Files
- `main.py` - runs and prints the analysis
- `functions.py` - reusable calculation/analysis functions
- `students.csv` - 20 fictional student records
- `analysis_results.csv` - generated analyzed data
- `Project_Documentation.md` - complete project write-up
- `requirements.txt` - dependencies

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## GitHub submission
```bash
git init
git add .
git commit -m "Complete student performance analytics project"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/student-performance-analytics.git
git push -u origin main
```
Replace `YOUR_USERNAME` with your GitHub username, verify all files online, then copy the repository URL into the EWB Google Form.

## Concepts demonstrated
Variables and data types, conditions, loops, functions, NumPy arrays and calculations, Pandas DataFrames, CSV loading/export, filtering, aggregation, ranking, and descriptive analysis.
