from random import randint
_try=0
no_of_tries= 5
check= False
actual_no = randint(0,100)
print(actual_no)
while ( _try <= no_of_tries):
 _try+=1
 guess_no = int(raw_input('Guess the number ;)\n'))
 if guess_no == actual_no:
    print('Damn, you are phenomenal at this game!\n')
    check= True
    break
 elif( abs(actual_no-guess_no) <=10 ):
    print('Pretty Close. Try again!\n')
 else:
        print('Your guess is not close to the actual number. Try again\n')
if check == True:
	print('All hail Master. You guessed it right at try number '+ str(_try))
else:
   print('Not your day. Come back again!')	


