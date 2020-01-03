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
```
x, y, z = 10, 20
x = y = z = 10
```
- 변수 삭제
> list 사용할 때 del이 유용하게 쓰인다.
```
x = 10
del x
```
- 빈 변수 선언
>보통 다른언어에서 null로 사용된다.
```
x = None
```
### input 함수
#### input 함수를 사용해보자.
```
input()
input :: Hello, world!
output :: 'Hello, world!'
```
#### input 함수를 사용해 변수에 넣어보자.
```
x = input()
input :: Hello, world!
output :: 
x
'Hello, world!'
```
#### input 함수에 placeholder 기능
```
x = input('문자열을 입력하세요: ')
문자열을 입력하세요: Hello, world!
x
'Hello, world!'
```
#### input 함수에 입력값 split
변수1, 변수2 = input('문자열').split('기준 문자열')
```
a, b = input('숫자 두 개를 입력하세요: ').split() # 입력받은 값을 공백 기준으로 split
숫자 두개를 입력하세요: 10 20
```
#### map에 int와 input함수를 같이 사용하면 input 결과를 모두 int로 반환해준다.
```
a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
숫자 두 개를 입력하세요: 10 20
```
### output
#### 값을 여러개 출력하기
print(값1, 값2, 값3)
```
print(1, 2, 3)
1 2 3
print('Hello', 'Python')
Hello Python
```
#### sep로 값 사이에 문자 넣기
sep :: separator
print(값1, 값2, sep='문자 또는 문자열')
```python
print(1, 2, 3, sep=', ')
# 1, 2, 3
print(1920, 1080, sep='x') 
# 1920x1080
```  

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
