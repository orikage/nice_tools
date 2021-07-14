import itertools
import pandas as pd


# dateの読み込み
df_train=pd.read_csv('./date/train.csv')
df_train["TrainFlag"]=True
df_test=pd.read_csv('./date/test.csv')
df_test["TrainFlage"]=False
df_all=df_train.append(df_test)

# 前処理
'''

df_all.drop("columns名",axis=1,inplace=True)

labelencodingはnice_tools/datecompe/str_elem_label_encoding_allに置いてある

'''

df_base=df_all.copy()
for pair in itertools.combinations(df_base.columns,2):
    new_col="*".join(pair)
    df_base[new_col]=df_base[pair[0]]*df_base[pair[1]]
