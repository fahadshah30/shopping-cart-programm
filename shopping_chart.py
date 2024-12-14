 # shopping cart program
 
foods = []
prices = []
total = 0
 
while True:
    food = input(f"enter food to buy(q to quit)")
    if food.lower == "q":
        break
    else :
        price = float(input(f"enter the prices of a {food}: $"))
        foods.append(food)
        prices.append(price)
print("..........your cart")

for food in foods:
    print(food)
for price in prices:
    total=total + price
print(f"your total is ${total}:")    


