#Minimum appends needed to make a string pallindrome

s = input("enter a string ")
x=0

def appends(s):
	if(isPalin(s)):
		return 0
	s = s[1:]

	return 1 + appends(s)

def reverse(s): 
    return s[::-1] 

def isPalin(s):

	rev = reverse(s)

	if(s==rev):
		return True
	else:
		return False

x = appends(s)
print(x)