"""
lambdaは無名関数である。
def 名前(引数, 引数, ...):
    return 式

名前 = lambda 引数, 引数, ...: 式
"""
def add_method(x,y=1):
    return x+y
print(add_method(3,4))
# 7

add_lambda = lambda x,y = 1: x+y
print(add_lambda(3,4))
# 7

lis = [1,2,3,4]
print(list(map(lambda x:x**2, lis)))
# [1, 4, 9, 16]

#ディクショナリのリスト
employees = [
    {"name": "John", "age": 21},
    {"name": "Kevin", "age": 45},
    {"name": "Amy", "age": 21},
    {"name": "Ryan", "age": 30}
]
result = filter(lambda x: x["age"] > 25, employees)
print(list(result))
# [{'name': 'Kevin', 'age': 45}, {'name': 'Ryan', 'age': 30}]

result = map(lambda x: x["name"], (filter(lambda x: x["age"] > 25, employees)))
print(list(result))
# ['Kevin', 'Ryan']