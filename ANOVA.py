import pandas as pd
import numpy as np

data = pd.read_csv("https://raw.githubusercontent.com/YoungjinBD/data/main/exam/5_3_2.csv")
print(data.head())

mean_A = data[data['campaign'] == 'A']['satisfaction_score'].mean()
std_A = data[data['campaign'] == 'A']['satisfaction_score'].std()
mean_B = data[data['campaign'] == 'B']['satisfaction_score'].mean()
std_B = data[data['campaign'] == 'B']['satisfaction_score'].std()
mean_C = data[data['campaign'] == 'C']['satisfaction_score'].mean()
std_C = data[data['campaign'] == 'C']['satisfaction_score'].std()

print(round(mean_A, 2))
print(round(std_A, 2))
print(round(mean_B, 2))
print(round(std_B, 2))
print(round(mean_C, 2))
print(round(std_C, 2))


from scipy.stats import f_oneway

f_statistic, p_value = f_oneway(
    data[data['campaign'] == 'A']['satisfaction_score'],
    data[data['campaign'] == 'B']['satisfaction_score'],
    data[data['campaign'] == 'C']['satisfaction_score']
)

print(f_statistic.round(3)
)

p_value = p_value.round(3)
if p_value < 0.05:
  result = "기각"
else:
  result = "채택"
print(result)