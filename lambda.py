#lambda function or anonymous functions
def add(a, b):
    return a+b
print(add(3 , 4))
#def minus(x, y):
 #   return x-y
minus = lambda x, y: x-y
print(minus(9, 6))
def a_first(a):
    return a[1]
a = [[1,2], [45, 34], [0, 8]]
a.sort(key=lambda x:x[1])
#a.sort(key=a_first)
print(a)