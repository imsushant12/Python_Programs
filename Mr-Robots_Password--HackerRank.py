'''
Problem Statement: 
------------------
Mr. John is making a website, in which there is a tab to create a password. 
As other websites, there are rules so that the password gets complex and none can predict the  password for another. 
So he gave some rules like:
	1. At least one numeric digit 
	2. At Least one Small/Lowercase Letter 
	3. At Least one Capital/Uppercase Letter 
	4. Must not have space
	5. Must not have slash (/)
	6. At least/Minimum 6 characters

	If someone inputs an invalid password, the code prints: 
		“Invalid password, try again”.
	Otherwise, it prints: 
		“password valid”.
	Input Format:
		A line with a given string as a password
	Output Format:
		If someone inputs an invalid password, the code prints: 
			“Invalid password, try again”.
	Otherwise, it prints: 
		“password valid”, without the quotation marks.
	Constraints:
		Number of character in the given string <=10^9
		Sample input 1:
			abcDeF012
		Sample output 1:
			password valid
		Sample input 2:
			abcDefGH
		Sample output 2:
			Invalid password, try again
		Note: Without using any pythons library like(re, string etc)
'''

def CheckPassword(s, n):
    if n < 6:
        return 0

    capitals = 0
    numbers = 0
    lowers = 0

    for i in range(n):
        if s[i] == ' ' or s[i] == '/':
            return 0

        if s[i] >= 'A' and s[i] <= 'Z':
            capitals += 1

        if s[i] >= 'a' and s[i] <= 'z':
            lowers += 1
            
        elif s[i].isdigit():
            numbers += 1

    if capitals > 0 and numbers > 0 and lowers > 0:
        return 1
    else:
        return 0


s = input()
if CheckPassword(s, len(s)):
    print("password valid")
else:
    print("Invalid password, try again")
