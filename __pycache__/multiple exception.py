try:
    num1 = int(input("enter a number:"))
    num2 = int(input("enter a number:"))
    result= num1/num2
    print("result is:", result)
except ZeroDivisionError:
      print("devision by zero is not allowed ")
except ValueError:
    print("please enter numerical value")
except NameError as ex:
    print("the exception is",ex)
except:
    print("some error occured")
finally:
    print("i will execute no matter what happens")