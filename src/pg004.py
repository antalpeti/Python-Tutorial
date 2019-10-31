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