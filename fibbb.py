from timeit import Timer

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

t1 = Timer("fib(10)", "from fibbb import fib")

for i in range(1,41):
    s = "fib(" + str(i) + ")"
    t1 = Timer(s, "from fibbb import fib")
    time1 = t1.timeit(3)
    print("Calculated fib(%2d), it took %8.6f sec" % (i, time1))
