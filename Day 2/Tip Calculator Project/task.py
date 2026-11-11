print("Welcome to the Tip Calculator!")
cost=float(input("How much would you like to pay? £"))
tip=int(input("How much tip would you like to give? 10, 12 or 15? "))
number_of_people=int(input("How many people are there to split the bill? "))
percentage=tip/100
percentage+=1
calculation_1=cost*percentage
calculation_1/=int(number_of_people)
calculation_2=round(calculation_1,2)
print(f"Each person should pay £{calculation_2}.")

