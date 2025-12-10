# 10) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები

pin = "1234"
attempts = 3

while attempts > 0:
    pincode = input("Enter the correct pin: ")

    if pincode == pin:
        print("Access granted")
        break
    else:
        attempts -= 1
        print("Incorrect pin, you have " + str(attempts) + "attempts left")

    if attempts == 0 and pincode != pin:
        print("Acces denied")


# 11) მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო

total = 0
count = 0

while True:
    number = int(input("Enter the number: "))
    if number == -1:
        break
else:
    average = total / count
    print("Average of entered numbers are:", average)
total += number
count += 1
