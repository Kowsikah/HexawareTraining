import pandas as pd
import numpy as np
df=pd.read_csv('course_enrollment.csv')
#clean invalid entries
df=df.dropna(subset=['student_name','enrollment_date','progress_percentage'])
print(df)
average=np.mean(df['progress_percentage'])
print("Average overall completion:",average)
average_completion_by_course= df.groupby('course_name')['progress_percentage'].mean()
print("-------SUMMARY REPORT--------")
print("Average completion by course")
print(average_completion_by_course)
