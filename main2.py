import pandas as pd

df=pd.read_csv('/Users/huijeongkim/PycharmProjects/untitled2/ActiveTeTimeList.csv')

print(df)

# df.head(), df.info() 등으로 data정보 확인하기
first = df.head()
print(first)

second = df.info()
print(second) # object가 뭔지

# df.loc로 index가 100-200의 값들만 뽑아보기

third = df.loc[100:201]
print(third)

#df[특정조건]으로 totalClassTime이 500 이상인 값들만 뽑아보기

A = df[df['totalClassTime']>= 500]
print(A)

#df[특정조건]으로 2019.7.21 이후의 데이터만 뽑아보기

import datetime

time1 = datetime.datetime(2019,7,21)
print(time1)

df['currentClassDate'] = pd.to_datetime(df['currentClassDate'],format = '%Y.%m.%d')
B = df[df['currentClassDate'] >= time1]
print(B)

# df의 모든 'totalClassTime'을 더한 sum을 뽑기
C = df['totalClassTime'].sum()
print(C)

# 1단계 데이터프레임에서 totalClassTime 열만 뽑아보기

total = df['totalClassTime']
print(total)

# 1단계 df[특정조건]으로 '2019.7.21'이후의 데이터들만 뽑아보기

import datetime

time1 = datetime.datetime(2019,7,21)
print(time1)

df['currentClassDate'] = pd.to_datetime(df['currentClassDate'],format = '%Y.%m.%d')
B = df[df['currentClassDate'] >= time1]
print(B)


# 2단계 totalClassTime의 최대, 최소, 평균값을 구해본다

Max = df['totalClassTime'].max()
Min = df['totalClassTime'].min()
mean = df['totalClassTime'].mean()
print(Max)
print(Min)
print(mean)

# 2단계 currentClassDate가 '2019.7.21'이후의 totalClassTime의 sum을 구해본다

import datetime

time1 = datetime.datetime(2019,7,21)
print(time1)

df['currentClassDate'] = pd.to_datetime(df['currentClassDate'],format = '%Y.%m.%d')
B = df[df['currentClassDate'] >= time1]
print(B)

sum2 = B['totalClassTime'].sum()
print(sum2)

# 3단계 currnetClassDate를 기준으로 주별 totalClassTime의 sum을 구해본다


# 추가 문항 3문항 중 1개
#
# t= int(input())
#
# for i in range(t):
#     mins = input()
#     mins.split()



