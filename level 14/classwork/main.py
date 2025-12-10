# for ციკლის სტრუქტურა
# 1. for
# 2. საიტერაციო ცვლადი
# 3. in ოპერატორი
# 4. მიმდევრობა
# 5. ორწერტილი
# 6. კოდის ბლოკი

# DRY - don't repeat yourself


i = 0
while i < 10:
    print(i)
    i = i + 1

    print("Loop ended")


    # pin code: 1234 | 123456

    pin_code = "4531"

    code = input("Enter pin code: ")

    while (code != pin_code):
        code = code = input("Enter pin code: ")

    print("Pin correct, Authorised!")

