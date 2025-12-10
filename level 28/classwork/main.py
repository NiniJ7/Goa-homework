# ფუნქცია - ხელახლა გამოყენბადი კოდის ბლოკი

# def greeting(first_name, last_name):
#     print("Hello " + first_name + " " + last_name)

# greeting("Luka", "Gurgenidze")


# list.append(element) - ელემენტს ამატებს სიის ბოლოს
# nums.append(50)
# nums.append("wrtye")

# list.insert(index, element) - ელემენტს ამატებს სიაში მოცემულ ინდექსზე
# nums.insert(2, "25")

# list.extend(sequence) - ცალცალკე ამატებს დალაგებული მონცამეთა ტიპის წევრებს სიაში
# nums.extend([70, 75, 80])

# list.pop(index) - შლის მოცემულ ინდექსზე მყოფ ელემენტს
# nums.pop() - ბოლო ელემენტს წაშლის

# nums.remove(value) - წაშლის სიიდან კონკრეტულ მნიშვნლობას
# nums.remove(30)

# range(4) - 0, 1, 2, 3

# odds = []

# for index in range(len(nums)):
    
#     if index % 2 == 1:
#         odds.append(nums[index])

# nums = [55, 12, 25, 26, 26, 3246, 34]

# list.sort() - ზრდადობით ალაგებს რიცხვებს და სტრქიონებს ანბანის მიხედვით, ცვილს გადაცემულ სიას
# sorted(list) - ანალოგიურად ახარისხებს სიას, ოღონდ არ ცვლის თავდაპირველ სიას და გვაძლევს ახალ სიას

# print(nums)


# 1) თითოეულ განხილულ მეთოდებზე len, append, insert, extend, pop, remove, sort, sorted შეასრულეთ 3-3 მაგალითი

nums = [7, 10, 35, 99, 50]

nums.append(1)
nums.append("3")
print(nums)

nums.sort()
print(nums)

nums.pop(2)
print(nums)

nums.remove(7)
print(nums)

nums.extend([20,30,50])
print(nums)

# 2) შექმენით ფუნქცია welcome, რომელიც მიიღებს პარამეტრებად first_name, last_name. თქვენი დავალება დააბრუნოთ მნიშვნელობა: "Hello <first_name> <last_name>". კომენტარებით ახსენით რა არის return და რით განსხვავდება print-ისგან

def welcome(first_name, last_name):
    return "Hello" + first_name + " " + last_name

    print(welcome(Nini, Jorbenadze))

