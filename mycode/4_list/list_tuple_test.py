# packing
my_list1 = [20,30,40]
# unpacking
n1,n2,n3 = my_list1
print(n1,n2,n3)
my_list2 = list()

# append, extend, insert
my_list1.append(10)
print(my_list1)
my_list1.extend([50,60])
print(my_list1)
my_list1.insert(0,10)
print(type(my_list1))
print(my_list1)
my_list1[2] = 100
print(my_list1[0:3])

# set (중복 허용 x, 순서 보장 x)
my_set = set(my_list1)
print(type(my_set))
print(my_set)

# tuple - read only list
my_tuple = (10,20,30,40)
my_tuple2 = tuple()
print(type(my_tuple))
print(my_tuple)
# TypeError: 'tuple' object does not support item assignment
# my_tuple[0] = 50
print(my_tuple)

num1 = (3)
num2 = (3,)
print(type(num1),type(num2))
#tuple usage
def swap(a,b):
    return (b,a)
n1,n2 = swap(10,20)
print(n1)
print(type(n1))
print(n2)
print(type(n2))

#문자열 타입 List 선언
cat_list = list('cat')
print(cat_list)

birth_day="2021/11/16"
birth_list = birth_day.split('/')
print(birth_list)
print('2021' in birth_list)
print('2021' not in birth_list)

if '2021' not in birth_list :
    print('not found')
else : print('found it')

