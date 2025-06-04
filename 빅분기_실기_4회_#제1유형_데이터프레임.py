#제1유형
#필터링 및 결측치 삭제
import pandas as pd
import numpy as np

dat = pd.read_csv("https://raw.githubusercontent.com/YoungjinBD/data/main/exam/4_1_1.csv")

#print(dat.isna().sum())
#결측치 삭제
dat.dropna(inplace = True)

#print(dat.isna().sum())

sub_dat = dat.loc[:int(len(dat) * 0.7), :]
result = sub_dat.loc[:, 'PTRATIO'].quantile(0.25)
print(np.round(result, 2))