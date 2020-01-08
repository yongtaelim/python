# Python
## install
python 다운로드에는 두가지 방법이 있다.  
1. 공식 홈페이지에서 다운로드
```
https://www.python.org/downloads/
```
2. 아나콘다 배포판 설치
```
설치 링크 : https://www.anaconda.com/downloads
설치 메뉴얼 : https://www.runnablecode.com/entry/%EC%95%84%EB%82%98%EC%BD%98%EB%8B%A4-%EB%B0%B0%ED%8F%AC%ED%8C%90Python-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0
```
- 파이썬은 인기가 많은 언어이므로 다양한 배포판이 존재한다. 가장 많이 사용되는 아나콘다(Anaconda) 배포판이 있다.  
- 배포판은 사용자가 한번의 클릭만으로 기본적이고 다양한 분야의 라이브러리와 필요한 파일등을 자동으로 설치해준다.

## tool - pycharm
```
설치 링크 : https://www.jetbrains.com/pycharm/download/
설치 매뉴얼 : https://www.runnablecode.com/entry/Anaconda-%EC%84%A4%EC%B9%98-%ED%9B%84-Pycharm-Virtual-ENV-%EC%97%B0%EB%8F%99%ED%95%98%EA%B8%B0?category=830618
```

## 학습
cmd -> python
git clone https://github.com/yongtaelim/python.git >> study
```
https://dojang.io/mod/page/view.php?id=2176
```
### 변수
- 변수 선언
```python
x, y, z = 10, 20
x = y = z = 10
```
- 변수 삭제
> list 사용할 때 del이 유용하게 쓰인다.
```python
x = 10
del x
```
- 빈 변수 선언
>보통 다른언어에서 null로 사용된다.
```python
x = None
```
### input 함수
#### input 함수를 사용해보자.
```python
input()
#input :: Hello, world!
#output :: 'Hello, world!'
```
#### input 함수를 사용해 변수에 넣어보자.
```python
x = input()
#input :: Hello, world!
#output :: 
x
#'Hello, world!'
```
#### input 함수에 placeholder 기능
```python
x = input('문자열을 입력하세요: ')
#문자열을 입력하세요: Hello, world!
x
#'Hello, world!'
```
#### input 함수에 입력값 split
변수1, 변수2 = input('문자열').split('기준 문자열')
```python
a, b = input('숫자 두 개를 입력하세요: ').split() # 입력받은 값을 공백 기준으로 split
#숫자 두개를 입력하세요: 10 20
```
#### map에 int와 input함수를 같이 사용하면 input 결과를 모두 int로 반환해준다.
```python
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
#숫자 두 개를 입력하세요: 10 20
```
### output
#### 값을 여러개 출력하기
print(값1, 값2, 값3)
```python
print(1, 2, 3)
#1 2 3
print('Hello', 'Python')
#Hello Python
```
#### sep로 값 사이에 문자 넣기
sep :: separator
print(값1, 값2, sep='문자 또는 문자열')
```python
print(1, 2, 3, sep=', ')
# 1, 2, 3
print(1920, 1080, sep='x') 
# 1920x1080
print(1, 2, 3, sep='\n')
#1
#2
#3
print(1)
print(2)
print(3)
#1
#2
#3
print(1, end='')
print(2, end='')
print(3, end='')
#123
```  
### 비교 연산자
is, is not  
==, !=는 값 자체를 비교하고, is, is not 은 객체를 비교
```python
a = -5
a is -5
#True
a = -6
a is -6
#False
```
변수 a가 있는 상태에서 다른 값을 할당하면 메모리 주소가 달라진다.

