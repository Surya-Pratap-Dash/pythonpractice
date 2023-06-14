from functools import partial


def multiply(a, b):
    return a*b


x = 2
f = partial(multiply, x)

result = f(10)  # 20
print(result)

x = 3
result = f(10)  # 20
print(result)
