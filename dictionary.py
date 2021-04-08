print("\t-:FIND DEVELOPER OF A LANGUAGE:-")

d = {
    "C" : "Dennis M. Ritchie",
    "C++" : "Bjarne Stroustrup",
    "Java" : "James Gosling",
    "Python" : "Guido van Rossum"
}

key = input('Enter Language : ')

if key in d:
    print(key, " is written by " + d[key])
else:
    print("TRY ANOTHER LANGUAGE")

# We can also write :-
# print(key, " is written by " , d.get(key))
