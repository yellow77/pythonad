# 程式7-9.py ( Python 3 version )
def pick(x):
    fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
    return fruits[x]
alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
#map(function, iterable, ...) , 据函数对指定序列做映射,function-函数，有两个参数/iterable--一个或多个序列
choices = map(pick, alist) 
for choice in choices:
    print(choice)