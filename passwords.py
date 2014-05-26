import sys

def main():
    users_and_pass = {}
    
    for x in range(0,1):
		username = raw_input("Input a username")
		users_and_pass[username] = raw_input("Input a password for that username")
	
	print users_and_pass.items()
	
def check_pass(password):
	if password == password.upper():
		return "Password is all uppercase"
	elif password == password.lower():
		return "Password is all lowercase"
	elif len(password) < 8:
		return "Password is too short"
	elif password == int:
		return "Password is just numbers"

if __name__ == '__main__':
	main()