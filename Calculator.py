from Functions import * # functionality from Functions.py will be available in this file 

while True: #infinite loop will enable code to run over and over again
    print("What do you want to do?")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Calculate a = 5 * 2 + 3 (Operator Precedence)")
    print("6 Check vote eligibility")
    print("Enter Q to Exit") #to terminate program

    choice = input("Enter your choice : ")
    if choice == 'q' or choice == 'Q': #same as line 9
        break
    
    if choice in ['1', '2', '3', '4']:
       num1 = float(input("Enter the number 1 : "))
    num2 = float(input("Enter the number 2 : "))

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
         multiplication(num1,num2)
    elif choice == '4':
         division(num1,num2)
         
    elif choice == '5':
           a = 5 * 2 + 3
           print(f"The value of 'a' (5 * 2 + 3) is: {a}")
           # Multiplication first (5 * 2 = 10)
           # Addition second = 10 + 3 = 13
           # Therefore a = 13
           
    else:
        print("Invalid Choice")
            
    print("\n") #Spacing for readability
   
    num = int(input("Enter your answer from above ^: ")) #Result number above
    
    if num % 2 == 0:  #Check if number is odd or even
        print(f"{num} is an even number.")
    else:
        print(f"{num} is an odd number.")
        print("Enter Q to Exit")
        
    choice = input("Enter your choice : ")
    if choice == 'q' or choice == 'Q': #same as line 9
        break
        
    print("\n") #Spacing for readability
        
    #check if person is eligible to vote or not (must be 18+ to vote)
    age=int(input("Enter your age: "))
    
    if age >=18:
        print("you are eligible to vote!")
    else:
        print("you are not over 18 to be able to vote therfore you are not eligible")
        print("Enter Q to Exit")
        
    choice = input("Enter your choice : ")
    if choice == 'q' or choice == 'Q': #same as line 9
        break
    
    print("\n") #Spacing for readability
    
    
   
