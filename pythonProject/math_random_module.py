# Java의 클래스 = Python의 모듈
import math # 수학 모듈
import random # 랜덤함수 모듈

r = 10
result = 2 * math.pi * r # math모듈의 파이(pi)를 구하는 함수
print(result)

print(math.ceil(2.5)) # 강제 반올림 (round()와 비슷 : 반올림함수)
print(math.floor(2.5)) # 강제 반내림

# 그외에도 다양한 수학기능이 math모듈에 있음

print('------------------------')

candidates = ['가위', '바위', '보']
selected = random.choice(candidates) # candidates의 요소값 중 랜덤으로 값을 선택하는 함수

print(selected)

print('------------------------')

# randint(a, b) : a <= n <= b
n = random.randint(2, 5)
print(n)

print('------------------------')

# shuffle(list변수명) : 랜덤으로 순서를 섞음
list = [2, 4, 6, 3, 5, 10]
random.shuffle(list)
print(list)

