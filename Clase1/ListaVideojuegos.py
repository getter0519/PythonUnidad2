def f(x=[]):
    x.append(2)
    return len (x)
print(f(), f(), f())
