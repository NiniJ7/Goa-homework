pin_codes = ["2323", "7777", "1234", "0017"]

your_pin = (input("Enter the pincode: "))
pin_found = False

for saved_pincodes in pin_codes:
    if your_pin == saved_pincodes:
        print("Correct pin")
        pin_found = True
        break
    

Fruits = ["Apple", "Banana", "Grapes"]

your_fruit = int(input("1 - Apple\n 2 - Banana\n 3 - Grapes"))
index = your_fruit - 1

print("Your choice is: ", Fruits[index] )

