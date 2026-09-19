def total_cost(billing_amount,tip_percentage):
    total=billing_amount*(1+0.01*tip_percentage)
    total=round(total,2)
    print(f"Your total is ${total}")


total_cost(150,20)