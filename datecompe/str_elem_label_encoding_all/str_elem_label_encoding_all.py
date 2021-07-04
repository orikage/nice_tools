import pandas as pd
from sklearn.preprocessing import LabelEncoder


# 読み込み部

df_train=pd.read_csv('./date/train.csv')
df_train["TrainFlag"]=True
df_test=pd.read_csv('./date/test.csv')
df_test["TrainFlage"]=False
df_all=df_train.append(df_test)

# str識別部

mem_string=[]
for i in range(len(df_all.columns)):
    if type(df_all.iat[1,i])==str:
        mem_string.append(df_all.columns[i])

# label encode 変換部
for i in range(len(mem_string)):
    le=LabelEncoder()
    encoded=le.fit_transform(df_all[mem_string[i]].values)
    decoded=le.inverse_transform(encoded)
    df_all[f'{mem_string[i]}_encoded']=encoded
    df_all=df_all.drop([mem_string[i]],axis=1)
