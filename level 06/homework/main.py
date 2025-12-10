# 2)მომხმარებელს შემოვატანინოთ თავისი სახელი, გვარი, ასაკი და ქალაქი.
#შემდეგ ეს ინფორმაცია ერთ წინადადებად დავბეჭდოთ ტერმინალში. 

name = input("Enter your name: ")
lastname = input("Your lastname: ")
age = input("enter your age: ")
city = input("enter in which city you live: ")

print(f"Your name is {name}, your lastname is {lastname}, you are {age} years old and you live in {city}.")


# 3) შექმენით ცვლადი სახელად celsius, სადაც შეინახავთ მთელ რიცხვს. 
# შემდეგ შექმენით ცვლადი სახელად fahrenheit, სადაც უნდა გამოთვალოთ წინა ცვლადის ტემპერატურა რამდენი ფაერენგეიტი იქნება. 
# ასევე შექმენით ცვლადი kelvin რომელშიც შეინახავთ თუ რამდენი კელვინი იქნება celsius ცვლადში მოცემული რიცხვი, 
# საბოლოოდ დაბეჭდეთ სამივე ცვლადი

celsius = 17
fahrenheit = ((celsius * 9/5) + 32)
kelvin = (celsius + 273.15)

print(f"Celsius is {celsius}")
print(f"fahrenheit is {fahrenheit}")
print(f"kelvin is {kelvin}")


# 4) თითოეულ მათემატიკურ ოპერატორზე (+, -, *, /, %, **, //) 
# შეასრულეთ 5 მაგალითი და დაბეჭდეთ შედეგი

# (+)
print(12 + 3)
print(29 + 17)
print(96 + 34)
print(187 + 22)
print(32 + 16)

#(-)
print(12 - 3)
print(17 - 6)
print(88 - 24)
print(129 - 86)
print(367 - 89)

#(*)
print(124 * 3)
print(18 * 9)
print(20 * 6)
print(16 * 5)
print(12 * 3)

# (/)
print(450 / 5)
print(336 / 3)
print(740 / 8)
print(45 / 3)
print(225 / 5)

# (//)
print(450 // 5)
print(336 // 3)
print(740 // 8)
print(45 // 3)
print(225 // 5)

# (%)
print(19 % 3)
print(77 % 2)
print(740 % 80)
print(90 % 7)
print(536 % 5)

# (**)
print(2 ** 8)
print(10 ** 5)
print(16 ** 3)
print(12 ** 4)
print(9 ** 3)



# 3)კომეტარებით ახსენით თუ რა განსხვავებაა /, //, და % მათემატიკურ ოპერატორებს შორის, 
# დაწერეთ რას აკეთებს თითოეული

# between operations like "/", "//" and "%" , difference is that 
#one is giving float division, it divides numbers and output their float result,
#  other is giving integer division , only remains decimal after divison
# and 3rd one is giving what is left after divison, for example: (10 % 3) result is 1





