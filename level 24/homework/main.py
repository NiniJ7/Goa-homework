# 2) დაწერეთ პროგრამა რომელიც ითხოვს ორ რიცხვს მომხმარებლისგან შემოაყვანინეთ დაწყებისა და დასრულების რიცხვი თუ მეორე რიცხვი ნაკლებია პირველზე დაბეჭდეთ არასწორი შუალედი სხვა შემთხვევაში დაბეჭდეთ ყველა რიცხვი შუალედში და იპოვეთ ამ რიცხვების ჯამი გამოიყენეთ for input int if else და sum

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
if end < start:
    print("არასწორი შუალედი")
else:
    numbers = []
    for i in range(start, end + 1 ):
      numbers.appeard(i)
    print(i)

    total = sum(numbers)
    print(total)


# 3) დაწერეთ პროგრამა რომელიც სთხოვს მომხმარებელს სამი რიცხვი და დაბეჭდავს ამ სამი რიცხვიდან მინიმალურ მნიშვნელობას გამოიყენეთ min და input int

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

minimum = min(a,b,c)
print("Minimum is: ", minimum)

# 4) დაწერეთ პროგრამა რომელიც იღებს ოთხ რიცხვს მომხმარებლისგან და პოულობს მაქსიმალურ მნიშვნელობას გამოიყენეთ max input და int

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter forth number: "))

maximum = max(a,b,c,d)

print("Maximum is: ", maximum)


# 5) შექმენით პროგრამა სადაც მითითებული იქნება რიცხვების სია პროგრამამ უნდა გამოთვალოს ამ სიის ჯამი და დაბეჭდოს გამოიყენეთ sum

numbers = [7,8,9,4,3]
total = sum(numbers)
print("Total sum is: ", total)


# 6) დაწერეთ პროგრამა რომელიც ითვლის რამდენი ელემენტი აქვს წინასწარ შექმნილ სიას გამოიყენეთ len და დაბეჭდეთ შედეგი

numbers[9,2,3,1,5,6]
count = len(numbers)

print("The count of list of numbers are:", count)

# 7) შექმენით პროგრამა რომელიც გამოითვლის რიცხვის კვადრატს math.pow ფუნქციით მომხმარებელს შემოაყვანინეთ ერთი რიცხვი და დაბეჭდეთ pow შედეგი

import math

number = int(input("Enter the number: "))
result = math.pow(number,2)

print("Square of the number is: ", result)

# 8) შექმენით პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ რიცხვზე ამოიღებს კვადრატულ ფესვს გამოიყენეთ math.sqrt და input int

import math

number = int(input("Enter the number: "))
result = math.sqrt(number)

print("Square root of this number is: ", result)


# 9) დაწერეთ პროგრამა რომელიც მომხმარებლის მიერ შეყვანილ ათწილადს დაჯამრავლებს math.floor და math.ceil ფუნქციებით და დაბეჭდავს ორივე შედეგს

import math
number = float(input("Enter the number: "))

floor = number * math.floor(number)
ceiled = number * math.ceil(number)

print(floor)
print(ceiled)

# 10) შექმენით პროგრამა რომელიც ბეჭდავს 5 შემთხვევით რიცხვს 1 დან 50 მდე გამოიყენეთ random.randint და მიღებული რიცხვებიდან იპოვეთ მინიმუმი და მაქსიმუმი min max

import random

numbers = []
for numbers in range(5):
    numbers.append(random.randint(1,50))

    print("Random numbers: ", numbers)

    minimum = min(numbers)
    maximum = max(numbers)

    print(minimum)
    print(maximum)

# 13) დაწერეთ პროგრამა სადაც მომხმარებელი შეიყვანს ორ რიცხვს და პროგრამა დაბეჭდავს რომელი მათგანია მეტი გამოიყენეთ max

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

maximum = max(a,b)
print("მეტია რიცხვი: ", maximum)

# 15) შექმენით პროგრამა რომელიც ითხოვს ერთ რიცხვს და math.pow გამოყენებით გამოუტანს ამ რიცხვის კუბს ანუ მესამე ხარისხს

import math

number = int(input("Enter the number: "))
cube = math.pow(number, 3)

print("რიცხვის კუბი არის: ", cube)

# 12) შექმენით პროგრამა რომელიც აგენერირებს შემთხვევითი რიცხვების სიას 5 ელემენტით გამოიყენეთ random.randint და ბოლოს დაითვალეთ ამ სიის სიგრძე და ჯამი len sum

import random

number = []
for _ in range(5):
    numbers.append(random.randint(1,100))

    print("Random numbers: ", numbers)

    length = len(numbers)
    total = sum(numbers)

    print("Length of numbers: ", length)
    print("sum of numbers: ", total)