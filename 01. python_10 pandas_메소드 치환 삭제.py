# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 2021

@author: khb16
"""

# replace 메서드_치환, 삭제

# replace 메서드
# 치환(찾은 문자열, 바꿀 문자열)

# 1. 기본 문자열 메서드
# - 기본 파이썬 제공
# - 문자열에서 호출 가능
# - 벡터 연산(각 원소별 반복 처리) 불가
# - 오직 문자열 치환만 가능(숫자치환, NA 치환 불가능)

'abcd'.replace('a','A') # 'Abcd' >> a를 A로 치환
'abcd'.replace('a','')  # 'bcd' >> 공백으로 치환
'abcd1'.replace(1,'') # 숫자를 찾아서 치환하는 거 안됨.
# TypeError: replace() argument 1 must be str, not int 
 ' bcd1'.replace('',1) # 숫자로 치환하는 거 안됨
# TypeError: replace() argument 2 must be str, not int

['abcd','abcde','aabb'].replace(',','')
# AttributeError: 'list' object has no attribute 'str'
# list 는 replace 호출 불가

# for 문 활용
outlist = []
for i in ['abcd','abcde','aabb']:
    outlist.append(i.replace('a','A'))
                             
print(outlist)                            
# ['Abcd', 'Abcde', 'AAbb']

# map함수
f1 = lambda x : x.replace('a','A')
list(map(f1,['abcd','abcde','aabb']))
# ['Abcd', 'Abcde', 'AAbb']

['abcd','abcde','aabb'].map(f1)
# AttributeError: 'list' object has no attribute 'map'
# list 객체는 map 함수 호출 불가

from pandas import Series, DataFrame
['abcd','abcde','aabb'].map(f1) # 호출 불가
Series(['abcd','abcde','aabb']).map(f1) # Series는 호출 가능(method chaining)
# 0     Abcd
# 1    Abcde
# 2     AAbb
# dtype: object

import numpy as np
Series(['abcd','abcde','aaaab',np.nan]).map(lambda x: x.replace(np.nan,""))
# TypeError: replace() argument 1 must be str, not float
# 문자열(str) 이어야 함

# 2. str.replace
# - pandas 제공(Series 객체만 호출 가능)
# - 백터화 내장된 문자열 메서드
# - 문자열 호출 가능
# - 벡터 연산(각 원소 별 반복 처리) 가능
# - 오직 문자열 치환만 가능(숫자 치환, NA 치환 불가)
# - 숫자로 구성된 Series 적용 불가

Series(['abcd','abcde','aaaab']).str.replace('a','A')
# 0     Abcd
# 1    Abcde
# 2    AAAAb
# dtype: object

['abcd','abcde','aaaab'].str.replace('a','A')
# AttributeError: 'list' object has no attribute 'str'
# 리스트는 호출 불가

DataFrame(['abcd','abcde','aaaab']).str.replace('a','A')
# AttributeError: 'DataFrame' object has no attribute 'str'
# 데이터 프레임도 불가

# pandas replace
# - pandas 제공
# - 값 치환 메서드(똑같은, 완전히 일치하는 값을 다른 값으로 대체, 삭제)
# - Series, DataFrame 호출 가능
# - 숫자, Nan 치환 가능
# - 동시에 여러 대상 수정 가능

df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
#        0      1
# 0  1,200  1,300
# 1  1,400  1,500

df1.replace(',','') # 변화 없음
#        0      1
# 0  1,200  1,300
# 1  1,400  1,500

df2 = DataFrame([['1,200',','],['1,400','1,500']])
df2
#        0      1
# 0  1,200      ,
# 1  1,400  1,500

df2.replace(",","")
#        0      1
# 0  1,200       
# 1  1,400  1,500

df3 = DataFrame([['1200','1300'],['1400','.']],columns =['a','b'])
df3
#       a     b
# 0  1200  1300
# 1  1400     .
df3.replace('.',np.nan) # '.' 와 완전히 일치하는 값은 Nan 치환
#       a     b
# 0  1200  1300
# 1  1400   NaN

df3.replace(['.','1400','?','!'],np.nan)
#         a       b
# 0  1200.0  1300.0
# 1     NaN     NaN

# [연습 문제]
# df1 에 천단위 구분기호 제거 후 모두 숫자 변경
df1

# scala 에서는 문자열이 아닌 숫자로 변경해야 함.
df1.applymap(lambda x: int(x.replace(",","")))
#       0     1
# 0  1200  1300
# 1  1400  1500

df1.applymap(lambda x: int(x.replace(",",""))).sum()
# 0    2600
# 1    2800
# dtype: int64

