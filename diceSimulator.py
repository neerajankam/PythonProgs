from random import randint
no_attempts=3
attempt=0

actual_no = str(randint(1,6))
print(actual_no)
check= False

while(attempt<=no_attempts):
 attempt+=1	
 guessed_no = raw_input("Enter a number between 1 & 6\n")
 if(guessed_no == actual_no):
  print('You are really amazing at guessing!\n')
  check=True
  break
 else: 
  print('Please try again!\n')
  
if check==True:
 print('Let us play some other time....')  
else:	
 print('You are out of tries :( ')	
