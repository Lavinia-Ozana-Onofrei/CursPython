def my_function1(*args, **kwargs):
    s = 0
    for i in args:
        if type(i) == int or type(i) == float:
            s = s+i
    return s


def my_function2(n):
    if n == 0:
        return [0, 0, 0]
    elif n % 2 != 0:
        return (n1 + n2 for n1, n2 in zip((n, 0, n), my_function2(n - 1)))
    else:
        return (n1 + n2 for n1, n2 in zip((n, n, 0), my_function2(n - 1)))


def my_function3():
    try:
        n = int(input("n= "))
        return n
    except ValueError:
        print("Nu este numar intreg!")
        return 0


if __name__ == '__main__':

    print(my_function1(1, 5, -3, 'abc', [12, 56, 'cad']))
    print(my_function1())
    print(my_function1(2, 4, 'abc', param_1=2))

    print(my_function2(10))

    my_function3()
