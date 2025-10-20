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


# Logical operations
print(True or True)
print(True or False)
print(False or True)
print(False or False)

