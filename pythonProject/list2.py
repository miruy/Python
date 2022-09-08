# list2에 숫자 16을 요소값으로 추가해 7개의 요소를 가진 list로 바꾸기
list2 = [37, 23, 10, 33, 29, 40]
print(list2)

# 방법
# 1. append() : 하나의 list에 요소를 추가하는 함수
# list2.append(16)
# print(list2)
'''list += 요소값'''

# 2. list에 list를 더하는 방법
list3 = list2 + [16]
print(list3)

list4 = list3 + list3
print(list4)
'''list + list = new list'''

# in : list안에 해당 값이 들어있는지 아닌지를 boolean으로 판별
n = 12
ownership = n in list3
print(ownership) # list3에 12는 들어있지 않으므로 false

n = 10
if n in list3: # list3에 n값이 있다면 실행해라
    print('{}은 {}중에 있어!'.format(n, list3))

print()

# 요소값 삭제
# index번째를 지정하여 삭제
print('list4 확인용 :', list4)
del list4[12] # list4에 12번째 값(40)을 삭제 , del : delete
print(list4)

print()

# list에 들어있는 특정 값을 직접 입력하여 삭제
print('list4 확인용 :', list4)
# !! 40이라는 숫자가 여러개일 경우 처음에 해당하는 값만 삭제됨!!
list4.remove(40) # list4에 값 중 숫자 40을 삭제
print(list4)


