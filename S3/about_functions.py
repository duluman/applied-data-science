

def f_double(func, arg):
  return func(func(arg))


def mult(x):
  return x * x


print(f_double(mult, 7))