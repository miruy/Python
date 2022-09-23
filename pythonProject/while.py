# selected = None # selectd = null
#
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에 선택하세요 > ')
#
# print('선택된 값은 : ', selected)

# print('------while문 과 for문 비교------')

patterns = ['가위', '보', '보']

length = len(patterns)
i = 0

while i < length:
    print(patterns[i])
    i = i+1