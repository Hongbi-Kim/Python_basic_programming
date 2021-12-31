# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 11:23:45 2021

@author: khb16
"""

# 17. 날짜표현
# 월별, 일별, 요일별 집계
# 현재 날짜 - 입사일자 = 근무한 일자

# 현재 날짜
import numpy as np
import pandas as pd
from datetime import datetime
from pandas import Series, DataFrame

datetime.now()
# datetime.datetime(2021, 12, 29, 11, 25, 37, 276311)

d1 = datetime.now()
type(d1)

d1.year 
d1.month 
d1.day   

# 2. 날짜 파싱
d2 = '2022/01/01'
d2.year
# 'str' object has no attribute 'year'

# 벡터 연산이 안됨
# datetime.strptime(date_string, format)

datetime.strptime(d2, '%Y/%m/%d')
# datetime.datetime(2022, 1, 1, 0, 0)

datetime.strptime('21/12/25', '%d/%m/%y') # 2025년 12월 21일 해석
# datetime.datetime(2025, 12, 21, 0, 0)

# Series 벡터 연산 안됨.
# 해결방안 : map
s1 = Series(['2022/01/01','2022/01/02','2022/01/03'])
datetime.strptime(s1,'%Y/%m/%d')
# strptime() argument 1 must be str, not Series

s1.map(lambda x: datetime.strptime(x, '%Y/%m/%d'))
# 0   2022-01-01
# 1   2022-01-02
# 2   2022-01-03
# dtype: datetime64[ns]

# 2) pd.to_datetime
# 벡터 연산가능
s1
# 0    2022/01/01
# 1    2022/01/02
# 2    2022/01/03
# dtype: object

pd.to_datetime(s1)
# 0   2022-01-01
# 1   2022-01-02
# 2   2022-01-03
# dtype: datetime64[ns]

pd.to_datetime(s1,format = '%Y/%m/%d') #???
pd.to_datetime?
# 3) 날짜 포맷 변경 datetime.strftime(string format time)
# 요일 추출(날짜에서 요일을 return 하도록 날짜 출력 형식 변경)
# (연/월/일) --> (월/일/연) 순서로 변경
# (주의) 날짜 포맷 변경 한 후 return 데이터 타입은 무조건 문자라는 사실!!!

d1 = datetime.now()
d1
datetime.strftime(d1,'%A') # '%A' : 요일
#'Wednesday'
datetime.strftime(d1,'%a')  # 요일 리턴(축약형)
# 'Wed'

datetime.strftime(d1,'%m-%d,%Y')
# '12-29,2021'

type(datetime.strftime(d1,'%m-%d,%Y'))
# str

datetime.strftime(d1,'%Y') # 연도 리턴(완전체)
# '2021'
datetime.strftime(d1,'%y') # 연도 리턴(축약형)
# '21

datetime.strftime(s1,'%Y')
# descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'Series' object

s3 = pd.DataFrame({'date':['01-05-21','01-06-21','01-07-21']})
s3.dtypes
# AttributeError: 'DataFrame' object has no attribute 'dtype'

s3
#        date
# 0  01-05-21
# 1  01-06-21
# 2  01-07-21

s2.map(lambda x: datetime.strfitime(x,'%Y'))

# 4) 날짜 연산 ***
d1           # 현재 날짜
d1 + 100     # 100일 후

# 오늘 날짜로부터 100일 뒤 날짜 리턴 불가(타입이 틀리다)
# TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'int'

# 1) offset
from pandas.tseries.offsets import Day, Hour, Second
d1 + Day(100)
# Timestamp('2022-04-08 11:43:05.791627')

# 2) timedelta (날짜와의 차이)
from datetime import timedelta
d1 + timedelta(100) # 오늘부터 100일 뒤
# datetime.datetime(2022, 4, 8, 11, 43, 5, 791627)

# 3) (실무용) DateOffset *** 
d1 + pd.DateOffset(months = 4)
# Timestamp('2022-04-29 11:43:05.791627')

# 4) 날짜 - 날짜
d1 #datetime.datetime(2021, 12, 29, 11, 43, 5, 791627)
d2 #'2022/01/01'
d1 - datetime.strptime(d2, '%Y/%m/%d')
# datetime.timedelta(days=-3, seconds=42185, microseconds=791627)

d3 = d1 - datetime.strptime(d2, '%Y/%m/%d')
d3.days # -3
d3.seconds # 42185

# 연습문제
# 요일별 통화건 수 총합
import os
os.chdir("C:/Users/khb16/Desktop/code/Python basic")
deli = pd.read_csv("delivery.csv",encoding='cp949')
deli.dtypes
'''
일자       int64
시간대      int64
업종      object
시도      object
시군구     object
읍면동     object
통화건수     int64
dtype: object
'''

deli.head()
'''
         일자  시간대           업종     시도  시군구   읍면동  통화건수
0  20180201    0  음식점-족발/보쌈전문  서울특별시  강남구   논현동     5
1  20180201    0  음식점-족발/보쌈전문  서울특별시  강남구   역삼동     5
2  20180201    0  음식점-족발/보쌈전문  서울특별시  강서구  내발산동     5
3  20180201    0  음식점-족발/보쌈전문  서울특별시  강서구   화곡동     5
4  20180201    0  음식점-족발/보쌈전문  서울특별시  동작구  신대방동     5
'''

deli.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 119189 entries, 0 to 119188
Data columns (total 7 columns):
 #   Column  Non-Null Count   Dtype 
---  ------  --------------   ----- 
 0   일자      119189 non-null  int64 
 1   시간대     119189 non-null  int64 
 2   업종      119189 non-null  object
 3   시도      119189 non-null  object
 4   시군구     119189 non-null  object
 5   읍면동     119189 non-null  object
 6   통화건수    119189 non-null  int64 
dtypes: int64(3), object(4)
memory usage: 6.4+ MB
'''

deli.describe()
'''
                 일자            시간대           통화건수
count  1.191890e+05  119189.000000  119189.000000
mean   2.018021e+07      15.576362       9.916486
std    8.234111e+00       5.321848      13.904536
min    2.018020e+07       0.000000       5.000000
25%    2.018021e+07      13.000000       5.000000
50%    2.018021e+07      17.000000       5.000000
75%    2.018022e+07      19.000000       7.000000
max    2.018023e+07      23.000000     229.000000
'''

deli.boxplot()

# 날짜 파싱
deli
pd.to_datetime(deli['일자'])
deli['일자'] = pd.to_datetime(deli['일자'],format='%Y%m%d')

# 요일 리턴
datetime.strftime(deli['일자'],'%A')
# TypeError: descriptor 'strftime' for 'datetime.date' objects doesn't apply to a 'Series' object

deli['요일'] = deli['일자'].map(lambda x:datetime.strftime(x,'%A'))
'''
0          Thursday
1          Thursday
2          Thursday
3          Thursday
4          Thursday
   
119184    Wednesday
119185    Wednesday
119186    Wednesday
119187    Wednesday
119188    Wednesday
Name: 일자, Length: 119189, dtype: object
'''

# 요일별로 그룹화 (통화건수)
total = deli.groupby(by='요일')['통화건수'].sum()
'''
요일
Friday       162037
Monday       142157
Saturday     196429
Sunday       196096
Thursday     150316
Tuesday      158544
Wednesday    176357
Name: 통화건수, dtype: int64
'''
total[['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']]
# 월화수목금토일 순으로 재배치 해야 함
# 아직까지 정렬로 배치 안됨, 색인으로 처리해야 함.

# 일자별 통화건수
deli.groupby('일자')['통화건수'].sum()
'''
일자
2018-02-01    39653
2018-02-02    46081
2018-02-03    54124
2018-02-04    50323
2018-02-05    35023
2018-02-06    38628
2018-02-07    39371
2018-02-08    40153
2018-02-09    49116
2018-02-10    54101
2018-02-11    50795
2018-02-12    36734
2018-02-13    43097
2018-02-14    45282
2018-02-15    28201
2018-02-16    16570
2018-02-17    34789
2018-02-18    43692
2018-02-19    34259
2018-02-20    38036
2018-02-21    39381
2018-02-22    42309
2018-02-23    50270
2018-02-24    53415
2018-02-25    51286
2018-02-26    36141
2018-02-27    38783
2018-02-28    52323
Name: 통화건수, dtype: int64
'''





