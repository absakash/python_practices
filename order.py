order_list={
      "pizza": 150,
      "juice":100,
      "fish":120,
      "roll":60
}

print("welcome to py resturant \n")
print(" pizza : 150\n juice: 100 \n fish : 120 , roll: 60")
print("what do you want to order : ")
name_order=(input(""))
total=0;
if name_order in order_list:
      total+=order_list[name_order]
      print(f"your order {name_order} has been added")
else :
      print("your order is not available yet \n")

another_order=(input("do you wanna order more "))
if another_order=="yes":
      new_item=input("enter the second item ")
      total+=order_list[new_item]
else:
      print("item is not available yet")

print("your bill is  ",total)