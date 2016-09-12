class tracer:
    def __init__(self, func):
        self.cont = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.cont += 1
        print('Chamade de número %s a %s' % (self.cont, self.func.__name__))
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):
    print(a + b + c)

spam()
