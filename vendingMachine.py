#amount is the customer inserted total amount
#price is the total price 
def vendingMachine(amount, price):
    remaining = amount - price
    notes = [100, 50, 20, 10, 5, 1]
    count = {}
    for x in notes: 
        count[x] = remaining // x
        remaining = remaining % x
   
    result = ""
    for note, quantity in count.items():
        result += f"Note {note}: {quantity}\n"
    
    return result

print(vendingMachine(100, 20))
