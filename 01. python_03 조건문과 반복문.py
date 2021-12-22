# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:55:01 2021

@author: khb16
"""
# 반복문
# 객체의 각 원소에 동일한 연산처리 진행할 경우 사용
# 1. for 문 : 정해진 횟수, 대상이 있을 경우 사용

# for 반복변수 in 반복할 대상(범위):
#     반복 실행할 문장


for i in range(1,11):
    print(i)
    
# 예제
# 다음의 리스트 선언하고 5보다 클 경우, 'A', 작거나 같을 경우 'B'

l1 = [1,3,5,15,25]

for i in l1:
    if i > 5:
        print('A')
    else:
        print('B')
        
# 위 리스트에서 각 원소에 10을 더해서 출력
l1 + 10 #불가

for i in l1:
    print(i+10)
    
#for문의 결과를 바로 변수로 저장하는 건 불가
l1 = for i in l1:
    print(i+10)
    
#정답
l2 = []
for i in l1:
    l2.append(i+10)
    
print(l2)

#[11,13,15,25,35]



# 2. while문 : 조건에 따른 반복을 실행하는l3 = [1,2,3]
l3.append(4)
l3 경우
while 조건:
    조건이 참일 때 반복 문장
    
# 예제
# while 문으로 1~10까지 출력 

i=1
while i <=10:
    print(i)
    i = i+1
    
# 문제
# 1~100까지 총 합

vsum = 0
for i in range(1,101):
    vsum = vsum + i
    
print(vsum)

i    vsum         일반화
1     1          vsum + 1
2     1+2        vsum + 2
3     1+2+3      vsum + 3
4     1+2+3+4    vsum + 4
5     1+2+3+4+5  vsum + 5
6     1+2+3+4+5  vsum + 6
     +6
7     1+2+3+4+5  vsum + 7     
     +6+7
8     1+2+3+4+5  vsum + 8     
     +6+7+8       
9     1+2+3+4+5  vsum + 9     
     +6+7+8+9  
10    1+2+3+4+5  vsum + 10     
     +6+7+8+9+10   
               -----> vsum + i
              
                
vvvv=sum(i for i in range(1,101))              
print(vvvv)

# 1~100까지 짝수 총합
even = 0
for i in range(1,101):
    if i%2 == 0:
        even = even + i
print(even)


# 반복제어문
# 1.continue : 특정 조건일 경우 반복문 스킵
# 2.break : 특정 조건일 경우 반복문 종료(정지조건)
# 3.exit : 특정 조건일 경우 프로그램 종료
# 4.pass : 문법적으로 오류가 발생시키지 않기 위해 자리를 채우는 역할

# 예제
# 1~10출력, 5제외

for i in range(1,11):
    if i == 5:
        continue
    print(i)

for i in range(1,11):
    if i == 5:
        break
    print(i)

# for i in range(1,11):
#     if i == 5:
#         exit(0) :프로그램 종료
#     print(i)

v1 = 1
if v1 > 10:
    pass
else:
    print('b')
    
# 문제
# 1부터 100까지 누적합이 최소 2000 이상이 되는 시점의 k 값과 총 합을 출력하세요.
vsum = 0
for i in range(1,101):
    vsum = vsum + i
    if vsum >= 2000:
        break
print(i, vsum)


















