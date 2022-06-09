# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 12:03:47 2022

@author: khb16
"""

# 반복문
# x는 루프변수, in 다음에 오는 것은 시퀀스.
# 시퀀스에 올 수 있는 것은 리스트, 문자열이 존재.

for x in [0,1,2,3,4]:
    print("안녕하세요.")

# range(x)를 이용하면 훨씬 효율적, 가독성도 좋다.
# range() 함수는 리스트 타입으로 반환해준디ㅏ.
# range(x) : 0부터 시작하고 마지막 값(x-1)까지 정스 리스트 타입으로 반환   
for x in range(5):
    print("안녕하세요.")
# 안녕하세요.
# 안녕하세요.
# 안녕하세요.
# 안녕하세요.
# 안녕하세요.

print(type(range(5)))
# <class 'range'> 
# range 객체 타입

# 문자열 리스트를 시퀄스로 가질때
s = ["신은혁","김연아","김철수","홍길동","김남길"]
for name in s:
    print("반갑습니다. " + name + "님!")
# 반갑습니다. 신은혁님!
# 반갑습니다. 김연아님!
# 반갑습니다. 김철수님!
# 반갑습니다. 홍길동님!
# 반갑습니다. 김남길님!

# 줄바꿈을 하지 않게 하는 end 인자값을 확인
for x in [0,1,2,3,4]:
    print(x, end=' ')
# 0 1 2 3 4 

# range() 함수

# 1. range(x) 매개변수 1개짜리 함수를 이용
sum = 0
for x in range(10):
    sum = sum + x
print("0~9까지의 누계합 : ", sum)
# 0~9까지의 누계합 :  45

# 2. range(start, end) 매개변수 2개짜리 함수를 이용
# 누적을 하는데 stop 값은 포함하지 않는다.
for x in range(0,10):
    sum = sum + x
print("0~9까지의 누계합 : ", sum)

# 3. range([start], end, [step]) 매개변수 3개짜리 함수를 이용
# 누적을 시킬 때 step 만큼 건너 띄어 리스트를 생성
# 대괄호 [] 감싸져 있는 매개변수 값은 생략 가능
for x in range(0,10,2):
    sum = sum + x
print("0~9까지의 누계합 : ", sum)
# 0~9까지의 누계합 :  20

# 문자열 실습
# 문자열도 시퀀스의 대상에 포함됨.
s = "Shin Eun Hyeoc"
for ch in s:
    print(ch, end="")
# Shin Eun Hyeoc




