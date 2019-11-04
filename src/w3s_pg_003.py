txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(8))
print(txt.expandtabs(10))


txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)


txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)


txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)


txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)


txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
#print(txt.encode(encoding="ascii",errors="strict"))


txt = "My name is Ståle"

x = txt.encode()

print(x)


txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 10, 24)

print(x)


txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)


txt = "banana"

x = txt.center(20, "O")

print(x)


txt = "banana"

x = txt.center(20)

print(x)


txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)


txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)


#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 


#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 


#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 


txt = "Hello\tWorld!"
print(txt) 


txt = "Hello\rWorld!"
print(txt) 


txt = "Hello\nWorld!"
print(txt) 


txt = "This will insert one \\ (backslash)."
print(txt) 


txt = 'It\'s alright.'
print(txt) 


txt = "We are the so-called \"Vikings\" from the north."
print(txt) 


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


a = "Hello"
b = "World"
c = a + b
print(c)


txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x) 


txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a = "Hello, World!"
print(a.replace("H", "J"))


a = "Hello, World!"
print(a.upper())


a = "Hello, World!"
print(a.lower())


a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


a = "Hello, World!"
print(len(a))


b = "Hello, World!"
print(b[-5:-2])



b = "Hello, World!"
print(b[:5])


b = "Hello, World!"
print(b[1:])



b = "Hello, World!"
print(b[2:5])


a = "Hello, World!"
print(a[1])


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


a = "Hello"
print(a)


#You can use double or single quotes:

print("Hello")
print('Hello')
