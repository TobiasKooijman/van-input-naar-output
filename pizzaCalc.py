# Tobias Kooijman 99068704 Opdracht: Pizza Calculator
# Values

small = 1.99
medium = 4.99
large = 29.99

print("Choose your Pizza size!")
Size = input('Type Small(€1.99)/Medium(€4.99)/Large(€29.99) ')

# Large If

if (Size.lower() =="large"):
    print("Large Pizza selected")
    print("")
    print("----------------------------------------------------------------------------------------------------------------")
    print("")
    print("How many Pizza's do you want?")
    Amount = input('type the amount of pizzas you want: ')
    L_TA = 'Total amount of pizzas: ' + str(Amount)
    
    Calc_L = int(Amount) * 29.99
    
    print(L_TA)
    print("")
    print("----------------------------------------------------------------------------------------------------------------")
    print("")
    Total_L = 'The total price is: 29.99 X ' + str(Amount) + ' = ' + str(Calc_L)
    print(Total_L)
    print("Thank you for your large sized purchase!")
    print("you can pick up your pizza at your nearest pizza place!")

# Medium If

if (Size.lower() =="medium"):
    print("Medium Pizza Selected")
    print("")
    print("----------------------------------------------------------------------------------------------------------------")
    print("")
    print("How many Pizza's do you want?")
    Amount = input('type the amount of pizzas you want: ')
    M_TA = 'Total amount of pizzas: ' + str(Amount)
    
    Calc_M = int(Amount) * 4.99
    
    print(M_TA)
    print("")
    print("----------------------------------------------------------------------------------------------------------------")
    print("")
    Total_M = 'The total price is: 4.99 X ' + str(Amount) + ' = ' + str(Calc_M)
    print(Total_M)
    print("Thank you for your medium sized purchase!")
    print("you can pick up your pizza at your nearest pizza place!")

# Small If

if (Size.lower() =="small"):
    print("Small Pizza selected")
    print("")
    print("----------------------------------------------------------------------------------------------------------------")
    print("")
    print("How many Pizza's do you want?")
    Amount = input('type the amount of pizzas you want: ')
    S_TA = 'Total amount of pizzas: ' + str(Amount)
    
    Calc_S = int(Amount) * 1.99
    
    print(S_TA)
    print("")
    print("----------------------------------------------------------------------------------------------------------------")
    print("")
    Total_S = 'The total price is: 1.99 X ' + str(Amount) + ' = ' + str(Calc_S)
    print(Total_S)
    print("Thank you for your small sized purchase!")
    print("you can pick up your pizza at your nearest pizza place!")


