s1 = "Hello  Python, how   are  you!"
if("  " in s1):
        print("Double spaces are present.")
        print("String having double space is : " + s1)

        s1 = s1.replace("  " , " ")
        print("\nDouble space has been removed.\nNow the string is : " , s1)

