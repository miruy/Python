# value에 10을 더한 값을 돌려주는 함수
def add_10(value):
    if value < 10:
        return 10   # 해당 return 실행 후 함수 종료

    result = value + 10
    return result

n = add_10(5)
print(n)

n = add_10(42)
print(n)

n = round(1.5)
print(n)
