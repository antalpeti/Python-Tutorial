a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())


txt = "565543"

x = txt.isnumeric()

print(x)


a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())


txt = "hello world!"

x = txt.islower()

print(x)


a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


txt = "Demo"

x = txt.isidentifier()

print(x)


a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for 2

print(a.isdigit())
print(b.isdigit())

txt = "50800"

x = txt.isdigit()

print(x)


a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())


txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)


txt = "Company10"

x = txt.isalpha()

print(x)


txt = "CompanyX"

x = txt.isalpha()

print(x)


txt = "Company 12"

x = txt.isalnum()

print(x)


txt = "Company12"

x = txt.isalnum()

print(x)


txt = "Hello, welcome to my world."

print(txt.find("q"))
# print(txt.index("q"))


txt = "Hello, welcome to my world."

x = txt.index("e", 5, 10)

print(x)


txt = "Hello, welcome to my world."

x = txt.index("e")

print(x)


txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)


#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))

#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))


#Use "X" to convert the number into upper-case Hex format:

txt = "The Hexadecimal version of {0} is {0:X}"

print(txt.format(255))


#Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"

print(txt.format(255))


#Use "o" to convert the number into octal format:

txt = "The octal version of {0} is {0:o}"

print(txt.format(10))


#Use "G" to convert the number into upper-case general format:

txt = "The general version of {0} is {0:G}"

print(txt.format(211e11))


#Use "g" to convert the number into general format:

txt = "The general version of {0} is {0:g}"

print(txt.format(211E11))


#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:

txt = "The price is {:f} dollars."
print(txt.format(x))


#Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(45))

#without the ".2" inside the placeholder, this number will be displayed like this:

txt = "The price is {:f} dollars."
print(txt.format(45))


#Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))


#Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))


#Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))


#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"

print(txt.format(5))


#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."

print(txt.format(13800000000))


#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."

print(txt.format(13800000000))


#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."

print(txt.format(-3, 7))


#Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."

print(txt.format(-3, 7))


#Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."

print(txt.format(-3, 7))


#To demonstrate, we insert the number 8 to specify the available space for the value.

#Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."

print(txt.format(-5))


#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))


#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))


#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))


#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt = "Hello, welcome to my world."

print(txt.find("q"))
#print(txt.index("q"))


txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)


txt = "Hello, welcome to my world."

x = txt.find("e")

print(x)


txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)