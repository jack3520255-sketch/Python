# write a program that the user to enter numbers and stops only when the user enter done 
# after this print avg,min,max number from all number enter by user

count=0
sum=0
while True:
  user= input("Enter number or write done to stop: ")
  a= user
  if user=='done':
    print("Program end")
    break

  user= int(user)
  sum= sum+user
  count+=1
  
  if count ==1:
    min=max=user
  if user>max:
    max=user
  if user<min:
    min=user    

print(f"Max: {max}")  
print(f"Min: {min}")  
print(f"Max: {sum/count}")  