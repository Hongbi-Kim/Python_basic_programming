# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 20:44:15 2021

@author: khb16
"""

#파이썬 기본 구조
# 1. 리스트(list) [ ] cf. R : c()
# - 기본 자료 구조(여러 상수를 동시 전달)
# - 1차원
# - 서로 다른 데이터 타입 가입

# 1) 리스트 생성
# 리스트명 = [요소, 요소2, 요소3, ...]
l1 = [1,2,3,4]
l1
type(l1) #list
l2 = [1,2,3,'4'] 
type(l2) #list
a = [1,2,['Life','is']]

t1 = (1,2,3,4) # tuple : 상수(변하지 않는 값 -> 변경이 불가능한 값)
type(t1)
t2 = 1,2,3,4

# 2) 색인(indexing)
l1
l1[0]
l1[1] # reverse indexing
l1[-1]
a[-1][0] #'Life'

#슬라이싱
l1[0:1] # n:m --> n부터 m-1까지
l1[0:2]

#여러 숫자 전달 불가
l2
l2[0,2] 
l2[[0:2]]

# 3) 수정
l1[0] = 10
l1

# 4) 연산
l1 + 1 # 리스트와 정수(int) 연산 불가
l1 > 1
# TypeError: can only concatenate list (not "int") to list
# TypeError: '>' not supported between instances of 'list' and 'int'

# 리스트 확장
[1,2,3] + [10,20,30]
# [1,2,3,10,20,30]

# 원소 추가
l1 + [5]
# [10,2,3,4,5]

l1.append(6)
l1
# [10,2,3,4,6]

# 문자열 더하고 곱하기
'a' + 'b'
'a'*3

# 5) 삭제
del(l1[0]) #첫번째 원소 삭제
l1
del(l1) # 객체 삭제
l1

# 리스트 내 모든 원소 삭제

l2 = []
l2


# 2. 튜플(상수) 
# 리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
# 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
t1 = (1,2,'a','b')
t1[0] # 인덱싱
t1[1:] # 슬라이싱
t2 = (3,4)
t1+t2 
# (1, 2, 'a', 'b', 3, 4)

t2*3
# (3, 4, 3, 4, 3, 4)
len(t1)

t1
t1[0] = 10
# TypeError: 'tuple' object does not support item assignment


# 3. 딕셔너리 자료형
# - 순서가 없다. 인덱스x
dic = {'name':'pey','phone':'0119993323','birth':1118}
a = {1:'hi'} # Key로 정수 값 1, Value로 문자열 'hi'
a = {'a':[1,2,3]} # Value에 리스트 가능

# 딕셔너리 쌍 추가하기
a = {1:'a'}
a[2]='b'
a
# {1: 'a', 2: 'b'}

a['name'] = 'pey'
a
# {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1,2,3]
a
# {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# 삭제
del a[1]
a
# {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

# Key 사용해 Value 얻기
grade = {'pey':10,'julliet':99}
grade['pey'] # 10
grade['julliet'] # 99

# 중복 Key는 무시
a = {1:'a', 1:'b'}
a
# {1:'b'}

# 딕셔너리 관련 함수
# Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.keys()
# dict_keys(['name', 'phone', 'birth'])

a.values()
# dict_values(['pey', '0119993323', '1118'])

a.items()
# dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

a.clear()
a
#{}

# Key로 Value 얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'} 
a.get('name') #'pey'
a.get('phone') #'0119993323'

print(a.get('nokey')) #None
a.get('foo', 'bar') #get(x,'디폴트값')

'name' in a #True
'email' in a #False

# 4. 집합 자료형
# - 중복 허용 x
# - 순서가 없다(Unordered). - 인덱싱 x
s1 = set([1,2,3])
s1 #{1, 2, 3}

s2 = set("Hello")
s2 #{'H', 'e', 'l', 'o'}

l1 = list(s1)
l1 #[1, 2, 3]
l1[0] #1
t1 = tuple(s1)
t1 #(1,2,3)
t1[0] #1

# 교집합, 합집합, 차집합
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

s1 & s2 #{4,5,6}
s1.intersection(s2) #{4,5,6}

s1 | s2 #{1, 2, 3, 4, 5, 6, 7, 8, 9}
s1.union(s2)

s1 - s2 #{1, 2, 3}
s2 - s1 #{7, 8, 9}
s1.difference(s2)
s2.difference(s1)

#값 1개 추가(add)
s1 = set([1,2,3])
s1.add(4)
s1 #{1,2,3,4}

#값 여러 개 추가(update)
s1 = set([1,2,3])
s1.update([4,5,6])
s1
#{1, 2, 3, 4, 5, 6}

#특정 값 제거(remove)
s1 = set([1,2,3])
s1.remove(2)
s1
#{1, 3}

# 5. 불 자료형
# 1 참
# 0 거짓

a = True
b = False

type(a)
#bool

1 == 1

bool('python') #True
bool('') #False
bool([1,2,3]) #True
bool([]) #False
bool(0) #False
bool(3) #True

# 6. 자료형의 값을 저장하는 공간, 변수
a = [1,2,3]
b = a
a is b #True
a[1] = 4
a
#[1,4,3]
b
#[1,4,3] 같이 변경

# a와 다른 주소 가르키게 만들기
# 1) [:] 이용
a = [1,2,3]
b = a[:]
a[1] = 4
a #[1,4,3]
b #[1,2,3]

# 2) copy 모듈 이용
from copy import copy
a = [1,2,3]
b = copy(a)
b is a #False

b = a.copy()

# 변수 만들기
a , b = ('python','life')
(a, b) = 'python','life'
[a,b] = ['python','life']
a = b = 'python'

# 연습문제
# 1. 평균 구하기
import numpy as np
a = [80,75,55]
np.mean(a)

# 답2
a = 80
b = 75
c = 55
(a+b+c)/3
#70.0

# 2. 홀짝 구하기
x = 13
if x%2==0:
    print("짝수")
else:
    print("홀수")
    
# 3. 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력.    
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd) #881120
print(num) #1068234

# 4. 인덱싱
pin = "881120-1068234"
pin[7]

# 5.replace
a = "a:b:c:d"
a.replace(":", "#")

# 6. 내림차순 - 내장 함수
a = [1,3,5,4,2]
a.sort(reverse=True)
a

# 7. 리스트를 문자열로 출력
a = ['Life','is','too','short']
result = " ".join(a)
print(result)
# Life is too short

# 8.튜플에 값 추가
a = (1,2,3)
b = (4,)
a + b

# 9. 딕셔너리
a = dict()
a
a['name'] = 'python'
a[('a',)] = 'python'
a[[1]] = 'python' #unhashable type: 'list'
a[250] = 'python'

# 10. 딕셔너리 a에서 'B'에 해당되는 값 추출
a = {'A':90,'B':80,'C':70}
a.pop('B')
a
#{'A': 90, 'C': 70}


# 11. a리스트에서 중복 숫자 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
set(a) #{1, 2, 3, 4, 5}
list(set(a)) #[1, 2, 3, 4, 5]

# 이유 설명
a = b = [1,2,3]
a[1] = 4
print(b)
#a와 b 변수는 모두 동일한 리스트 객체 가르킴