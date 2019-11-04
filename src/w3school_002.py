x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)


x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)


x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)


import random

print(random.randrange(1,10))


x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))


x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = bytes(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = bool(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = frozenset(("apple", "banana", "cherry"))

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = set(("apple", "banana", "cherry"))

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = dict(name="John", age=36)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = range(6)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = tuple(("apple", "banana", "cherry"))

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = list(("apple", "banana", "cherry"))

#display x:
print(x)

#display the data type of x:
print(type(x)) 



x = complex(1j)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = float(20.5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = int(20)

#display x:
print(x)

#display the data type of x:
print(type(x)) 


x = str("Hello World")

#display x:
print(x)

#display the data type of x:
print(type(x)) 
