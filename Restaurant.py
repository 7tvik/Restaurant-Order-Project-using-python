#dictionary concept to used as display menu of MyResto
menu = {
    'pasta':90,
    'coffee':50,
    'burger': 70,
    'blackTea':20,
    'french-fries':90,
}

#Greet
print("\nWelcome to 'MyResto!!!'")
print("\n Coffee: 50 Rs\n blackTea: 20 Rs\n pasta: 90 Rs\n french-fries: 90 Rs\n burger: 70 Rs\n")

print("Do your order as name as in menu please...")
# variable to calculate the total amount
total_amount =0

item_1 = input("What would you like to have? : ")
if item_1 in menu:
    print(f"your order {item_1} has done successfully")
    total_amount += menu[item_1]
else:
    print("Please order from above menu, Sorry for inconvenience...\n")

more = "yes"
while more !="no" :
    more = input("\nDo you wanat something else? (yes/no): ")
    if more == "yes":
        item = input("order something: ")
        if item in menu:
            print(f"your order {item} has done successfully\n")
            total_amount += menu[item]
        else:
            print("Please order from above menu")
    else:
        print("Enter yes or no")

print(f"your total bill to pay is {total_amount}")