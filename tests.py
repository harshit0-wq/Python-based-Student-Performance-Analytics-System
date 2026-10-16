from pathlib import Path
from functions import load_data, process_students, subject_analysis, overall_summary
base=Path(__file__).resolve().parent
df=process_students(load_data(base/'students.csv'))
assert len(df)==20
assert set(['Total','Average','Grade','Status']).issubset(df.columns)
assert len(subject_analysis(df))==4
summary=overall_summary(df)
assert summary['passed'] + summary['failed'] == 20
assert df['Average'].between(0,100).all()
print('All project checks passed.')
