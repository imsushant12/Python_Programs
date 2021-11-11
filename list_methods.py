""""
10 methods of list. 
"""

l = [10, 15, 5, 25, 20]

# 1. append()
l.append(30)
print(l)

# 2. insert()
l.insert(2, 35)
print(l)

# 3. reverse()
l.reverse()
print(l)

# 4. sort in ascending order: sort()
l.sort()
print(l)

# 5. sort in descending order: sort(reverse = True)
l.sort(reverse = True)
print(l)

# 6. count(number)
print(l.count(5))

# 7. copy()
l2 = l.copy()
print(l2)

# 8. remove(number)
l.remove(5)
print(l)

# 9. pop()
print(l.pop())

# 10. clear()
l.clear()
print(l)