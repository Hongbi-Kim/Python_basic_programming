# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 13:13:42 2021

@author: khb16
"""

# 14. drop, shift, rename

# 기타 메소드

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# 1. drop
# - 특정 행, 컬럼 제거
# - 이름 전달


emp = pd.read_csv("emp.csv")
emp
'''
   empno  ename  deptno   sal
0      1  smith      10  4000
1      2  allen      10  4500
2      3   ford      20  4300
3      4  grace      10  4200
4      5  scott      30  4100
5      6   king      20  4000
'''

# scott 퇴사
emp['ename'] == 'scott' # 조건문

# scott 관련된 record
emp.loc[emp['ename'] == 'scott']
#    empno  ename  deptno   sal
# 4      5  scott      30  4100

emp.loc[emp['ename'] == 'scott',:] 
emp.loc[~(emp['ename'] == 'scott'),:]
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 5      6   king      20  4000

emp.drop?

# emp.drop(
#     labels=None,
#     axis=0,
#     index=None,
#     columns=None,
#     level=None,
#     inplace=False,
#     errors='raise',
# )

emp.drop(4, axis = 0) # 행기준, 4번째 idx 제외

# 예제)
# emp 데이터셋에서 sal 컬럼 제외 (iloc)
emp
emp.iloc[:,0:3]
emp.iloc[:,:-1]

emp.loc[:,"empno":'deptno']
emp.drop(['ename','deptno'],axis=1)
emp.drop('sal',axis=1)

# shift
# - 행 또는 열을 이동
# - 전일자 대비 증감율

emp['sal']
# 0    4000
# 1    4500
# 2    4300
# 3    4200
# 4    4100
# 5    4000
# Name: sal, dtype: int64

emp['sal'].shift() # default : axis = 0 (행)
# 0       NaN
# 1    4000.0
# 2    4500.0
# 3    4300.0
# 4    4200.0
# 5    4100.0
# Name: sal, dtype: float64

# [예제 - 다음 데이터프레임에서 전일자 대비 증감율 출력]
s1 = Series([3000,3500,4200,2800,3600],
       index=['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])
s1
'''
2021/01/01    3000
2021/01/02    3500
2021/01/03    4200
2021/01/04    2800
2021/01/05    3600
dtype: int64
'''

# 1월 2일 증감율 >> (3500-3000)/3000
s1.shift()
'''
2021/01/01       NaN
2021/01/02    3000.0
2021/01/03    3500.0
2021/01/04    4200.0
2021/01/05    2800.0
dtype: float64
'''

(s1-s1.shift())/s1.shift() * 100
'''
2021/01/01          NaN
2021/01/02    16.666667
2021/01/03    20.000000
2021/01/04   -33.333333
2021/01/05    28.571429
dtype: float64
'''

# 3. rename
# - 행, 컬럼명 변경

emp
emp.columns = ['emptno','ename','deptno','salary']

emp.rename?
'''
emp.rename(
    mapper=None,
    index=None,
    columns=None,
    axis=None,
    copy=True,
    inplace=False,
    level=None,
    errors='ignore',
)
'''

emp.rename({'salary':'sal','deptno':'dept_no'},axis=1)
'''
   emptno  ename  dept_no   sal
0       1  smith       10  4000
1       2  allen       10  4500
2       3   ford       20  4300
3       4  grace       10  4200
4       5  scott       30  4100
5       6   king       20  4000
'''

# [예제] emp 데이터에서 ename을 index로 설정 후 scott을 SCOTT 변경
emp.set_index('ename').rename({'scott':'SCOTT'})
'''
       emptno  deptno  salary
ename                        
smith       1      10    4000
allen       2      10    4500
ford        3      20    4300
grace       4      10    4200
SCOTT       5      30    4100
king        6      20    4000
'''
