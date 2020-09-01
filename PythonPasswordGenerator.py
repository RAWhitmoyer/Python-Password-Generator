import random 
import sys
import getopt

##global
##determines possible characters to be used in strings
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowers = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
special = "~`!@#$%^&*()_+-=[]{}<>?|"

##converts strings to list for easier access
caps = list(caps)
lowers = list(lowers)
digits = list(digits)
special = list(special)

def generate(num_char_type):
##empty password list
password = []

##loop to generate characters
for i in range(num_char_type):

##random capital letter
rand = random.randint(0, 25)
password.append(caps[rand])

#random lowercase letter
rand = random.randint(0, 25)
password.append(lowers[rand])

#random digit
rand = random.randint(0, 9)
password.append(digits[rand])

#random special character
rand = random.randint(0, 23)
password.append(special[rand])


##shuffles password, creates final string
random.shuffle(password)
final_password = ""
for i in password:
final_password += i
print("Password: " + final_password)


def main(argv):
##check for only one argument
if len(argv) > 1:
print("A max of one argument may be passed")
sys.exit(2)
##determines number of each char type in password
num_char_type = 2

##processes arguments
try:
opts, args = getopt.getopt(argv, "hml")
except getopt.GetoptError:
print("error")
sys.exit(2)
for opt, arg in opts:
if opt == "-h":
print("-h help, -m medium (12 characters), -l long (16 characters)")
print("ex. PasswordGenerator3.py -l")
sys.exit()
elif opt == "-m":
##3 of each character type
num_char_type = 3
elif opt == "-l":
##4 of each character type
num_char_type = 4

generate(num_char_type)



if __name__ == "__main__":
main(sys.argv[1:])











