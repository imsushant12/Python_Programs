"""
10 Dictionary Methods.
"""

d = {
    "name": "John",
    "surname": "Cena",
    "champs": 16
}

# 1. get()
print(d.get("name"))

# 2. copy()
d2 = d.copy()
print(d2)

# 3. keys()
print(d.keys())

# 4. values()
print(d.values())

# 5. update(key:value):
d.update({"surname": "Cena!"})
print(d)

# 6. pop(key)
print(d.pop("surname"))

# 7. popitem()
print(d.popitem())

# 8. items()
print(d.items())

# 9. setdefault()
d.setdefault("best wrestler", True)
print(d)

# 10. clear()
d.clear()
print(d)
