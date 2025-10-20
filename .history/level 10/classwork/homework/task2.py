# შექმენით 30 მაგალითი შედარების ოპერაციებზე (>, <, >=, <=, ==, !=), გამოიყენეთ სხვადასხვა ტიპის მნიშვნელობები (რიცხვები, სტრინგები, ცვლადები). თითოეულ მაგალითში კომენტარით მიუწერეთ, რას აბრუნებს (True ან False) და რატომ მაგალითად, თუ ობიექტები განსხვავებული ტიპისაა, ახსენით როგორ იქნა შედარებული. ეცადეთ, რომ მაგალითები არ გამეორდეს და მოიცავდეს სხვადასხვა სიტუაციებს (მათ შორის ცვლადების გამოყენებასაც)

a = 4
b = 12
c = "Nini"
d = "17"
e = 2,7

# int comparisons
print(12 > 4) #True
print(-2 >= 4) #False
print(27 <= 56) #True
print(-12 < 4) #True
print(4 == 4) #True
print(-7 != -7) #False

# float comparisns
print(1.2 > 1.1) #True
print(-2.5 >= -2) #False
print(0.5 <= 1/2) #False
print(1.0 < 4.1) #True
print(0,5 == 1/2) #True
print(1.5 != 3/2) #False

# Mixed variable comparisons
print(b > a) #True
print(a >= b) #False
print(b <= 20) #True
print(a < 8) #True
print("Nini" == 'Nini') #True
print(e != 2,7) #False