total_amount=int(input("enter total number:"))
paid_amount=int(input("enter paid amount:"))
def calculate(total,paid):
    due_amount=total-paid
    print("Due amount:",due_amount)
    calculate(total_amount,paid_amount)