### list
빈 list 생성
```python
b = list()
b
#[]
```
range 이용하여 list 생성
```python
range(10) or range(0, 10)
range(0, 10, 2)
# [0, 2, 4, 6, 8]
range(10, 0, -1)
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a = list(range(10))
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
### tuple
- list 처럼 요소를 일렬로 저장하지만 안에 저장된 요소를 변경, 추가, 삭제할 수 없다.  
- 읽기 전용 리스트
```python
a = (38, 21, 53, 62, 19)
a
#(38, 21, 53, 62, 19)
a = 38, 21, 53, 62, 19
a
#(38, 21, 53, 62, 19)
```
range 이용하여 tuple 생성
```python
a = tuple(range(10))
a
#(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
```
tuple -> list
```python
a = [1, 2, 3]
tuple(a)
#(1, 2, 3)
```
list -> tuple
```python
a = (1, 2, 3)
list(a)
#[1, 2, 3]
```
언패킹 : list와 tuple의 요소를 변수 여러개에 할당하는것
```python
x = [1,2,3]
a,b,c = x
print(a,b,c)
#1 2 3
y = (4,5,6)
d, e, f = y
print(d,e,f)
#4 5 6 
```
### 시퀀스 자료형 활용
#### 특정값 체크
```python
a = [1,2,3,4,5,6,7,8,9]
9 in a
#True
11 not in a
#True
'P' in 'Hello, Python'
#True
```
#### 객체 연결
```python
a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
a + b
#[0, 10, 20, 30, 9, 8, 7, 6] 
```
range는 `+` 연산자로 연결할 수 없다.   
문자열에 숫자 연결할 수 없다. 숫자를 str으로 치환 후 연결
```python
a = range(10)
b = range(10, 20)
#a + b (X)
#list(a) + list(b) (O)
```
#### list && tuple 개수
```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
len(a)
hello = '안녕하세요'
len(hello.encode('utf-8'))
```
#### list slice
```python
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a[0:4]
#[0, 1, 2, 3]
a[2:8:3]
#[2, 5]
a[:3]
#[0, 1, 2]
a[:]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
###딕셔너리
- 연관된 값을 묶어서 저장하는 용도로 딕셔너리 자료형  
- 중복되는 키는 저장되지 않음. (키가 중복되면 가장 뒤에 있는 값만 사용됨.)
```python
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
```
#### 딕셔너리 생성
```python
a = {}
b = dict()
c = dict(health=490, mana=334, melee=550, armor=18.72)
d = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
e = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
f = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
```
#### 딕셔너리의 키에 값 할당
딕셔너리[키] = 값
```python
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037
```
키 값 확인
```python
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
'health' in lux
```
키 개수
```python
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
len(lux)
```
### if 조건문
- `들여쓰기` 필수
- `:` 필수
```python
x = 10
if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

if x == 10:
    pass
```
### 반복문
#### for
```python
for i in range(100):
    print('Hello, world')

x = ('apple', 'orange', 'grape')
for fruit in x:
    print(fruit)
```
#### while
```python
i = 0
while i < 100:
    print('Hello, world!')
    i += 1
```

### 주석
- `TODO`
- `FIXME`
- `BUG`
- `NOTE`

### keyword
- 인터프리터(intepreter) : 코드를 한줄 한줄 실행하여 결과를 얻는 방식
- 파이썬 프롬프트(Python prompt) : 파이썬 셸에서 '>>>' 부분

## unittest
### 개념정리
테스트 자동화, 테스트를 위한 사전 설정(setup)과 종료(shutdown) 코드 공유, 테스트를 컬렉션에 종합하기, 테스트와 리포트 프레임워크의 분리 등을 지원한다.  
이를 달성하기 위해 unittest는 객체 지향적인 방법으로 몇 가지 중요한 개념을 지원한다.
#### Test Fixture
1개 또는 그 이상의 테스트를 수행할 때 필요한 준비와 그와 관련된 정리 동작에 해당합니다.   
임시 또는 프락시 데이터 베이스, 디렉터리를 생성하거나 서버 프로세스를 시작하는 것 등을 포함한다.
#### Test Case
테스트의 개별 단위  
특정한 입력 모음에 대해서 특정한 결과를 확인한다. unittest는 베이스 클래스인 Test Case를 지원한다. 이 클래스는 새로운 테스트 케이스를 만드는 데 사용된다.
#### Test Suite
여러 테스트 케이스, 테스트 묶음, 또는 둘 다의 모임이다.  
서로 같이 실행되어야 할 테스트들을 종합하는 데 사용된다.
#### Test Runner
테스트 실행을 조율하고 테스트 결과를 사용자에게 제공하는 역할을 하는 컴포넌트이다.  
실행자는 테스트 실행 결과를 보여주기 위해 그래픽 인터페이스, 텍스트 인터페이스를 사용하거나 특별한 값을 반환할 수도 있다.  
