# 2) შექმენით ფუნქცია greeting რომელიც დაბეჭდავს "Welcome"-ს, შემდეგ 3-ჯერ გამოიძახეთ, ახსენით რა არის ფუნქცია, რომელი ჩაშენებული ფუნქციები გაქვთ ნასწავლი და კომენტარებით დეტალურად დაწერეთ ფუნქციის შექმნის სინტაქსი

from turtle import *

def greeting():
    print("Welcome")

greeting()
greeting()
greeting()

# ფუნქციის შექმნის სინტაქსი
# 1. def
# 2. ფუნქციის სახელი
# 3. ფრჩხილები ()
# 4. ორწერტილი :
# 5. კოდის ბლოკი


def grade():
    score = int(input("Enter your score: "))
    if score > 50:
        print("Passed")
    else:
        print("Failed")    


# 3) შექმენით add რომელიც მიიღებს 2 რიცხვს პარამეტრად a,b და დაბეჭდავს მათ ჯამს, ფუქნცია გამოიძახეთ 3-ჯერ, განმარტეთ პარამეტრები და არგუმენტები კომენტარებით


def add(a,b):
    print(a + b)

add(224,9)
add(67,19)
add(44,98)

# არსებობს 2 ტიპის ფუნქცია

# string.lower() - ყველა ასოს აპატარავებს სტრინგში
# string.upper() - ყველა ასოს ადიდებს სტრინგში
# string.capitalize() - პირველ სიმბოლოს ტოვებს დიდს


# 4) დაბეჭდეთ 3 სხვადსხვა string რომელზეც გამოიყენებთ lower, upper, capitalize ფუქნციებს

print("fiRst".lower())
print("seCOnd".upper())
print("THIrd".capitalize())