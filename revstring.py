#Write a function revstring(mystr) that uses a stack to reverse the characters in a string.


def revstring(mystr):

	
	l = []
	for i in mystr:
		l = i.split() + l
	
	rev = ''.join(l)
	return rev

	
	

