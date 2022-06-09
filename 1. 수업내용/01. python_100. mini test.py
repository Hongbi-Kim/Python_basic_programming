# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 16:48:26 2021

@author: khb16
"""

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# 1. [4,5,6] 을 리스트로 넘파이 배열로 만들어 a 변수에 담고 합을 구하시오. 
a = np.array([4,5,6])
a.sum()
# 15

# 2. DataFrame([['2,200','4,300'],['3,400','1,500']])을 df 변수에 담고, 
#    이의 천 단위 구분 기호를 제거한 후 모두 숫자로 변경하세요.

df = DataFrame([['2,200','4,300'],['3,400','1,400']])
df.applymap(lambda x: int(x.replace(",","")))
#       0     1
# 0  2200  4300
# 1  3400  1400

# 3. DataFrame(np.arange(1,17) 을 4행 4열의 행렬로 변환하여 df에 담고, 
#    컬럼별 합을 구하시오. 
df = DataFrame(np.arange(1,17).reshape(4,4))
df.sum(axis=1)
# 0    10
# 1    26
# 2    42
# 3    58
# dtype: int64

# 4. drwill@drwill.kr 이메일 주소에서 아이디를 추출하세요
#    (Series로 변환하여 s 변수에 담은 후 이를 처리하시오)

s = Series(['drwill@drwill.kr'])
s.map(lambda x : x[:x.find('@')])
# 0    drwill
# dtype: object

list(map(lambda x: x[:x.find('@')],s))
# ['drwill'] 

# 5. [1,3,5,15,25] 를 _list 의 변수에 담고 10보다 클 경우, 'pass', 
#    작거나 같은 경우 'fail'을 출력하시오 (반복문 사용하세요)
_list = [1,3,5,15,25]
for i in _list:
    if i > 10:
        print('pass')
    else:
        print('fail')
# fail
# fail
# fail
# pass
# pass

