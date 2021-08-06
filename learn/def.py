def fib(n):
    """斐波拉

    Args:
        n (number): 范围内的
    """
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a + b
        print()


# fib(1000)
# f = fib
# print(f(10000))
#


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib2(100000)
print(f100)