
def root(a, b, c):    # 매개변수 parameter
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2


x = 1
y = 2
z = -8

r1, r2 = root(x, y, x)
print('근은 {}'.format(r1, r2))

# python은 return 값으로 여러 개를 돌려줄 수 있고, return값을 여러 개의 변수로 받을 수 있음!