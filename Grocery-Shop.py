#Grocerry Shop 

import time

Grocerry_Items={                       # -->Dictionary 
"Types":["Apple","Banana","Cherry"],
"Quantity":[40, 30, 70],
"Price":[15, 20, 25]
}

Customer_Dict={
"Bag": [],
"Quantity": [],
"Bill":[]
}

print("\nWelcome to ITI shop!")
Status=True
while Status:
 print("For Customer mode         press 1")
 print("For Owener mode           press 2")
 print("For Exist                 press 0")

 print("-"*40) #--> Separator
 mode_choice=int(input("Enter your mode choice "))
 print("-"*40) #--> Separator


 if mode_choice==1:                                  #--> Customer mode 
        print("To show our products      press 1")
        print("To Exist                  press 0")

        print("-"*40) #--> Separator
        customer_choice=int(input("Enter your choice: "))
        print("-"*40) #--> Separator

        if customer_choice==1:
            print("Shop products ",Grocerry_Items["Types"])
            print("Quantity of each type ",Grocerry_Items["Quantity"])
            print("Price for each type ",Grocerry_Items["Price"])
            loop=True
            while loop:
             print("-"*40) #--> Separator
             print("To Buy from our product     press 1")
             print("To print the bell           press 2") 
             print("Finished                    press 0")
             print("-"*40) #--> Separator
             x=int(input("Enter your choice: "))
             print("-"*40) #--> Separator
             if x==1:
                Fruit_type=input("Enter Fruit type you want to buy: ")
                Customer_Dict["Bag"].append(Grocerry_Items["Types"][Grocerry_Items["Types"].index(Fruit_type)])  
                print(Customer_Dict["Bag"])

                quantity=int(input("Enter the quantity you want to buy: "))
                Customer_Dict["Quantity"].append(quantity)
                print("Quantity= " ,Customer_Dict["Quantity"])

                Grocerry_Items["Quantity"][Grocerry_Items["Types"].index(Fruit_type)] -=quantity
                print("Available quantity for each type= ",Grocerry_Items["Quantity"])

             elif  x==2:
                bill = 0 
                for i in range(len(Customer_Dict["Bag"])):
                    #To calculate total cost
                    bill += Grocerry_Items["Price"][Grocerry_Items["Types"].index(Customer_Dict["Bag"][i])] * Customer_Dict["Quantity"][i]
                print("Total cost= ",end="")
                print(bill)

             elif x==0:
                 loop=False
                
                
 elif mode_choice==2:   
            Loop=True
            while Loop:                                #--> Owner mode 
             print("Show products             press 1")
             print("Add new products          press 2")
             print("Change cost               press 3")
             print("Exist                     press 0")
            
             print("-"*40) #--> Separator
             owner_choice=int(input("Enter your choice: "))
             print("-"*40) #--> Separator

             if owner_choice==1:
                print("Shop products ",Grocerry_Items["Types"])
                print("-"*40) #--> Separator

             elif owner_choice==2:
                Add_choice=input("Enter name of the new product: ")
                Grocerry_Items["Types"].append(Add_choice)
                
                Add_choiceQ=int(input("Enter quantity of the new product: "))
                Grocerry_Items["Quantity"].append(Add_choiceQ)

                Add_choiceP=int(input("Enter cost of the new product: "))
                Grocerry_Items["Price"].append(Add_choiceP)

                print(Grocerry_Items)
                print("-"*40) #--> Separator

             elif owner_choice==3:
                print("Products: ",Grocerry_Items["Types"])
                print("Cost of Products: ",Grocerry_Items["Price"])

                print("-"*40) #--> Separator
                i =input("Enter the element you want to change it's price: ")
                New_cost=int(input("Enter the new price: "))
                Grocerry_Items["Price"][Grocerry_Items["Types"].index(i)]=New_cost #--> To link price with its product 

                #print("Products: ",Grocerry_Items["Types"])
                print("Cost of Products: ",Grocerry_Items["Price"])

             elif owner_choice==0:
                Loop=False  
            
 else: 
    Status=False

