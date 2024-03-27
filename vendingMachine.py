#amount is the customer inserted total amount
#price is the total price 
def vendingMachine(amount, price):
    remaining = amount - price
    notes = [100, 50, 20, 10, 5, 1]
    count = {}
    for x in notes: 
        count[x] = remaining // x
        remaining = remaining % x
   
    result = f"Total Credit: RM{amount}\n"
    result += f"Total Price: RM{price}\n"
    result += f"Total Return: RM{amount - price}\n"

    for note, quantity in count.items():
        result += f"Note {note}: {quantity}\n"
    
    return result


prices = [3,4,5]
names = ["a","b","c"]
prom = ""
total_price = 0
for index, (price, name) in enumerate(zip(prices, names)):
    prom += f"{index}. Drink {name}: RM{price}\n"
continue_loop  = True
while continue_loop : 
    amount = int(input("Enter Money: "))

    while(total_price<=amount):
        print(prom)
        select = int(input("Enter Selection (-1 for done): "))
        if select == -1 :
            print(vendingMachine(amount, total_price))
            break
        else:
            if(select<len(prices)) :
                total_price+=prices[select]


    if total_price>amount:
        print("Credit Not Enough!!")
        total_price -= prices[select]
        print(vendingMachine(amount, total_price))
    
    answer = input("Do you want to continue? (anykey for yes , 0 for no)")
    if answer == 0 :
        continue_loop = False
    else :
        continue_loop = True


