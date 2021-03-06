# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 13:41:32 2022

@author: khb16
"""

# 딕셔너리(dictionary) : 사전과 매우 유사
# 사전에는 단어와 단어의 설명이 저장되어 있다.
# 파이썬에서 키(key)와 값(value)의 쌍을 저장할 수 있는 객체

# 딕셔너리 생성방법 : {} "키:값" 같은 형태
dic1 = {1:"사과", 2:"토마토", 3:"오렌지"}
print(dic1)
# {1: '사과', 2: '토마토', 3: '오렌지'}

# 딕셔너리의 키값은 변경 불가능한 객체이어야 한다.
# 문자열이나 숫자를 권장
dic2 = {[1]:"사과", 2:"토마토", 3:"오렌지"}
# TypeError: unhashable type: 'list'

# 딕셔너리의 키값의 자료형은 혼합되어도 됨.(권장x)
dic3 = {1:"사과", "2":"토마토", (3,):"오렌지"}

# 공백 디셔너리
dic4 = {}
# set 객체도 역시 {}사용하기 떄문에 혼돈이 있을 수 있음.
# set을 생성할 때는 내장함수인 set()을 사용해야 한다.
set1 = set({1,2,3,4,5})
print(set1)
# {1, 2, 3, 4, 5}

# 딕셔너리 항목 추출
dic1 = {1:"사과", 2:"토마토", 3:"오렌지"}
# 첫 번째 방법은 []안에 키 값을 주면 값을 얻음.
print("dic1[1]키의 값은 : ", dic1[2])
# dic1[1]키의 값은 :  토마토

# 두 번째 방법은 get() 메서드 사용
print("dic1[1]키의 값은 : ", dic1.get(1))
dic1[1]키의 값은 :  사과

# 만약 키가 딕셔너리에 존재하지 않으면 KeyError가 발생
print("dic1[1]키의 값은 : ", dic1.get(4)) # 리턴값이 None
# dic1[1]키의 값은 :  None
print("dic1[1]키의 값은 : ", dic1[4]) # Error 발생
# KeyError: 4

# 키가 딕셔너리에 없으면 디폴트 값을 사용
a = dic1.get(4, "파인애플")
print(a)

# 키가 존재하는지 알아보는 방법
print(1 in dic1)
# True
print(1 not in dic1)
# False

# 딕셔너리 항목 추가하는 방법
# 딕셔너리는 변경 가능한 객체
# 값을 추가, 삭제해도 동일한 주소값을 갖는다.
dic1[4]  = "파인애플"
print(dic1)
# {1: '사과', 2: '토마토', 3: '오렌지', 4: '파인애플'}

print("요소추가 전 주소 : ", id(dic1))
print("요소추가 후 주소 : ", id(dic1))
# 요소추가 전 주소 :  2193741979776
# 요소추가 후 주소 :  2193741979776

# 삭제
# pop()
dic1 = {1: '사과', 2: '토마토', 3: '오렌지', 4: '파인애플'}
a = dic1.pop(2)
print(a)
print(dic1)
# 토마토
# {1: '사과', 3: '오렌지', 4: '파인애플'}

# del()
del dic1[1]
print(dic1)
# {3: '오렌지', 4: '파인애플'}

# 모든 항목 삭제 : clear()
dic1.clear()
dic1 # {}

