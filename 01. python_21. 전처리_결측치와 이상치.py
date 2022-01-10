# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:29:58 2021

@author: khb16
"""

# 21. 결측치와 이상치

# ------------------------------------------------------------
# 빅데이터 분석기사
# part1 : 단답형(10문제 * 3 = 30점 만점)
# part2 : 전처리(결측치 처리, 이상치 처리, 변수 변환, 치환..., 연산, 3문제 * 10 = 30점 만점)
# part3 : 분석과정(변수선택, 변수변환, ..., 모델비교, 튜닝, 평가 => 40점 만점)

# ------------------------------------------------------------

# 1. 결측치 처리
# 결측치 : 잘못 들어온 값, 누락 값(NA로 표현)
# 삭제 또는 대치

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

import os
os.chdir("C:/Users/khb16/Desktop/code/Python basic")

df1 = pd.read_csv('file1.txt')
#      a   b   c   d
# 0    1   2   3   4
# 1    5   6   7   8
# 2    9  10  11  12
# 3    .  13  14  15
# 4   16  17  18  19
# 5  NaN  20  21  22

pd.read_csv('file1.txt',
            sep=',',         # 필드 구분자
            header=None,     # 파일의 첫 줄을 컬럼으로 읽을지 여부
                             # (기본값은 첫줄을 컬럼으로 만들기 때문에 
                             # 첫줄을 컬럼으로 표현하지 않으려면 None 사용)
            skiprows=[0,3])  # 스킵할 행 번호 => 첫 번째, 네 번째 행 로딩 생략

# [ 문제 ]
# df1의 a컬럼의 결측치를 a컬럼의 최소값으로 대치 후 전체 평균 계산

df1['a'].min()
# TypeError: '<=' not supported between instances of 'str' and 'float'
# 실패 -> 문자 타입(str)

df1['a'].astype('float')
# ValueError: could not convert string to float: '.'


# . 확인 및 NaN으로 변경
df1['a'][df1['a']=='.'] # . 발견
# 3    .
# Name: a, dtype: object

df1['a'][df1['a']=='.'] = np.nan

df1['a'] = df1['a'].astype('float')
vmin = df1['a'].min() # 1.0
# nan를 최소값으로 대체

df1['a'][df1['a'].isnull()] # null 값 확인
# 3   NaN
# 5   NaN
# Name: a, dtype: float64

# nan값을 최소값으로 대체
vmin = df1['a'][df1['a'].isnull()]
'''
<ipython-input-122-5c155e83677f>:1: SettingWithCopyWarning: 
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
'''

vmin = df1['a'][df1['a'].isnull()].copy()

# 평균값으로 출력
df1['a'].mean() 
# 5.5

# ------------------------------------------------------------

# 이상치 (outliers)
# - 일반적인 범위를 벗어난 데이터
# - 삭제 또는 대치 처리
# - 다양한 이상치 탐색기법이 존재. But~
# - 데이터마다 이상치에 대한 구간이 정의되어 있는 경우가 다반사...
# - Box plot으로 확인하기 권장



# [문제]
# df1의 d 컬럼을 보세요. d 컬럼의 경우 16이상인 경우를 이상치로 판단
# 이상치를 제외한 나머지에 대해 최대값으로 이상치를 대치한 후, 평균을 계산
df1['d']
# 0     4
# 1     8
# 2    12
# 3    15
# 4    19
# 5    22
# Name: d, dtype: int64

df1['d'][df1['d'] >= 16]
# 4    19
# 5    22
# Name: d, dtype: int64

vmax = df1['d'][df1['d'] < 16].max() # 15
df1['d'][~(df1['d'] >= 16)].max()

# 이상치를 대치값으로 대치

df1['d'][df1['d'] >= 16] = vmax
df1['d']
# 0     4
# 1     8
# 2    12
# 3    15
# 4    15
# 5    15
# Name: d, dtype: int64

# 평균
df1['d'].mean() # 11.5
