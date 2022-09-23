# 튜플을 이용한 list 출력
list = [1,2,3,4,5]

# 기본 list 출력
for i, v in enumerate(list):
    print('{}번째 값 : {}'.format(i, v))

print('----------------')

# 튜플 - 인덱스를 이용한 list 출력
for a in enumerate(list):
    print('{}번째 값 : {}'.format(a[0], a[1]))

print('----------------')

# 튜플 - * : 변수를 쪼개라 라는 뜻을 이용한 list 출력
for a in enumerate(list):
    print('{}번째 값 : {}'.format(*a))


print('-------------------------------------------')

# 튜플을 이용한 딕셔너리 출력
ages = {'Tod':35, 'Jane':23, 'Paul':62}

# 기본 딕셔너리 출력
for key,val in ages.items():
    print('{}의 나이는 : {}'.format(key, val))

print('----------------')

# 튜풀 - 인덱스를 이용한 딕셔너리 출력
for a in ages.items():
    print('{}의 나이는 : {}'.format(a[0], a[1]))

print('----------------')

# 튜플 - *를 이용한 딕셔너리 출력
for a in ages.items():
    print('{}의 나이는 : {}'.format(*a))