# Q-1. Python program to check if the given number is Happy Number
# A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly.
# If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy
# number.
# Let's understand by an example:
# Number = 32
# 3^2 + 2^2=13
#  1^2 + 3^2 = 10
#  1^2 + 0^0= 1 happy number

a= int(input("Enter number: "))
while a!=1 and a!=4:
  sum=0
  while a!=0:
    r=a%10
    sum+=r**2
    a=a//10
  a=sum
if a==1:
  print("Happy number")
else:
  print("Unhappy number")      
  
# ---------------------------------------------------------------------------------------------

limit= int(input("Enter number: "))
for i in range(limit):
  