# import pandas as pd
#
# df = pd.read_csv('/Users/huijeongkim/PycharmProjects/untitled2/ActiveTeTimeList.csv')
# print(df)

# print(df.head())

# df.info()

# first = df.loc[100:200]
# print(first)

# second = df[df['totalClassTime'] >= 500]
# third = df[df['currentClassDate'] >= '2019.7.21']

# df의 모든 'totalClassTime'을 더한 sum값 뽑기


# df2 = df["totalClassTime"]
# print(df2)
# sum2 = df2.sum(axis =0)
# print('totalClassTime은', sum2)

# sum1 = df.sum(axis = 0) # axis=0 모든 열 합계 구하기 vs axis=1 모든 행 합계구하기
# print('열 단위 합계:\n', sum1)

# 컬럼별 sum/max/min은?
# print(df['totalClassRime'.sum()]
# df['totalClassRime'.max()]
# df['totalClassRime'.min()]

# 새로 만든 데이터를 csv로 뽑아내기!
# df.to_csv('myNewData.cxv')

# """datetime 학습"""
#
# import datetime
#
# today = datetime.datetime.today()
# print(today)
# time2 = datetime.datetime(2019.8.1)
# print(time2)
#
# oneday = datetime.timedelta(days=1)
#
# print(today - oneday)
# print(today - 7*oneday)
# print(today - 5*oneday)
# print(today - 30*oneday)
#
# # 월이없다
#
# # python datetime to string 을 구글링, date
#
# df2 = df["totalClassTime"]
# print(df2)


# 1번

import pandas as pd

df1 = pd.read_csv('/Users/huijeongkim/PycharmProjects/untitled2/StuTeaMatching.csv')
df2 = pd.read_csv('/Users/huijeongkim/PycharmProjects/untitled2/StuInfo.csv')
df3 = pd.read_csv('/Users/huijeongkim/PycharmProjects/untitled2/TeaInfo.csv')

pd1 = pd.merge(df1,df2, on ='st_no', how="inner")
print(pd1.head())
pd2 = pd.merge(pd1,df3, on='te_no', how="inner")
print(pd2.head())

pd2.to_csv("FullMatchingInfo.csv", mode='w')

china = pd2[pd2['mj_name']=="중어중문학과"]
print(china)

china2 = china['수업과목']
print(china2)

pd2[pd2['st_gender']=='F' & pd2['te_gender']=='F'].shape[0]

