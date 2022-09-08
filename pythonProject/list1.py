list1 = ['가위', '바위', '보']
list2 = [37, 23, 10, 33, 29, 40]

# list1, list2라는 변수에 여러개의 값이 들어가있는 것
print(list1)
print(list2)

# index를 이용해 index번째 요소값만 불러옴
print(list1[0])
print(list2[4])

# index번째 값을 원하는 값으로 변경
list1[0] = '가위 대신 바위'
print(list1[0])
print(list1)

# -1의 의미는 '뒤에서 부터 첫번째'라는 뜻
print(list1[-1]) # 뒤에서 첫번째
print(list1[-2]) # 뒤에서 두번째
print(list1[-3]) # 뒤에서 세번째