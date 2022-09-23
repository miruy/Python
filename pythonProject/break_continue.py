list = [1,2,3,5,7,2,5,237,55]

# for val in list:
#     if val % 3 == 0:
#         print(val)
#         break

# for i in range(10):
#     if i % 2 != 0:
#         print(i)
#         print(i)
#         print(i)
#         print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    print(i)
    print(i)
    print(i)

# continue 장점 : 제외하는 부분을 처음에 처리함으로써 핵심이 되는 블록이 너무 깊게 들어가지 않도록 방지해줌(가독성 효과)
