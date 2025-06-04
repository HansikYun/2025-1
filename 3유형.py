import pandas as pd
import numpy as np

data=  pd.read_csv("https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_3_1.csv")

mean_a = data[data['department'] == 'A']['hours_worked'].mean()
std_a = data[data['department'] == 'A']['hours_worked'].std()
mean_b = data[data['department'] == 'B']['hours_worked'].mean()
std_b = data[data['department'] == 'B']['hours_worked'].std()

print("A 부서 근무시간 평균 :", round(mean_a, 2))
print("A 부서 근무시간 표준편차 :", round(std_a, 2))
print("B 부서 근무시간 평균 :", round(mean_b, 2))
print("B 부서 근무시간 표준편차 :", round(std_b, 2))

from scipy.stats import ttest_ind

t_statistic, p_value = ttest_ind(data[data['department'] == 'A']['hours_worked'],
                                 data[data['department'] == 'B']['hours_worked'] )

print("검정통계량 :", round(t_statistic, 2))

p_value = round(p_value, 2)
if p_value <0.05:
  result = "기각"
else :
  result = "채택"

print(result)