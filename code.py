# Write a program that take's the use input for hour,between 1 and 12 and take's the use input for A.M, P.M 
# Also take use input how many hour in future threr want to print. final Print out the time in the future by 
# calculat hour by user

a= int(input("Enter hour between(1-12): "))
b= input("Enter am or pm: ")
c= int(input("Enter future time: "))
           
for i in range(1,c+1):
  a+=1
  if a>12:
    a=a-12
  if a==12:
    if b=="am":
      b='pm'
    elif b=="pm":
      b='am'
print(a,b)        
  