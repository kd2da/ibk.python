"""
dictionary 는 key:value 쌍으로 이루어진 데이터를 저장하는 자료구조
"""
my_dict = dict()
my_dict = {'name':'홍길동','age':20}
print(type(my_dict))
# dict 를 key 로 값을 조회
print(my_dict['name'])
print(my_dict['age'])

# dict 에 새로운 key 와 value를 추가
my_dict['address'] = '충주'

# print(mydict['name1'])
result = my_dict.get('name1')
if result :
    print(result)
else :
    print('key does not exits')

if 'name' in my_dict :
    print('name key 가 있습니다.')

for key, value in my_dict.items():
    print(key, value)