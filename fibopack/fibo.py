
# Fibonacci numbers module

def fib(n):
    result = []
    a, b = 0, 1
    while b < n:
            result.append(b)
            a, b = b, a+b
    return result

if __name__ == "__main__":
    import sys
    print "module is called as script"
    result = fib(int(sys.argv[1]))
    print result
