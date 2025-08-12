#Palindrome or not
def isPal(s):s
    if s[::-1]==s:
        print("its a palindrome")
    else:
        print("Its not a palindrome")
s=input()
isPal(s)
