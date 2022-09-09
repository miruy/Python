for i in range(10): # ~ = [0,1,2,3,4]
    print(i)

# range() : 0부터 매개변수까지의 순서대로 수를 list 형태로 만들어줌

names = ['철수', '영희', '바둑이', '귀도', '유림']

for i in range(len(names)):
    name = names[i]
    print('{}번 : {}'.format(i+1, name))

# len(names) : names의 길이 만큼

print()


for i, name in enumerate(names):
    print('{}번째 : {}'.format(name, i+1))

# enumerate() : 매개변수안의 개수(길이)와 값를 한번에 꺼내줌
# ! 쉼표 , 를 이용하면 여러개의 값을 돌려받을 수 있고 개수, 값 순서로 사용해야함!

# 순회할 횟수가 정해져있을때 사용