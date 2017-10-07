def memoize(f):
    """ Decorator - memory for functions. Results of function f
        are stored in memory {}. Can be used to decrease th number
        of calls of a function, i.e. time """
    memory = {}
    def helper(x):
        if x not in memory:
            memory[x] = f(x)
        return memory[x]
    return helper

class Memoize:
    """ Decorator class - memory for functions. Same concept as
        func @memoize, only difference is that we use a Class
        instead of a function in case one wants to know the name,
        doc, etc of the original function """
    def __init__(self, fn):
        self.fn = fn
        self.memory = {}

    def __call__(self, *args):
        if args not in self.memory:
            self.memory[args] = self.fn(*args)
        return self.memo[args]
