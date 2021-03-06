# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 15:18:48 2021

@author: khb16
"""

# 판다스_문자열 메소드
# 기본 메소드 : 벡터 연산 불가능(매 원소마다 반복 불가)

'abc'.upper()
'a/b/c'.split('/')

l1 = ['abc','def']
l2 = ['a/b/c','d/e/f']

l1.upper() #안 됨. 
l2.upper() #안 됨.

map(lambda x: x.upper(),l1)
list(map(lambda x: x.upper(),l1))
list(map(lambda x: x.split('/'),l2))

# pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame 적용 가능

from pandas import Series, DataFrame

# 1) split
Series(l1)
# 0    abc
# 1    def
# dtype: object

s1 = Series(l1)
s2 = Series(l2)

s2
# 0    a/b/c
# 1    d/e/f
# dtype: object

s2.split('/')
# 'Series' object has no attribute 'split'

s2.str.split('/') # 가능
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

#대소치환
s1.str.upper() #대문자 치환
s1.str.lower() #소문자 치환
s1.str.title()
# 0    Abc
# 1    Def
# dtype: object

# replace(치환)
s1.str.replace('a','A') #문자열 치환
s1.str.replace('a','') #문자열 삭제

# [예제] 천단위 구분기호 처리
s3 = Series(['1,200','3,000','4,000'])
s3.str.replace(',','').astype(int).sum()

# 패턴확인 : startswith, endswith, contains
s1
s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool
s1[s1.str.startswith('a')] # s1 각 원소에서 'a'로 시작하는 원소 추출
s1[s1.str.endswith('c')] # s1 각 원소에서 'c'로 끝나는 원소 추출
# 0    abc
# dtype: object
s1[s1.str.contains('e')] # s1 각 원소에서 'e'를 포함하는 원소 추출

# 문자열 크기 len()
s1.str.len()
# count 포함되어 있는 개수
Series(['aabca','abcdsa']).str.count('a')

# 문자열 제거(제거함수 : 공백, 문자)
Series(['     cd    ','    df   ']).str.strip(' ')
Series(['     cd    ','    df   ']).str.strip(' ').str.len()

s1
s1.str.strip('a') # 문자열 제거
Series(['aaabaaca','abcda']).str.strip('a') # 문자열 제거(중간값 삭제 불가)
# 0    baac
# 1     bcd
# dtype: object

Series(['aaabaaca','abcda']).str.replace('a','') # 문자열 제거(중간값 삭제 가능)
# 0     bc
# 1    bcd
# dtype: object

# find : 위치값 리턴
s3 = Series(['abc@abc.com','abcvdf@abc.com'])
s3.str.find('@')

# 문자열 색인(추출)
'abcdef'[0:3] # 문자열 색인
s3[0:1]  #Series 에서 1번째 원소 추출
# 0    abc@abc.com
# dtype: object

s3
s3.str[0:3] #Series에서 각 원소마다 1~3번째까지의 문자열 추출
# 0    abc
# 1    abc
# dtype: object

# [예제 - 이메일 아이디 추출]
s3 = Series(['abc@abc.com','abcvdf@abc.com'])
s3.map(lambda x:x[:x.find('@')])

id = s3.str.find('@')
id
list(map(lambda x, y: x[0:y], s3, id))
#['abc', 'abcvdf']

# 문자열 삽입 pad
s1.str.pad(5,         # 총자리수
           'left',    # 삽입할 방향
           '!')       # 삽입할 글자

s1
s1.str.pad(5,'left','!')
# 0    !!abc
# 1    !!def
# dtype: object

s1.str.pad(5,'right','^')
# 0    abc^^
# 1    def^^
# dtype: object

# 문자열 결합 cat
'a' + 'b' # 'ab'
'a'*3     # 'aaa'

s4 = Series(['abc','def','123'])
s4.str.cat()     # 'abcdef123' >> Series 내 서로 다른 원소 결합
s4.str.cat(sep = '/') # 'abc/def/123' >> Series 내 서로 다른 원소를 구분기호와 함께 결합

s5 = Series([['a','b','c'],['d','e','f']])
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object

s5.str.join(sep='') # >> Series 내 각 원소 내부의 문자열 결합
# 0    abc
# 1    def
# dtype: object

s5.str.join(sep=',')
# 0    a,b,c
# 1    d,e,f
# dtype: object





























