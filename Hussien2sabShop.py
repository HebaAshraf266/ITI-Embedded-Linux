from tkinter import*

Larage_cost=0
L_Total_cost=0
Medium_cost=0
M_Total_cost=0
Small_cost=0
S_Total_cost=0
TotalCost=0

print("Cost of Larage = 30")
print("Cost of Meduim = 20")
print("Cost of Small = 10")

# Functions to calculate quantities + price
def ButtonPressLarage():
	ButtonPressLarage.counter +=1 
	global Larage_cost
	Larage_cost=30
	print("Quantity of Larage 2sab= " , ButtonPressLarage.counter)
	global L_Total_cost
	L_Total_cost=Larage_cost*ButtonPressLarage.counter
	print("Total cost for your Larage 2sab order= ",L_Total_cost)
	
ButtonPressLarage.counter =0


def ButtonPressMedium():
	ButtonPressMedium.counter1 +=1 
	global Medium_cost
	Medium_cost=20
	global M_Total_cost
	M_Total_cost=Medium_cost*ButtonPressMedium.counter1
	print("Quantity of Medium 2sab= " , ButtonPressMedium.counter1)
	print("Total cost for your Medium 2sab order= ", M_Total_cost)
	
ButtonPressMedium.counter1 =0


def ButtonPressSmall():
	ButtonPressSmall.counter2 +=1 
	global Small_cost
	Small_cost=10
	global S_Total_cost
	S_Total_cost=Small_cost*ButtonPressSmall.counter2
	print("Quantity of Small 2sab= " , ButtonPressSmall.counter2)
	print("Total cost for your Small 2sab order= ",S_Total_cost)
	
ButtonPressSmall.counter2 =0


def ButtonTotalCost():
	global TotalCost
	TotalCost=L_Total_cost+M_Total_cost+S_Total_cost
	print("Total cost for your order= ",TotalCost)

#Create instance
Shop= Tk()  
Shop.title = ("BEST 2SAB")

label_1=Label(Shop,text="Welcome to Hussien 2sab Shop ",bg = "khaki2")
label_1.pack(side=TOP)


Shop.geometry ('500x500')

# Addi photo in background
photo1 = PhotoImage(file='2sab.png')
label2 = Label( Shop, image = photo1)
label2.place(x = 0,y = 25)


B1= Button(Shop, text="Larage",width=8,height=2 ,bg="DarkOliveGreen3", fg="black",bd='5', command = ButtonPressLarage)
B1.place(x=20, y=40)

B2= Button(Shop, text="Medium", width=8,height=2 ,bg="DarkOliveGreen3", fg="black",bd='5', command = ButtonPressMedium)
B2.place(x=20, y=90)

B3= Button(Shop, text="Small", width=8,height=2 ,bg="DarkOliveGreen3", fg="black",bd='5', command = ButtonPressSmall)
B3.place(x=20, y=140)

B4= Button(Shop, text="Exit", width=8,height=2 ,bg="DarkOliveGreen3", fg="black",bd='5',command = Shop.destroy)
B4.place(x=280, y=400)

B5= Button(Shop, text="TotalCost", width=8,height=2 ,bg="DarkOliveGreen3", fg="black",bd='5', command = ButtonTotalCost)
B5.place(x=180, y=400)

Shop.mainloop()

mysize=["Larage","Meduim","Small"]

myquantity=[]
myquantity.append(ButtonPressLarage.counter)
myquantity.append(ButtonPressMedium.counter1)
myquantity.append(ButtonPressSmall.counter2)

mycost=[]
mycost.append(L_Total_cost)
mycost.append(M_Total_cost)
mycost.append(S_Total_cost)

MyDict={'Size': [],
'Quantity':[],
'Cost':[]
}

MyDict['Size']=mysize
MyDict['Quantity']=myquantity
MyDict['Cost']=mycost
print(MyDict)

#To store data in excel file
import csv 
filename="2sabShop.csv"
with open(filename, 'w',newline='') as csvfile: 
	writer=csv.DictWriter(csvfile,fieldnames=['Size','Quantity','Cost'])
	writer.writeheader()
    
	csvwriter = csv.writer(csvfile)     
	
	for list in zip(mysize,myquantity,mycost):			
		csvwriter.writerow(list)
		
		
with open (filename,'r') as file:
	csvreader=csv.reader(file)
	for row in csvreader:
		print(row)
