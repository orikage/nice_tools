import holidays
import datetime

# trainデータを読み込んでる前提
# dateカラムに日にちが入っている想定
# 日にちの形は20210717みたいな感じを想定

us_holidays=holidays.UnitedStates()

count_for=0 # ????????

for tmp in train['date']:
    datetime_data=datetime.datetime.strptime(str(tmp),'%Y%m%d')
    bool_holiday=datetime_data in us_holidays
    #print(bool_holiday)
    if bool_holiday==True:
        train.at[train.index[count_for], 'bool_holiday']=1
    if bool_holiday==False:
        train.at[train.index[count_for], 'bool_holiday']=0
    count_for+=1
