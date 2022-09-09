## 딕셔너리 수정하기


list = [1, 2, 3, 4, 5]

# list 수정
list[2] = 33

# list 추가
list.append(6)

# list 삭제
del (list[0])

# list 삭제, 삭제된 요소값을 return 해줌
print(list.pop(0))

print(list)


# 딕셔너리 만들기
dict = {
    'one' : 1,
    'two' : 2
}

# 딕셔너리 수정하기
dict['one'] = 11

# 딕셔너리 추가하기
dict['three'] = 3

# 딕셔너리 삭제
del dict['two']

# 딕셔너리 삭제, 삭제된 요소값을 return 해줌
print(dict.pop('one'))

print(dict)