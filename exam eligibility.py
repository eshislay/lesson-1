print("exam eligibility test")
medical_cause=input("enter medical cause either yes/no:")
attendence=int(input("enter an attendence:"))
if medical_cause=="yes":
    print("you are eligibe for exams")
else:
    if attendence>=75:
     print("you are eligible for exams")
    else:
     print("you are not eligible for exams")