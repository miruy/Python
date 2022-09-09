## 딕셔너리와 반복문


# list 반복문
seasons = ['봄', '여름', '가을', '겨울']

for season in seasons:
    print(season)

print('------------------------')

# 딕셔너리 반복문
ages = {
    'Tod' : 35,
    'Jane' : 23,
    'Paul' : 62
}

# key만 가지고 오는 방법 , default가 key로 가지고 오기 때문에 keys() 생략가능
for key in ages.keys():
    print(key)

for key in ages:
    print(key)

# value만 가지고 오는 방법
for value in ages.values():
    print(value)

# key를 이용해 value값 불러오기
for key2 in ages.keys():
    print('{}의 나이는 {}입니다.'.format(key2, ages[key2]))

# key와 value를 같이 받아오는 방법
for key, value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key, value))

