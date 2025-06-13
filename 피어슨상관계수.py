import pandas as pd
import numpy as np

data = pd.read_csv("https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_3_1.csv")
print(data.head())

mean_a = data['study_hours'].mean()
std_a = data['study_hours'].std()
mean_b = data['exam_scores'].mean()
std_b = data['exam_scores'].std()


print(round(mean_a, 2))
print(round(std_a, 2))
print(round(mean_b, 2))
print(round(std_b, 2))

from scipy.stats import pearsonr
corr, p_value = pearsonr(data['study_hours'], data['exam_scores'])
print(corr.round(3))
p_value = p_value.round(3)
if p_value < 0.05:
  result = "기각"
else:
  result = "채택"
print(result)