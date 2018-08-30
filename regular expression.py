#Question 1

import re
s=input("Enter an Email: ")
m=re.findall('^[0-9A-Za-z][\w_]*[@](gmail.com|yahoo.com)',s)
if m:
    print("Valid Email")
else:
    print("Invalid Email")


#Question 2

import re
s=input("Enter a mobile number with country code: ")
m=re.findall('^[+]91[6-9][0-9]{9}',s)
if m:
    print("Valid Number")
else:
    print("Not a valid number")
