#회귀 모델
import pandas as pd
import numpy as np
train = pd.read_csv("https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_2_train.csv")
test = pd.read_csv("https://raw.githubusercontent.com/YoungjinBD/data/main/exam/8_2_test.csv")

#print(train.info())
#print(test.info())

test_id = test['ID']

train_x = train.drop(["count"], axis = 1)
train_y = train["count"]
test_x = test.drop(["count"], axis = 1)
test_y = test["count"]

from sklearn.model_selection import train_test_split
train_x, valid_x, train_y, valid_y = train_test_split(
    train_x, train_y, test_size = 0.3, random_state = 1
)

cat_columns = train_x.select_dtypes("object").columns.to_list()

from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(sparse_output = False, handle_unknown = 'ignore')
train_x_preprocessed = onehotencoder.fit_transform(train_x[cat_columns])
valid_x_preprocessed = onehotencoder.transform(valid_x[cat_columns])
test_x_preprocessed = onehotencoder.transform(test_x[cat_columns])

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(random_state = 1)
rf.fit(train_x_preprocessed, train_y)

from sklearn.metrics import mean_absolute_error
pred_val = rf.predict(valid_x_preprocessed)
print("valid mae", mean_absolute_error(valid_y, pred_val))

test_pred = rf.predict(test_x_preprocessed)
test_pred = pd.DataFrame(test_pred, columns = ['pred'])

result = pd.concat([test_id, test_pred], axis = 1)
print(result.head())

result.to_csv('-', index = False)