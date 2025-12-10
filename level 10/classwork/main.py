height = float(input("Enter your height: "))
years = int(input("Enter your age: "))
eh = height + (years * 0,5)
print(eh)

# implicit data conversion - ბუნბერივი (თავისთავად) მონაცემთა ტიპის შეცვალა
# print(10 / 2)

# explicit data conversion - ხელონვური (ჩვენით) მონაცემთა ტიპის შეცვალა
# int('2')
# float('2.3')
# str(5)

# Comparsion operations
# boolean - მონაცემთა ტიპი ორი შესაძლო მნიშვნელობით: True ან False 
#print(type(True))
# print(type(False))

# შეადრების ოპერაციის შედეგი ერის ყოველთვის boolean მონაცემთა ტიპის მნიშვნელობა

print(5 > 2) # True
print(4 < 3) # False
print(9 == 8) # False
print(4 >= 4) # True
print(12 <= 11) # False


# Logical operations: and, or, not

# Or
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) #False

# and
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False

# Not
print(not True) #False
print(not False) #True



# range(start, stop, step) - ინსტრუქცია რომელიც იღებს 3 მნიშვნელობას, საწყის პოზიციას რომელსაც იქამადე უმატებს ნაბიჯს (მესამე მნიშვნელობას რასაც გადავცემთ) სანამ არ გახდება საბოლოო მნიშვნლობის ესეიგი stop-ის (მეორე) ტოლი. თუ მხოლოდ 1 მნიშვნელობა გადავეცით range-ს მაშინ ეს ჩაითვლება stop-ად, ხოლო საწყისი იქნება 0. თუ 2 მნიშვნელობა გადავეცი პირველი იქენება საწყისი, მეორე კი საბოლოო, ნაბიჯი (step) ჩაითვლება 1


# Sequencing - მიმდევრობა
print("1")
print("2")

# Iteration - გამეორება
print("Nini")

# for -ციკლი მეშვეობით შეგვიძლია განვიხილოთ რაიმე მიმდევრობა
# for ციკლის ინიციალიზებისას იქმნება საიტერაციო ცვლადი
# რომელიც ამ მიმდევრობის ყველა წევრის მნიშვნელობას მიიღებს

# 0, 1, 2, 3, 4, 5
for num in range(20):
    print(num)


# 3) for და range-ის გამოყენებით გამოიტანეთ შემდეგი რიცხვების მიმდევრობები:

#1-იდან 20-ის ჩათვლით ლუწები
#30-იდან 5-მდე ყველა
#25-იდან 40-მდე კენტი რიცხები

for num in range(0,21,2):
    print(num)

for num in range(30,5, -1):
    print(num)

for num in range(25,41,2):
    print(num)   