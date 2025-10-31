# 4) for ციკლისა და range-ის საშვალებით გამოიტანეთ რიცხვები
# 80 დან 90 მდე
#90 დან 80 მდე
#78 დან 94 მდე ლუწი

# (80 დან 90 მდე)
for num in range(80,90,):
    print(num)


#(90 დან 80 მდე)
for num in range(90,80,-1):
    print(num)


#(78 დან 94 მდე)
for num in range(78,94,2):
    print(num)


# bonus დავალება

read_pages = int(input("Enter the number of pages you read: "))
free_time = input("did you have any free time? (T or F)")

productive = read_pages >= 20 and free_time = True
print("productive =", productive)