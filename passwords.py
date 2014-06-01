import sys

users_and_password = {}
password_count = 3
weak_passwords = {}
medium_passwords = {}
strong_passwords = {}

def main():
	
	for x in range(0,password_count):
		#Grab the password
		username = raw_input("Input a username \n")
		users_and_password[username] = raw_input("Input a password for that username \n")
		password = users_and_password[username]
		#Check the password
		if check_pass_length(password):
			if check_pass_strength_weak(password):
				print "Weak"
			elif check_pass_strength_medium(password) and check_pass_strength_strong(password):
				print "Strong"
			elif check_pass_strength_medium(password):
				print "Medium"
			# elif (check_pass_strength_medium(password) == "Medium" and check_pass_strength_strong(password) == "Strong"):
			# 	print "Strong"
			# elif (check_pass_strength_medium(password) == "Medium" and check_pass_strength_strong(password) == "Strong"):
			# 	print "Strong"
				
	print users_and_password.items()			
	
def check_pass_length(password):
	if password < 12 or password > 6: 
		return True

#These functions need some cleaning and combining

def check_pass_strength_weak(password):
	upper_count = 0
	lower_count = 0
	number_count = 0
	for letter in password:
		if letter.isdigit():
			number_count = number_count + 1
		elif letter == letter.lower():
			lower_count = lower_count + 1
		elif letter == letter.upper():
			upper_count = upper_count + 1
	
	if upper_count == len(password) or lower_count == len(password) or number_count == len(password):
		return True
	else:
		return False
		
def check_pass_strength_medium(password):
	upper_count = 0
	lower_count = 0
	number_count = 0
	for letter in password:
		if letter.isdigit():
			number_count = number_count + 1
		elif letter == letter.lower():
			lower_count = lower_count + 1
		elif letter == letter.upper():
			upper_count = upper_count + 1
			
	
	if upper_count > 0 or lower_count > 0 or number_count > 0:
		return True
	else:
		return False
		
def check_pass_strength_strong(password):
	upper_count = 0
	lower_count = 0
	number_count = 0
	for letter in password:
		if letter.isdigit():
			number_count = number_count + 1
		elif letter == letter.lower():
			lower_count = lower_count + 1
		elif letter == letter.upper():
			upper_count = upper_count + 1

	if upper_count > 0 and lower_count > 0 and number_count > 0:
		return True
	else:
		return False

if __name__ == '__main__':
	main()