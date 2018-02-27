import sys
import string
import random

minPassLen = 4 			# minimal length of the password	
maxPassLen = 60			# maximal length of the password
bruteCalcPerformance = 10000000 # performance of brute force cracking 

def printHelp():
	print('Proper use of password generator is: ')
	print('  ',sys.argv[0],' #PasswordLength [-t]')
	print('-t')
	print('   is used for calculation of the maximum cracking time') 
	print('   of password with brute force method.')
	print('#PasswordLength')
	print('   represents the length of the password which should') 
	print('   be beetween', minPassLen, 'and', maxPassLen)
	return

# input check; syntax check of password length
try:
	int(sys.argv[1])
except:
	printHelp()	
	exit(0)
	
# input check; check of password length
if (int(sys.argv[1]) < minPassLen or int(sys.argv[1]) > maxPassLen):
	print('Password length should be beetween', minPassLen, 'and', maxPassLen, '.')
	exit(0)

# collection of characters which will be used for creation of the password	
string.letters 	= 'abcdefghjkmnpqrstuvwxyzABCDEFGHIJKMNPQRSTUVWXYZ' # included in collection
string.numbers 	= '23456789' 			# included in collection
string.symbols 	= '@#$%' 				# included in collection
string.ambigous = '{}[]()/\'"`~,;:.<>' 	# excluded from collection
string.similar 	= 'il1Lo0O' 			# excluded from collection
string.collection = string.letters + string.numbers + string.symbols  

# generation of the password
string.password = ''
for i in range (0, int(sys.argv[1])):
	string.password += random.choice(string.collection)
print('Password:', string.password)

# calculation of time for cracking password lengthOfPassword ^ numberOfPossibleCharacters / 10M
try:
	sys.argv[2] 
except:
	exit(0)
else:
	if sys.argv[2] != '-t':
		print('Wrong switch: ', sys.argv[2])			
		printHelp()			
	else:
		sec = len(string.collection) ** int(sys.argv[1]) / bruteCalcPerformance
		print('Max cracking time with brute force in seconds:', sec)
