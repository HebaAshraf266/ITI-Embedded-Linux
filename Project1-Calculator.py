# # Calculator -- programmer,  standard (Using eval())

# print("Hello Caluclator!")
# Status=True
# while Status:
#    print("Standard mode            press 1")
#    print("Programmer mode          press 2")
#    print("Exit                     press 0")

#    print("-"*40) #--> Separator
#    user_mode=int(input("Enter your choice for mode: "))
#    print("-"*40) #--> Separator

#    #while True: 
#    if user_mode==1:
#         print("Enter first number ")
#         print("Enter operation + - * / % ")
#         print("Enter other numbers with other operation ")
#         Result=eval(input("Enter a math expression: "))
#         print("Result of operation= ",Result)
#         print("-"*40) #--> Separator


#    elif user_mode==2:
#         print("For Logical operations       press 1")
#         print("For Binary conversion        press 2")
#         print("For Hexdecimal conversion    press 3")
#         print("Exit                         press 0")

#         print("-"*40) #--> Separator
#         prog_mode=int(input("Enter your choice: "))
#         print("-"*40) #--> Separator

#         if prog_mode==1:
#             print("For Logic NOT                    Press 1")
#             print("For Other logical operations     Press 2")
#             Choice=int(input("Enter your chioce: "))
#             print("-"*40) #--> Separator
#             if Choice==1:
#                 result=eval(input("Enter the number: "))
#                 print("Result of logical NOT= ",(~result))
#                 print("Result in binary= ",bin(~ result))
#                 print("-"*40) #--> Separator
#             elif Choice==2:
#                 print("Enter first number") 
#                 print("Enter logic operator , option for operators: & | ^ >> << ")
#                 print("Enter other numbers operation with other operator")
#                 Result=eval(input("Enter a math expression: "))
#                 print("Result of operation= ",Result)   
# 			    print("Result in binary= ",bin(Result))
#                 print("-"*40) #--> Separator 

#         elif prog_mode==2:
#             num=int(input("Enter your decimal number to convert to binary: "))
#             #print("-"*40) #--> Separator
#             print(f"Binary number of Decimal number {num} = {bin(num)}")
#             print("-"*40) #--> Separator

#         elif prog_mode==3: 
#             Num=int(input("Enter your decimal number to convert to hexdecimal: ")) 
#             print(hex(Num))
#             print("-"*40) #--> Separator
        
#         else:
#             Status=False              
#    else: 
#        break



# Calculator -- programmer,  standard (Using eval())

print("Hello Caluclator!")
Status=True
while Status:
   print("Standard mode            press 1")
   print("Programmer mode          press 2")
   print("Exit                     press 0")

   print("-"*40) #--> Separator
   user_mode=int(input("Enter your choice for mode: "))
   print("-"*40) #--> Separator

   #while True: 
   if user_mode==1:
        print("Enter first number ")
        print("Enter operation + - * / % ")
        print("Enter other numbers with other operation ")
        Result=eval(input("Enter a math expression: "))
        print("Result of operation= ",Result)
        print("-"*40) #--> Separator


   elif user_mode==2:
        print("For Logical operations       press 1")
        print("For Binary conversion        press 2")
        print("For Hexdecimal conversion    press 3")
        print("Exit                         press 0")

        print("-"*40) #--> Separator
        prog_mode=int(input("Enter your choice: "))
        print("-"*40) #--> Separator

        if prog_mode==1:
            print("For Logic NOT                    Press 1")
            print("For Other logical operations     Press 2")
            Choice=int(input("Enter your chioce: "))
            print("-"*40) #--> Separator
            if Choice==1:
                result=eval(input("Enter the number: "))
                print("Result of logical NOT= ",(~result))
                print("Result in binary= ",bin(~ result))
                print("-"*40) #--> Separator
            elif Choice==2:
                print("Enter first number") 
                print("Enter logic operator , option for operators: & | ^ >> << ")
                print("Enter other numbers operation with other operator")
                Result=eval(input("Enter a math expression: "))
                print("Result of operation= ",Result)   
                print("Result in binary= ",bin(Result))
                print("-"*40) #--> Separator 

        elif prog_mode==2:
            num=int(input("Enter your decimal number to convert to binary: "))
            #print("-"*40) #--> Separator
            print(f"Binary number of Decimal number {num} = {bin(num)}")
            print("-"*40) #--> Separator

        elif prog_mode==3: 
            Num=int(input("Enter your decimal number to convert to hexdecimal: ")) 
            print(hex(Num))
            print("-"*40) #--> Separator
        
        else:
            Status=False              
   else: 
       break