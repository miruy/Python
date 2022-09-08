# 입사 로봇
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

# 이전 방법
print(number, '번 손님', greeting, '.', place, '에 오신걸', welcome, '!')

print()

# format()를 이용한 편리한 값 대입 방법
base = '{}번 손님, {}. {}에 오신걸 {}!'
new_wqy = base.format(number, greeting, place, welcome)

print(new_wqy)

print()

mine = '가위'
yours = '바위'
result = '졌다...ㅠㅠ'

print('나는 {}, 너는 {} 그래서 {}'.format(mine, yours, result))