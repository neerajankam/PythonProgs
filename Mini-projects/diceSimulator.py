# Import the random module to simulate a roll of a dice
from random import randint 


def dice_simulator(tries):
	#Variable to keep track of the attempt numbers.
	attempt=0
	#Simulating the roll of a dice.
	actual_no = str(randint(1,6))
	#Boolean to keep track if the user was successful in guessing the right number or not.
	check = False
	#Loop which runs until the tries are exhausted or the user has guessed the right number.
	while attempt < tries:
		attempt += 1	
	 	guessed_no = raw_input("Enter a number between 1 & 6: ")
	 	#Checking if the user guessed number is equal to the roll of the dice
	 	if(guessed_no == actual_no):
	 		print('You are really amazing at guessing!\n')
	 		#Setting the boolean to True indicating that the user guessed the right number.
			check = True
	  		break
	 	else: 
	 		#User gets another try
	  		print('Please try again!\n')
	# if-else statement returns the outcome based on whether the user guess was right or not.  
	if check == True:
	 	return 'Let us play some other time....'  
	else:	
	 	return 'You are out of tries :( '

print(dice_simulator(int(raw_input("Enter the number of tries:"))))	 
