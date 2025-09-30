# write a program to encode a number enter by user base on follwing loop
# 1-->3  2-->4 3-->5  4-->6  5-->7  6-->8 7-->9 8-->1 9-->2  0-->0

a= int(input("Enter number between 0 to 9: "))
r=0
c=0
while a>0:
  b= a%10
  a=a//10
  
  if b in(0,1,2,3,4,5,6,7,8,9):
    if b==1:
      b=3
    elif b==2:
      b=4  
    elif b==3:
      b=5 
    elif b==4:
      b=6 
    elif b==5:
      b=7 
    elif b==6:
      b=8 
    elif b==7:
      b=9 
    elif b==8:
      b=1 
    elif b==9:
      b=2 
    elif b==0:
      b=0   
  
  r= r+(b*10**c)
  c+=1   

print(r)                  