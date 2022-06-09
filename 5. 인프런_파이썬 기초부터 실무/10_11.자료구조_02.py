# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 19:44:37 2022

@author: khb16
"""

# 문제1
# 딕셔너리의 항목들을 순회하는 방법
scores = {'국어' : 80, "수학":95, "영어":80}

# 키값만 출력
for subject in scores:
    print(subject, end=" ")
# 국어 수학 영어

print(scores.keys())
# dict_keys(['국어', '수학', '영어'])

for subject in scores.keys():
    print(subject, end=" ")
# 국어 수학 영어

print(scores.values())
# dict_values([80, 95, 80])











