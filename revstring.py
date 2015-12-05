#Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

from stackLesson import Stack 
import time

def revstring(mystr):

	start = time.time()

	myStack = Stack()
	for ch in mystr:
		myStack.push(ch)
	rev = ''
	while not myStack.isEmpty():
		rev = rev + myStack.pop()
	
	end = time.time()
	return rev, 'Time: ', end-start


def revstring1(mystr):
	
	start = time.time()
	l = []
	for i in mystr:
		l = i.split() + l
	
	rev = ''.join(l)
	end = time.time()
	return rev, 'Time: ', end-start


	
	

