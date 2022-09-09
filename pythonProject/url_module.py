# url을 매개변수로 넣으면 페이지 내용을 불러오는 함수

import urllib.request  # url을 요청하는 모듈 사용

def get_web(url):
    response = urllib.request.urlopen(url)    # 불러오고싶은 url을 요청하여 reponse변수에 담기
    data = response.read()      # reponse에 담겨진 불러오고싶은 url을 읽어서 data변수에 담기
    decoded = data.decode('utf-8')      # 읽어진 url을 사람이 해석할 수 있게 utf-8로 디코딩(부호화/암호화 해제)하요 decoded
    return decoded       # 사람이 이해할 수 있게 디코딩 된 decoded를 return

url = input('웹 페이지 주소를 입력하세요 > ')  # 사용자가 입력하는 url(input의 매개변수)이
content = get_web(url)  # get_web(url)의 매개변수로 들어가 위의 함수 실행될

print(content)

'''
그 외 알게된 것
- 인코딩 : 정보를 "부호화/암호화" 하다
- 디코딩 : 정보를 "부호화/암호화 해제" 하다
'''
