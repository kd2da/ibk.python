"""
나이 = 현재년도 - 태이난년도 + 1
태어난 년도는 input() 함수를 사용하여 입력 받는다.
"""
# from 모듈명 import 클래스명 또는 함수명
from datetime import datetime as dt

print(dt.today())
# year property 로 보기 떄문에 year() 로 호출하지 않는다.
print(dt.today().year)

current_year = dt.today().year
print("태어난 년도를 입력하세요.")
birth_year = int(input())


# pep 8 에 coding style 을 정해놔서 거기에 맞지 않을 경우 연한 밑줄이 그어진다.
def age_cal(age):
    if 17 <= age < 20:
        print(f"당신은 {age} 살이며, 고등학생 입니다.")
    elif 20 <= age < 27:
        print(f"당신은 {age} 살이며, 대학생 입니다.")
    else:
        print(f"당신은 {age} 살이며, 학생이 아닙니다.")


age_cal(current_year - birth_year + 1)
