# 1) მოხმარებელს შემოატანინეთ 2 რიცხვი, start და end. თქვენი ამოცანაა რომ start-იდან end-ის ჩათვლით გამოიტანთ ყველა რიცხვის ჯამი და დაბეჭდოთ შედეგი ერთხელ. ასევე შექმენით name ცვლადი, რომელშიც შეინახავთ თქვენს სახელს და გადაურეთ for ციკლით, გამოიტანეთ თითოეული სიმბოლო ცალცალკე

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

total = 0
for num in range(start,end+1):
    total += num
    print("total is: " , total)

    name = "Nini"
    for i in name:
        print(i)
