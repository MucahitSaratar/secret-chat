import requests as R
import sys
import time
import os

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

def cmd(kom):
	os.system(kom)


komut = "curl -s --socks5-hostname 127.0.0.1:9050 http://rgpon3r67u5bt4geytqmojrn3rkm5kr3bcw4seeyn2ai2umiu3z4okid.onion/chat/index.php -d \"username={}&password={}&signature={}&islem=write&mesaj=FUZZ\"".format(username,password,sign)
while True:
	try:
		mesaj = raw_input("mesaj->")
		cmd(komut.replace("FUZZ",mesaj))
	except:
		break
