import os
import sys

try:
	username = sys.argv[1]
	password = sys.argv[2]
	sign = sys.argv[3]
except:
	username = raw_input("username->")
	password = raw_input("password->")
	sign = raw_input("imza->")

print "username->",username
print "password->",password
print "signature->",sign


os.system("xterm -e python write.py {} {} {} &".format(username,password,sign))
os.system("python read.py {} {} {}".format(username,password,sign))
