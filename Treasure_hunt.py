# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
ind = position.split(" ")
print(ind)
if int(ind[1]) == 3:
  row3[int(ind[0]) - 1] = 'X'
elif int(ind[1]) == 2:
  row2[int(ind[0]) - 1] = 'X'
else:
  row1[int(ind[0]) - 1] = 'X'
  
  






#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
