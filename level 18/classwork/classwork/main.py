# 1) სტუდენტს შემოტანინეთ გამოცდის ქულა, გარდაქმენით ინტეჯერად და შეინახეთ score ცვლადში, შემდეგ შეამოწმეთ if პირობითი განცხადების გამოყენებით თუ ქულა მეტია ან ტოლი 50-ის მაშინ დაუბეჭდეთ exam passed და ბოლოს ამ პირობითი განცხადების დამოუკიდებლად დაბეჭდეთ student graded

#score = int(input("Enter the exam score: "))
#if score >= 50:
#    print("exam passed")

#print("student graded")


# 2) მიიღეთ მოსწავლის ქულა 0-იდან 100-მდე input-ით შემდეგ კი შეაფასეთ if-elif-else ბლოკის მეშვეობით ამ სკლაის მიხედვით

score = int(input("enter the score: "))

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


#3) for ციკლით განიხილეთ რიცხვები 30-იდან 60-მდე და დაბეჭდეთ ყველა გარდა 50-ისა (ამისთვის შეამოწმეთ რიცხვი ხომ არ უდრის 50-ს და თუ უდრის continue მეშვეობით გამოტვეთ ეს იტერაცია ანუ გამეეორება) ხოლო თუ რიცხვი უდრის 55-ს მაშინ შეწყვიეთ ციკლი (if-ით შეამომწეთ და გამოიყენეთ break keyword)

for num in range(30, 60):
    if num == 50:
        continue
    if num == 55:
        break