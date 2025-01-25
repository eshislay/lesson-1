print("profit/loss")
AC=input("enter actual cost")
AC=int(AC)
SC=input("enter selling cost:")
SC=int(SC)
amount=SC-AC
if amount>0:
    print("profit of",amount)
else:
    print("loss of",amount)