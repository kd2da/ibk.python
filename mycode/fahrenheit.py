"""
섭씨온도를 입력 받아서 화씨로 변환하기
"""
#섭씨를 화씨로 변환하는 함수
def fah_convert(celsius):
    return ((9/5)*float(celsius))+32

print("변환하고 싶은 섭씨 온도를 입력하세요.")
user_input=input()
print(type(user_input), user_input)
fah = fah_convert(user_input)
print('섭씨온도 :',user_input)
print(f'섭씨온도 : {user_input}')
# f 를 쓰면 정적인 변수 와 동적인 변수를 같이 사용할 수 있다.
print('화씨온도 : {0}'.format(fah))
print('화씨온도 : {0:.2f}'.format(fah))
print(f'화씨온도 : {round(fah,2)}')