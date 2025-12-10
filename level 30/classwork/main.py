# 1) შექმენით tuple, type ფუნქციის მეშვეობით დაბეჭდეთ მისი ტიპი და გამოიყენეთ 2 მეთოდი count, index. შექმენით ფუნქცია manual_count რომელიც მიიღებს 2 პარამეტრს: sequence, target და დათვლის მიმდევრობაში (სიმრვალეში) კონკრეტული ელემენტის რაოდენობას


print(sports.index[2])
print(sports.count[1])
print(type(sports))

sports = ("Basketball", "Tennis", "Football")

def manual_count(sequence,target):
    count = 0
    for element in sequence:
        if element == target:
            count += 1
        return count

result = manual_count(sports, "Tennis")
print(result)


