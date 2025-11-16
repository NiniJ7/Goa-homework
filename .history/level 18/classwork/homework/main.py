# 2) for ციკლის საშვალებით დაბეჭდეთ რიცხვები 0-იდან 20-მდე, შეამოწმეთ თითოეული რიცხვი ლუწია თუ კენტი, თუ ლუწია დაბეჭდეთ "even" თუ კენტია დაბეჭდეთ odd და გვერდზე მიუწერეთ ეს რიცხვი თითოეულ შემთხვევაში

for num in range(0,21):
    if num % 2 == 0:
        print("even", num)
    else:
        print("odd", num)


# 3) while ციკლის საშვალებით დაბეჭდეთ რიცხვები 0-იდან 20-მდე, შეამოწმეთ თითოეული რიცხვი ლუწია თუ კენტი, თუ ლუწია დაბეჭდეთ "even" თუ კენტია დაბეჭდეთ odd და გვერდზე მიუწერეთ ეს რიცხვი თითოეულ შემთხვევაში

num = 0

while num <= 20:
    if num % 2 == 0:
        print("even", num)
    else:
        print("odd", num)
    num += 1


# 4) მომხმარებელს შემოატანინეთ სახელი და თუ ის თქვენს სახელს ემთხვევა დაბეჭდეთ "coincidence"

name = "Nini"
username = input("Enter the name: ")

if username == name:
    print("coincidence")


# 6) მოხმარებელს შემოატანინეთ გამოცდის ქულა და შეინახეთ score ცვლადში ინტეჯერად, თუ ქულა მეტია 70-ზე დაუბეჭდეთ რომ გამოცდა გადალახა "passed" სხვა შემთხვევაში კი რომ ჩაიჭრა "failed"

score = int(input("Enter the score: "))

if score >= 90:
    print("A")

elif score >=80:
    print("B")

elif score >=70:
    print("C")

elif score >=60:
    print("D")

elif score >=50:
    print("E")

else:
    print("F")


# 7) შექმენით პროგრამა რომელიც მომხმარებლისგან მიიღებს რიცხვს, შემდეგ დაადგენს დადებითია, უარყოფითი თუ ნული if-elif-else ის საშვალებით, თუ რიცხვი დადებითია შეამოწმეთ არის თუ არა ლუწი თუ არის დაბეჭდეთ "The number is positive and even." ხოლო სხვა შემთხვევაში დაბეჭდეთ "The number is positive and odd."

number = int(input("Enter the number: "))
if number > 0 and number % 2 == 0:
    print("The number is positive and even")
elif number > 0 and number % 2 != 0:
    print("The number is positive and odd")
else:
    print("The number is negative")


# 8) მომხმარებელს იქამდე შეეკითხეთ რიცხვები სანამ უარყოფით რიცხვს არ შემოიყვანს, while ციკლისა და input ინსტრუქციის საშვალებით, ასევე პირობითი განცხადებების დადებითობა/უარყოფითობის შესამოწმებლად, საბოლოოდ დაბეჭდეთ ყველა მიღებული დადებითი რიცხვის ჯამი

total = 0
number = int(input("Enter the number: "))
while number <= 0:
    continue
else:
    total += number

    print("The sum of positive numbers is", total)


# 9) შექმენით პროგრამა რომელშიც მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ უარყოფითს არ შეიყვანს. დაბეჭდეთ შეყვანილი ლუწი და კენტი რიცხვების რაოდენობა გამოიყენეთ პირობითი განცხადებები


even_numbers = 0
odd_numbers = 0

while True:
    number = int(input("Enter the number: "))

    if number <= 0:
        break

    if number % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print("Even numbers entered:", even_numbers)
print("Odd numbers entered:", odd_numbers)
