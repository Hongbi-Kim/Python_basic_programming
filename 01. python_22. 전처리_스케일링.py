# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 15:19:15 2021

@author: khb16
"""

## 22. scailing

# 변수 스케일링(표준화)

# 설명변수의 서로 다른 범위를 동일한 범주 내 비교하기 위한 작업 
# - 거리 기반 모델
#   ex) knn, clustering, PCA, SVM, NN 모델 등에 필요
# - 각 설명변수의 중요도를 정확하게 비교하기 위해 요구됨 
# - 이상치에 덜 민감하게 조정

# 스케일링의 종류 

# 1) Standard Scailing
# - 평균을 0, 표준편차 1 로 맞추는 작업

# 2) MinMax Scailing
# - 최소값 0, 최대값 1 로 맞추는 작업

# 3) Robust Scailing
# - 중앙값 0, IQR 1 로 맞추는 작업
# - 중앙값은 이상치의 영향을 안 받기 때문.

# scaling module 불러오기
from sklearn.preprocessing import StandardScaler as standard
from sklearn.preprocessing import MinMaxScaler as minmax

# iris data loading
from sklearn.datasets import load_iris

iris_x = load_iris()['data']
iris_y = load_iris()['target']

# 1) standard scailing (표준화) : (x-xbar) / sigma
# 직접 계산
(iris_x - iris_x.mean(axis=0)) / iris_x.std(axis=0)
# [ 6.86617933e-02, -1.31979479e-01,  7.62758269e-01, 7.90670654e-01]

df1 = (iris_x - iris_x.mean(axis=0)) / iris_x.std(axis=0)
df1.min() # -2.43394714190809
df1.max() # 3.0907752482994253

# 함수 사용
m_sc = standard()
m_sc.fit(iris_x) # fit : 데이터를 모델에 적합하게 해주는 함수.
m_sc.transform(iris_x) # transform : 변환
# [ 6.86617933e-02, -1.31979479e-01,  7.62758269e-01, 7.90670654e-01]

# 2) min max scailing ((x-x.min()) / (x.max()-x.min())
# 직접 계산

df2 = (iris_x - iris_x.min(0)) / (iris_x.max(0) - iris_x.min(0))
# [0.44444444, 0.41666667, 0.69491525, 0.70833333]
df2.max() # 1.0
df2.min() # 0.0

# 함수 사용
mm = minmax()
mm.fit(iris_x) # MinMaxScaler()
df3 = mm.transform(iris_x) 
# [0.44444444, 0.41666667, 0.69491525, 0.70833333]
df3.min() # 1.0
df3.max() # 0.0


# train/test 로 분리되어진 데이터를 표준화
from sklearn.model_selection import train_test_split

train_x, test_x, train_y, test_y = train_test_split(iris_x, iris_y)

# 1) train_x, test_x 동일한 기준으로 스케일링 (good)
mm_2 = minmax()
mm_2.fit(train_x)
train_mm = mm_2.transform(train_x)
# [0.22222222, 0.22727273, 0.35087719, 0.41666667]
test_mm = mm_2.transform(test_x)
# [0.19444444, 0.68181818, 0.10526316, 0.20833333]

train_mm.min(0) # array([0., 0., 0., 0.])
train_mm.max(0) # array([1., 1., 1., 1.])

test_mm.min(0) # array([0.02777778, 0.13636364, 0.05263158, 0.        ])
test_mm.max(0) # array([0.94444444, 1.09090909, 1.03508772, 0.95833333])


# 2) train_x, test_x 서로 다른 기준으로 스케일링 (bad)
mm_2 = minmax()
mm_3 = minmax()

mm_2.fit(train_x)
mm_3.fit(test_x)

train_mm_2 = mm_2.transform(train_x)
# [0.22222222, 0.22727273, 0.35087719, 0.41666667]
test_mm_2 = mm_3.transform(test_x)
# [0.18181818, 0.57142857, 0.05357143, 0.2173913 ]

train_mm_2.min() # 0.0
train_mm_2.max() # 1.0

test_mm_2.min() # 0.0
test_mm_2.max() # 1.0
