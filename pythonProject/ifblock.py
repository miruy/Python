# 블록
# 콜론 다음에 들여쓰기 된 부분을 블록이라고 부름

if True:
    print('블록에 속한 코드')

    if False:
        print('한 줄 더')

    if True:
        print('또 한줄 더')

    print('블록의 끝 코드')

print('바깥 블록의 끝')


print('-------------------')

if False:
    print('조건이 맞지 않아 실행되지 않는 블록')

    if True:
        print('조건이 맞는 코드')

    print('어쨋든 실행되지 않는 코드')

print('다시 바깥에 있는 코드')











