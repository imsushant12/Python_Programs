#list comprehension
ls = [i   for i in range(10)   if(i%2 == 0)]
print(ls)


#dictionary comprehension
d1 = {i:f"item-{i}"  for i in range(10)   if(i%3 == 0)}
print(d1)
#reversing the above dictionary
d2 = {value:key for key,value in d1.items()}
print(d2)


#set comprehension
ls2 = [10 , 20 , 30 , 10 , 50 , 20 , 50]
s1 = {i   for i in ls2}
print(s1)