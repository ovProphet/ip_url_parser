import sys
import re
import httplib2
from IPy import IP

http = httplib2.Http()

print "1) Enter an address -> receive IPs\n2) Enter a filename -> receive IPs\n3) Enter a filename -> receive URLs"
choice = raw_input("Your choice is: ")
if choice == '1':
	addr = raw_input("Enter an address: ")
	try:
		response, content = http.request(addr,'GET',)
	except:
		print "Oops. No sites found."
		sys.exit()
	else:
		result = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', content)
		for a in result:
			try:
				IP(a)
			except: pass
			else:
				print a

elif choice == '2':
	fil = raw_input("Enter a filename: ")
	try:
		f=open('%s' % fil, 'rb')
	except:
		print "Oops. No files found.\n"
		sys.exit()
	content=f.read()
	result = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})', content)
	for a in result:
		try:
			IP(a)
		except: pass
		else:
			print a
elif choice == '3':
	fil = raw_input("Enter a filename: ")
	try:
		f=open('%s' % fil, 'rb')
	except:
		print "Oops. No files found.\n"
		sys.exit()
	content=f.read()
	result = re.findall(r'(https?://\S+)', content)
	for a in result:
		print a
else:
	print "Oops. You've typed a wrong character.\n"
	sys.exit()