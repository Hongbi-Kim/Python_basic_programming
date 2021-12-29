# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 14:16:29 2021

@author: khb16
"""

# 시각화
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

import matplotlib.pyplot as plt

# 선그래프 : plot

plt.plot([1,2,3,4],
         [10,20,30,40],
         marker = '^',
         linestyle = '--',
         color='r')

s1 = Series([10,20,30,40])
s1.plot()

s1.plot(xticks=[0,1,2,3],   # 눈금 좌표
        ylim=[0,100],       # y 축 범위
        xlabel='x name',    # x 축 라벨
        ylabel='y name',    # y 축 라벨
        rot=90,             # rot (=rotation 회전) 90도
        title='name',       # title 그림 제목
        marker='^',         # marker
        linestyle='--',     # 선 스타일
        color='red')        # 컬러

plt.plot(s1)
plt.xticks(ticks=[0,1,2,3],labels=['a','b','c','d'], rotation = 180)
plt.xticks(ticks=[0,1,2,3],labels=['a','b','c','d'])
plt.ylim([0,100])
plt.ylabel('y name',loc='top',labelpad=30, fontdict=font1)

# fontdict
font1 = {'family' : 'Malgun Gothic',
         'weight' : 'bold',
         'size' : 15,
         'color' : 'red',
         'style' : 'italic'}

# global option 변경
plt.rc('font',family='Malgun Gothic')

# 데이터프레임의 선 그래프 출력
df1 = DataFrame({'apple':[10,20,30,40],'banana':[49,39,30,12],'mango':[10,32,43,40]})
#    apple  banana  mango
# 0     10      49     10
# 1     20      39     32
# 2     30      30     43
# 3     40      12     40

df1.index
# RangeIndex(start=0, stop=4, step=1)
df1.index=['a','b','c','d']
df1.index.name = '지점'
df1.columns.name = '과일명'
df1
# 과일명  apple  banana  mango
# 지점                       
# a       10      49     10
# b       20      39     32
# c       30      30     43
# d       40      12     40

df1.plot() # 컬럼별 서로 다른 선 그래프 출력 가능
plt.legend(fontsize=9, loc='best',title='과일이름')










