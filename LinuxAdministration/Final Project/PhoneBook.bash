#!/bin/bash
exit=0
file=Database.txt
i=0

#Check if the file exist
if ! [ -f "$file" ];then 
	touch Database.txt
fi

while [ $exit -ne 1 ]
do 
	echo "--------------------------------------------------------------"
	echo "Select the operation "
	printf "1.Add new phone contact\n"
	printf "2.View all contacts\n"
	printf "3.Search for phone record\n"
	printf "4.Delete specific contact\n"
	printf "5.Delete All contacts\n"
	printf "6.Exit\n"
	echo "--------------------------------------------------------------"
	read Answer
	echo "--------------------------------------------------------------"
	
	if [ $Answer -eq 1 ]
	then
		echo "Create new record"
		printf "Enter the first name: "
		read Fname
		printf "Enter the last name: "
		read Lname
		printf "Enter the phone number: "
		read Number
		echo "$Fname $Lname : $Number " >> Database.txt 


	elif [ "$Answer" -eq 2 ]
	then
		echo "Display all records "
		cat $file 
		#i= $( ( $i + 1 ) )
		#echo "$i $line"
		#done 


	elif [ "$Answer" -eq 3 ]
	then
		echo "Search a record"
		printf "Enter the first name or Last name or phone number: "
		read search 
		#found= `ls | grep $search | wc -w` 
		
		#found= $( (grep $search $file) )
		#if [ $found -eq 0 ] 
		#then
		#	echo "No record found"
		#else
		grep $search $file
		#	grep $search $file | while read -r line ; do
		#	i= $( [ $i+1 ] )
		#	echo "$i $line"
		#	done
		#fi
		

	#delete specific record
	elif [ "$Answer" -eq 4 ]
	then
		#echo "Search a record "
		printf "Enter the first name or Last name or phone number to delete: "
		read Search
		#Found= `ls | grep $Search`
		#Found= $( grep $Search  $file )
		#if [ $Found -eq 0 ] 
		#then 
		#echo "No record found "
		#else
		#grep $Search $file | while read -r line ; do 
		#i= $( [ $i+1 ] )
		#echo "$i $line"
		#done
		#printf "Enter the number you wanna delete"
		#read deleteNo
		#i=0
		#grep $search $file | while read -r line ; do
		#i= $ [ $i+1 ]
		#if [ $deleteNo -eq $i ]
		#then
		#echo "`sed /"$line"/d Database.txt `" > Database.txt
		#fi 
		#done
		#fi
		###sed `s/$Search/Deletedrecord/` Database.txt
		
		sed -i -e "/$Search/d" Database.txt
		#fi
		
	#Delete all records 
	elif [ "$Answer" -eq 5 ]
	then
		echo "Delete all records"
		echo " " > $file 

	elif [ "$Answer" -eq 6 ]
	then
		exit=1 

	else 
	printf "No such options, Please select again \n"
	
	fi
done




