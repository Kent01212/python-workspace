def fib(n):
    return fib(n-2) +fib(n-1) if n > 1 else 1

def more_than_zero(func):
    def wrapper(n):
        if n > 0:
            return func(n)
        else:
            print("引数は0より大きい数にしてください")
        return None
    return wrapper
