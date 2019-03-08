import random

nouns=[]
sports=[]
dishes=[]

for i in range(0,3):
	nouns.append(raw_input('Enter a noun!\n'))
	sports.append(raw_input('Enter the name of a sport!\n'))
	dishes.append(raw_input('Enter the name of a dish!\n'))
	print('----------------')

print('Neeraj is a ' + random.choice(nouns) +' guy. 
      He likes playing ' + random.choice(sports)+'. 
      His favorite dish is ' + random.choice(dishes))
print(nouns)
