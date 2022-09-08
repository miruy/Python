# 3. print_sqrt()함수에 매개변수로 a, b, c를 넣음
def print_sqrt(a, b, c):    # 매개변수 parameter
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))

# 1.
x = 1
y = 2
z = -8

# 2. 여기서 실행 인자로 전달된 x, y, z가 위의 매개 변수인 a, b, c에 대입 되었기 때문에 함수가 정상적으로 실행됨
print_sqrt(x, y, z) # 실행인자 argument



print('----------------')

def print_round(number):
    rounded = round(number); # round() : 숫자를 반올림하는 함수
    print(rounded)

print_round(4.6)
print_round(2.2)
print_round(3.6)

