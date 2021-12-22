# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# 단축키
# f9 라인단위 실행
# ctrl+1 : 선택 영역 주석처리

# 변수 생성
# 변수 : 값을 저장하기 위한 객체(object)
# 변수 명명 규칙
# - 대소 구분, 숫자 시작 불가(숫자 포함 가능), 특수기호(!@#) 삽입불가(_dict : _사용가능)
# - 예약어(함수명, 함수 내 인자명, 패키지 이름... if, for, while)

vsum = 1                              
vsum                                  

v1 = 'abcd'
v1

# 모듈(module) : 함수나 변수 또는 클래스를 모아 놓은 파일
# 패키지(package)
# import 모듈 호출(loading)

round(1.5)
# trunc(1.5) 불가

# 1) 모듈 호출 : 하위 함수(모듈명.함수명)
import math
import math as ma #as (alias : 별명)

ma.trunc(1.5)
# 2) 모듈 내 함수 직접 호출 : 함수명만 사용 가능
from math import trunc
trunc(1.5)


math.pow(3,2) #3의 제곱


#2-1. 숫자형

# 숫자형
# 정수형(Integer)
a = 123
# 실수형(Floating-point)
a = 1.2

# 산술연산
3 + 2
3 / 1.5
10-2
5*3

9 // 2 #몫
9%2 #나머지
3**2 #거듭제곱

#2-2. 문자열 자료형
#문자열(String) : 문자, 단어 등으로 구성된 문자들의 집합
"life is too short, You need Python"
"a"
'Pythong is fun'
"""Life is too short, You need python"""
'''A'''

# 1. 문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때
# 1) 문자열에 작은따옴표(') 포함시키기
food = "Python's favorite food is perl"
# food = 'Python's favorite food is perl' : Python을 문자열로 인식
# SyntaxError: invalid syntax

# 2) 문자열에 큰따옴표(") 포함시키기
say = '"Python is very easy." he says.'

# 3) 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 2. 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1) 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"

# 2) 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기
multiline = '''
Life is too short
You need python
'''

multiline = """
Life is too short
You need python
"""

print(multiline)

# 이스케이프 코드
# \n : 문자열 안에서 줄을 바꿀 때 사용
# \t : 문자열 사이에 탭 간격을 줄 때 사용
# \\ : 문자 \를 그래도 표현할 때 사용
# \' : 작은따옴표(')를 그대로 표현할 때 사용
# \" : 큰따옴표(")를 그대로 표현할 때 사용
# \r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f : 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a : 벨 소리(출력할 때 PC 스피커에서 '삑'소리가 난다.)
# \b : 백 스페이스
# \000 : 널 문자

# 문자열 연산하기
# 문자열 더해서 연결하기(Concatenation)
head = "Python"
tail = " is fun!"
head + tail

# 문자열 곱하기
a = "python"
a*2

# 문자열 길이 구하기
a = "Life is too short"
len(a)

# 문자열 인덱싱(Indexing)
a = "life is too short, You need Python"
a[3]
a[12]
a[-1]
a[-0] # a[0]

# 문자열 슬라이싱
a = "life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
b

a[0:4] # 0<= a < 3
a[5:7]
a[19:]
a[:17]
a[:]
a[19:-7]

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date #'20010331'
weather #'Rainy'

year = a[:4]
day = a[4:8]
weather = a[8:]
year #'2001'
day #'0331'

a = "Pithon"
a[1]
a[1] = 'y'
# 당연히 오류가 발생한다. 
#왜냐하면 문자열의 요솟값은 바꿀 수 있는 값이 아니기 때문이다
#문자열 자료형은 그 요솟값을 변경할 수 없다. 그래서 immutable한 자료형이라고도 부른다.

a[:1] #'P'
a[2:] #'thon'
a[:1] + 'y' + a[2:] #'Python'

문자열 포매팅
"I eat %d apple." %3 # 숫자 바로 대입
"I eat %s apples." %five #문자열 바로 대입
#※ 문자열을 대입할 때는 앞에서 배운 것처럼 큰따옴표나 작은따옴표를 반드시 써주어야 한다.

number = 3
"I eat %d apples." $number

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number,day)

# %f : floating-point

"I have %s apples" %3
"rate is %s" %3.234
"Error is %d%%." %98

# 포맷코드와 숫자 함께 사용하기
# 정렬과 공백
"%10s" % "hi"
#'        hi' : 전체길이 10

"%-10sjanes." % 'hi'
#'hi        janes.'

#소수점 표현하기
"%0.4f" % 3.42134234
#'3.4213'

"%10.4f" % 3.42134234
#'    3.4213'

#format 함수를 사용한 포매팅
"I eat {0} apples.".format(3)
"I eat {0} apples.".format("five")

number=3
"I eat {0} apples."format(number)

number=3
day="three"
"I ate {0} apples. so I was sick for {1} days.".format(number,day)
"I ate {number} apples. so I was sick for {day} days.".format(number=10,day=3)
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)

"{0:<10}".format("hi") #왼쪽 정렬
"{0:>10}".format("hi") #오른쪽 정렬
"{0:^10}".format("hi") #가운데 정렬

#공백 채우기
"{0:=^10}".format("hi")
#'====hi===='
"{0:!<10}".format("hi")
#'hi!!!!!!!!'

#소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
#'3.4213'
"{0:10.4f".format(y)
#'    3.4213'

#{ 또는 } 문자 표현하기
"{{ and }}".format()
#{ and }

# f 문자열 포매팅
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
age = 30
f'나는 내년이면 {age+1}살이 된다.'

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

f'{"hi":<10}' #왼쪽 정렬
f'{"hi":>10}' #오른쪽 정렬
f'{"hi":^10}' #가운데 정렬

f'{"hi":=^10}' # 가운데 정렬, '='문자로 공백 채우기
f'{"hi":!^<10}' # 왼쪽 정렬, '!'문자로 공백 채우기

y = 3.42134234
f'{y:0.4f}'
f'{y:10.4f}'
f'{{ and }}'

# 문자 개수 세기(count)
a = "hobby"
a.count('b') #2

# 위치 알려주기1(find)
a = "Python is the best choice"
a.find('b') #14
a.find('k') #-1(존재x)

# 위치 알려주기2(index)
a = "Life is too short"
a.index('t') #8
a.index('k')
# ValueError: substring not found

# 문자열 삽입(join)
",".join('abcd') #'a,b,c,d'
",".join(['a','b','c','d']) #'a,b,c,d'

a = "hi"
a.upper()
a = "HI"
a.lower()

# 왼쪽 공백 지우기(lstrip)
a = " hi "
a.lstrip()

# 오른쪽 공백 지우기(rstrip)
a = " hi "
a.rstrip()

# 양쪽 공백 지우기(strip)
a = " hi "
a.strip()

# 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg")

# 문자열 나누기(split)
a = "Life is too short"
a.split()
#['Life','is','too','short']
b = "a:b:c:d"
b.split(':')
#['a','b','c','d']




















