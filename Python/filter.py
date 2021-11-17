"""
filter(関数、リスト)
"""
#関数で実行
def func(x):
    return x >= 5
lis = list(filter(func, [1,2,3,4,5,6,7,8,9,10]))
print(lis)
''' [5, 6, 7, 8, 9, 10] '''

#ラムダでの可能
import random
new = [random.randint(1,11) for _ in range(20)]
print(new)
print(list(filter(lambda x:x >= 5, new)))
#[10, 4, 9, 6, 7, 3, 3, 11, 4, 9, 1, 2, 5, 6, 1, 6, 1, 8, 4, 7]
#[10, 9, 6, 7, 11, 9, 5, 6, 6, 8, 7]