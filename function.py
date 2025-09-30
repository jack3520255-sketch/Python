# Positional argument & keyword argument:

# def add(a=3,b=5):
#   x=a+b
#   return x
# print(add(7,3))
# print(add(11))
# print(add(b=3))
# print(add(7,b=8))
# print(add(b=9,a=15))
# print(add(a=5,7))

# -------------------------------------------------------------------------------------------------------

# Arbitary argument:

# def fun(*a):
#   for i in a:
#        print(i)
#   print(a)         
# fun(1,4,5,6,7,8,9)

# -------------------------------------------------------------------------------------------------------

# def g(x):
#   def h(x):
#     x=x+1
#     print(x)
#   x=x+1
#   print(x)
#   h(x)
#   return x
# x=3
# z=g(x)
# print(x)
# print(z)

# --------------------------------------------------------------------------------------------------------

def fun(a):
  # global a
  a=a+1
  print(a)
# a=5
fun(5)  