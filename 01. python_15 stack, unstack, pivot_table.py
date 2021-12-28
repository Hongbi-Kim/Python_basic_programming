# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:31:13 2021

@author: khb16
"""

# 15. stack, unstack, pivot_table

# 자료구조(데이터타입) 형태
# - long data(tidy data)
# - 각 속성을 컬럼으로 표현

# 지점
# A
# B
# C

# - wide data(cross table : 교차표)
# - 하나의 속성을 갖는 데이터가 각 종류마다 서로 다른 컬럼으로 분리되어 나열함.

#           A      B       C
# 판매량

# stack / unstack
# 1. stack
# wide ->> long

# 2. unstack
# long ->> wide

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

kimchi = pd.read_csv("kimchi_test.csv", encoding="cp949")

# kimchi 데이터를 연도별, 제품별 수량의 총합
df1 = kimchi.groupby(['판매년도','제품'])['수량'].sum()
'''
판매년도  제품  
2013  무김치     420750
      열무김치    419045
      총각김치    483735
2014  무김치     447768
      열무김치    489359
      총각김치    551613
2015  무김치     540809
      열무김치    601661
      총각김치    742150
2016  무김치     733437
      열무김치    637934
      총각김치    634155
Name: 수량, dtype: int64
'''


# 멀티 인덱스
# 인덱스나 컬럼이 여러 레벨로 표현
# 상위레벨 : 0, 하위레벨로 갈수록 숫자 증가

df2 = df1.unstack() # long ->> wide
'''
제품       무김치    열무김치    총각김치
판매년도                        
2013  420750  419045  483735
2014  447768  489359  551613
2015  540809  601661  742150
2016  733437  637934  634155
'''

df2.stack() # wide ->> long

df1.unstack(level=0) # 상위레벨 (2013)
'''
판매년도    2013    2014    2015    2016
제품                                  
무김치   420750  447768  540809  733437
열무김치  419045  489359  601661  637934
총각김치  483735  551613  742150  634155
'''

df1.unstack(level=1) 

# pivot_table
# 교차표 작성

# kimchi.pivot_table(index = '판매월',     : index 방향에 배치할 컬럼명
#                     columns = '판매처',   : column 방향에 배치할 컬럼명
#                     values = '수량',      : 교차표에 작성할 값을 갖는 컬럼명
#                     aggfunc = 'sum'       : 그룹 함수
#                     )


# 에제 - kimchi 데이터를 이용해서, 연도별, 제품별 판매금액의 총 합을 교차표로 작성하세요.
kimchi.pivot_table(index='판매년도', columns='제품',values='판매금액',aggfunc='sum')
'''
제품           무김치        열무김치        총각김치
판매년도                                    
2013  3809133886  3416217894  4186789117
2014  4111403907  4392490590  5250364301
2015  5212738410  5859079408  7485159996
2016  6903506142  6627888927  6378374872
'''

