print("tip the waiter")
def cal_amount(amount,tp):
    tip=amount*tp*0.01
    total=amount+tip
    print("total amount:",total)
amount=int(input("enter amount:"))
tp=int(input("enter tip percentage:"))
cal_amount(amount,tp)