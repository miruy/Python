# 내가 만든 커스텀 모듈 사용 (파일명 사용)

import my_module

selected = my_module.random_rsp()
print(selected)
print('가위?', my_module.SCISSOR == selected)

# Java의 getScissor() = Python의 .SCISSOR <바로 변수명>

# 커스텀 모듈 파일과 커스텀 모듈을 사용할 파일이 같은 패키지(폴더)에 있어야함 (Java와 같음)


