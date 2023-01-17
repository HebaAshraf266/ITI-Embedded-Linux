import os
import time

n=int(input("Enter the number of rows:"))

while True:
	#RIGHT
	for i in range (n):
		print("*"*(i+1))
			
			
	for j in range(n):
		print("*"*(n-j-1))

	print('\n')
	time.sleep(1)
	os.system('cls')

	#UP
	for i in range (n):
		for j in range (i,n):
			print(' ',end='') #Space
			
		for j in range(i):
			print('*',end='')
			
		for j in range(i+1):
			print('*',end='')

		print()

	print('\n')
	time.sleep(1)
	os.system('cls')



#LEFT
	for i in range (n):

		if i==n-1:
			print((i+1)*"*")
		else:
			print((n-i-1)*" ",end="")
			print((i+1)* "*")
			
	for j in range (n-1,0,-1):
		print((n-j)*" ",end="")
		print(j* "*");

	print('\n')	

	time.sleep(1)
	os.system('cls')
			
		

	#Down
	for i in range (n):
		for j in range (i+1):
			print(' ',end='') #Space
			
		for j in range(i,n-1):
			print('*',end='')
			
		for j in range(i,n):
			print('*',end='')

		print()		
		
	time.sleep(1)
	os.system('cls')
