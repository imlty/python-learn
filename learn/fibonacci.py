def fib(n):
    """
    this is the function document
    菲波那切数列   
    the end
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# 调用函数并打印2000以内的斐波那契数列
fib(2000)
print(fib.__doc__)

# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
#
#    this is the function document
#    菲波那切数列
#    the end
#
