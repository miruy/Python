# else if문
# if : if문 조건이 참일 때 실행
# else : if문 조건이 거짓일때 실행

# !변수가 대문자인 경우 : 자주쓰이는 값에 이름을 주는 것 / 코드 작성 시 따옴표로 나누어 관리하기 번거롭기 때문
SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이겼다!'
DRAW = '비겼다..'
LOSE = '졌다ㅠ'

me = '가위'
you = '바위'

# if문과 else문을 따로 사용했을 떼

if me == you:
    result = DRAW
else:
    if me == SCISSOR:
        if you == ROCK:
            result = LOSE
        else:
            result = WIN
    else:
        if me == ROCK:
            if you == PAPER:
                result = LOSE
            else:
                result = WIN
        else:
            if me == PAPER:
                if you == SCISSOR:
                    result = LOSE
                else:
                    result = WIN
            else:
                print('결과 이상해요')


print(result)


print('--------------------')

# if문과 else문을 합쳐 elif문으로 사용하였을 때

if me == you:
    result = DRAW
elif me == SCISSOR: # 그 조건이 아니고 이 조건이라면
    if you == ROCK: # 이 조건이 참이라면
        result = LOSE
    else:   # 위 조건이 거짓이라면
        result = WIN
elif me == ROCK:
    if you == PAPER:
        result = LOSE
    else:
        result = WIN
elif me == PAPER:
    if you == SCISSOR:
        result = LOSE
    else:
        result = WIN
else:
    print('결과 이상해요')


print(result)

"""
Java와 Python 의 else if문 차이

if / if
else / else
* else if / elif
"""






