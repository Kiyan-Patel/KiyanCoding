def calculate_change(paid,amount):
    change=paid-amount
    return change

snack_price=25
print("======Snack Vending Machine======")
print(f"The price of the snack is {snack_price} units")
print("Accepted coins 1, 5, 10, 25/")

total_inserted=0
coins_inserted=0

while True:

    coin=int(input("The coins accepted are (1,5,10,25):"))

    if coin !=1 and coin !=5 and coin !=10 and coin !=25:
        print("Invaid coin/")
        continue 


# PART 5: Add the valid coin to the running total

total_inserted += coin

coins_inserted += 1

print(f"Inserted {coin}. Total so far: {total_inserted}\n")

# PART 6: Stop asking for coins once enough has been inserted

if total_inserted >= snack_price:
 print("Enough money inserted!\n")
 

# PART 7: Work out the change using the value returned by calculate_change

change_due = calculate_change(total_inserted, snack_price)

print("Dispensing your snack...")

# PART 8: Nothing extra to do when the change is exactly zero

if change_due == 0:

 pass

else:

 print(f"Here is your change: {change_due} units")

# PART 9: Print a short summary of the purchase

print("\n===== PURCHASE SUMMARY =====")

print("Snack Price:", snack_price)

print("Coins Inserted:", coins_inserted)

print("Total Paid:", total_inserted)

print("Change Given:", change_due)

print("=============================")

print("Thanks for your purchase!") 


