# 1) შექმენით სია რომელშიც ჩამოწერთ თქვენთის ნაცნობ პროგრამირების ენებს, უნდა იყოს მინიმუმ 10 ელემენტი, ჯერ დაბეჭდეთ მთლიანად სია, შემდეგ კი მისი ელემენტები ცალცალკე ინდექსის გამოყენებით, კომენტარებით დაწერეთ თუ რა არის ინდექსი თქვენი აზრით

programming_languages = ["PY", "HTML", "CSS", "JS", "C#", "C++", "Java"]

print(programming_languages[0])
print(programming_languages[1])
print(programming_languages[2])
print(programming_languages[3])
print(programming_languages[4])
print(programming_languages[5])
print(programming_languages[6])
print(programming_languages)

# index - ელემენტის პოზიცია სიაში, ელემენტის პოზიცია იწყება 0 დან

# 2) შექმენით ცივი სასმელის სია, მომხმარებელს შემოატანინეთ ინდექსი და გამოუტანეთ ამ სასმელებიდან იმ ინდექსზე მყოფი ელემენტი რომელსაც შემოიტანს, შედეგ შეცვალეთ ეგ ელემენტი ახალი პროდუქტი, ასევე შეცვალეთ სიის მეორე ელემენტი, ახსენით რას ნიშნავს რომ სია არის დალაგებული მიმდევრობა კომენტარებით, შექმენით ახალი რიცხვების სია (10 ელემენტით), შემდეგ for ციკლითა და range ინსტრუქციის გამოყენებით იტერაცია მოახდინეთ ისეთ დიაპოზნზე რომელიც იქნება თქვენი რიცხვების სიის შესაბამისი (ესეიგი range-ში ჩაწერეთ სიის ელემენტების რაოდენობა) და ყოველ სიის ელემენტს მოუმატეთ ერთი გარდა მე-5 ელემენტისა

cold_drinks = ["Cola", "Fanta", "Sprite", "Icecoffee", "Icetea", "water"]

print("cold drinks: ", cold_drinks)

index = int(input("Enter an index from 0 to 5: "))
print("Your drink is: " , cold_drinks[index])

cold_drinks[index] = "Pepsi"
print("replace element at the chosen index:", cold_drinks)

cold_drinks[1] = "Orange juice"
print("replace element at the second index:", cold_drinks)

numbers = [0,1,2,3,4,5,6,7,8,9,]

for i in range(10):
    if i == 3:
        continue
    numbers[i] += 1
    
    print(numbers)

