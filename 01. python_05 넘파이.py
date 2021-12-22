# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 16:23:29 2021

@author: khb16
"""

# 자료구조
# 1. 리스트(기본구조)
# 2. 튜플(상수, 불변)
# 3. 딕셔너리(key:value) <<- json {1:'양진욱',2:'백혜림',3:'박윤수}
# 4. 세트(set) : 집합
# 5. 배열(numpy)
# 6. 판다스 구조(Series, DataFrame)

# 넘파이(numpy)
# 배열(array) 생성, 연산

# 배열(array) : 하나의 데이터 타입만 허용(int, float, ), 다차원 자료구조

import numpy as np
np.array([1,2,3])
# array([1, 2, 3])


np.array([[1,2,3],[4,5,6],[7,8,9]])
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# array([[[ 1,  2,  3],
#         [ 4,  5,  6]],

#        [[ 7,  8,  9],
#         [10, 11, 12]]])
# 3차원 배열

np.arange(1,26)
# array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
#        18, 19, 20, 21, 22, 23, 24, 25])

np.arange(1,26).reshape(5,5)
# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

a1 = np.arange(1,26)
type(a1)
# numpy.ndarray

# 색인
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

# array[행 선택, 열 선택]
a2[1,:]
# array([4, 5, 6])

a2[:,1]
# array([2, 5, 8])

# 슬라이스 색인(두 번째 열 선택 : 차원 축소 발생 안함)
a2[:,1:2]
# array([[2],
#        [5],
#        [8]])

# a2에서 1,3행 선택
a2[0:3:2,:] 
# array([[1, 2, 3],
#        [7, 8, 9]])

a2[[0,2],:]

# a2에서 1,3 열 선택
a2[:,[0,2]]

a2[1,1]
a2[[1,2],[1,2]] #array([5, 9])
# >>> a2[1,1], a2[2,2] 포인트 인덱싱
# 2개의 포인트(점) 출력
# 색인함수 (ix_()) 사용하여 해결

a2[np.ix_([1,2],[1,2])]
# array([[5, 6],
#        [8, 9]])

# 조건 색인
a2
a2 > 5
# array([[False, False, False],
#        [False, False,  True],
#        [ True,  True,  True]])

a2[a2>5]
# array([6, 7, 8, 9]) True만 출력

a2[:,0] > 5 #첫 번째 컬럼 가져와서 5이상인 행만 선택
a2[a2[:,0]>5]
# array([[7, 8, 9]])
# 조건의 결과를 행방향에 색인 값으로 전달

# 3.메서드 
dir(a2)

a2.dtype   # numpy 구성 데이터 타입 
a2.shape   # numpy 모양(shape)
# (3, 3)
a2.shape[0]  #numpy 행의 수 
a2.shape[1]  #numpy 열(컬럼) 수 

a2.reshape(1,9) # array 모양 변경 
a2.ndim         # array 차원 

# 4. 연산 
[1,2,3] + [4,5,6]      # list 는 서로 원소끼리 연산 불가 (확장으로 해석됨)
# [1, 2, 3, 4, 5, 6]

np.array([1,2,3])+np.array([4,5,6])
# array([5, 7, 9])
np.array([1,2,3])+np.array([4,5,6,7])
# 서로 사이즈가 같은 배열끼리 연산 가능 

# 5. 형(데이터 타입) 변환 메서드 

a2.astype('float')
# array([[1., 2., 3.],
#        [4., 5., 6.],
#        [7., 8., 9.]])
a2.astype('int')
a2.astype('str')
# array([['1', '2', '3'],
#        ['4', '5', '6'],
#        ['7', '8', '9']], dtype='<U11')

# 6. np.where 함수 
# if문의 축약형
# np.where(조건, 참인 값 반환, 거짓인 값 반환)

# sql 문 기본 형태 : select * from db where   

np.where(a2>5,'A','B')

# 7. 산술 연산 메서드 
a2
a2.sum()     # 전체 합
a2.mean()    # 전체 평균
a2.var()     # 전체 분산
a2.std()     # 전체 표준편차(평균에서 떨어진 정도)
a2.min()     # 전체 최소값
a2.max()     # 전체 최대값

a2 > 5

(a2 > 5).sum() # a2 에서 5보다 큰 값의 수  
(a2 > 5).any() # True  a2에서 5보다 큰 값이 하나라도 있을 경우 참 
(a2 > 5).all() # False a2에서 모두 5보다 클 경우만 참 

a2
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])
a2.sum(axis=0)       # 행 기준, 행 별 총합 (서로 다른 행끼리, 세로방향 연산)
#array([12, 15, 18]) 

a2.sum(axis=1)       # 열 기준, 열 별 총합(서로 다른 열끼리, 가로 방향 연산)
#array([ 6, 15, 24])

# [축 번호]
# 2차원 : 행(0) 열(1)
# 3차원 : 층(0) 행(1) 열(2)

# 8. 전치 메서드 
# 1) T : 행과 열을 전치 
np.arange(1,9)
#  array([1, 2, 3, 4, 5, 6, 7, 8])
a1 = np.arange(1,9).reshape(4,2)
a1
# array([[1, 2],
#        [3, 4],
#        [5, 6],
#        [7, 8]])
a1.T
# array([[1, 3, 5, 7],
#        [2, 4, 6, 8]])

# 2) swapaxes: 두 축을 전달 받아서 두 축을 서로 전치, 전달 순서는 중요하지 않아요
a1.swapaxes(0,1)
a1.swapaxes(1,0)

# 3) transpose 
# 원본의 차원에 맞는 축번호를 인수에 차례대로 전달. 그리고 그대로 전치 전달되는 순서 중요
a1

a1.transpose(0,1) # 원본 그래도 출력 
a1.transpose(1,0) # 행과 열 전치 

# 판다스
import pandas as pd


# 외부 파일 입출력
# 1) 파일 불러오기
# np.loadtxt(fname,           # 파일명
#              dtype,         # 데이터타입
#              delimiter,     # 필드 구분 기호
#              skiprows,      # skip 할 행 수
#              usecols,       # 선택할 컬럼 값(위치)
#              encoding)      # 인코딩 옵션

import numpy as np
np.loadtxt('./Desktop/code/file1.txt', delimiter=',',dtype='str')

# 2) 파일 내려쓰기
# np.savetxt(fname,        # 파일명
#            X,            # 객체명
#            delimiter,    # 구분자
#            fmt,          # 출력형식(format)
#            header,       # 헤더 출력 여부(file 첫 문자열)
#            encoding)     # 인코딩 옵션

import os
print(os.getcwd())

# np.savetxt?
x = np.arange(0.0,5.0,1.0)
np.savetxt('./Desktop/code/file2.txt',x,delimiter=',',fmt='%s')
#'%s' : 문자타입(string)

# [참고 : fmt 전달/변경 방식]
# %s : 문자열
# %f : 실수(float)
# %d : 정수
'%s' % 123 #'123'
'%f' % 123 #'123.000000'
'%.2f' % 123 #'123.00' >> 소수점 2째자리까지
'%d' % 123  #'123'
'%7d' % 123 #'    123'































