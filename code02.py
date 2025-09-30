day= int(input("Enter days: "))
money=1
sunday=7
total=0
for i in range (day//7):
  for j in range(money,sunday+1):
    total+=j
  money+=1
  sunday+=1
for k in range(day%7):
  total+=money
  money+=1
print(total)  
