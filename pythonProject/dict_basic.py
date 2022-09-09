# Java의 switch~case와 같은 개념

# 딕셔너리 만들기
wintable = {
    '가위' : '보',  # 앞 : 이름표, 뒤 : 값 -> 가위라는 이름표를 가진 보라는 값을 실행해라
    '바위' : '가위',
    '보' : '바위'
}

# 매개변수로 인해 결과가 달라지는 함수
def rsp(mine, yours):
    if mine == yours:
        return '비겼다'
    elif wintable[mine] == yours:
        return '이겼다!'
    else:
        return '졌다ㅠㅠ'

# 함수에 매개변수 넣어 실행하기
mine = '가위'
yours = '바위'

result = rsp(mine, yours)

# 결과에 따른 출력 메세지

message = {
    '비겼다' : '나 : {}, 너 : {}. 그래서 {}'.format(mine, yours, result),
    '이겼다!' : '나 : {}, 너 : {}. 그래서 {}'.format(mine, yours, result),
    '졌다ㅠㅠ' : '나 : {}, 너 : {}. 그래서 {}'.format(mine, yours, result)
}
print(message[result])


