# 2) შემოიტანეთ სიტყვა input-ით და დაბეჭდეთ ის პატარა ასოებით

word = input("Enter a word: ")
print(word.lower())

# 3) შემოიტანეთ ორი სიტყვა და შეადარეთ (print(word1 == word2) ისე, რომ არ ჰქონდეს მნიშვნელობა ასოების სიდიდეს (გამოიყენეთ lower)

word1 = input("Enter a first word: ")
word2 = input("Enter a second word: ")

print(word1.lower() == word2.lower())

# 4) მოცემული სიაა: ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]. ყველა ელემენტი გადააკეთეთ პატარა ასოებად და დაბეჭდეთ (გამოიყენეთ for ციკლი)

countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for i in countries:
    print(i.lower())


# 5) შემოიტანეთ სიტყვა input-ით და დაბეჭდეთ დიდი ასოებით

word = input("Enter a word: ")
print(word.upper())

# 6) მოცემული სიაა: ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]. ყველა ქვეყანა გადააკეთეთ დიდი ასოებად და დაბეჭდეთ

countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for i in countries:
    print(i.upper())


# 7) შემოიტანეთ სიტყვა input-ით და შეამოწმეთ, არის თუ არა ის მთლიანად დიდი ასოებით

word = input("Enter a word: ")

if word == word.upper():
    print("Right")
else:
    print("Wrong")

# 8) შემოიტანეთ წინადადება input-ით და გამოიყენეთ capitalize ისე, რომ მხოლოდ პირველი ასო დარჩეს დიდი

sentence = input("Enter the sentence: ")
print(sentence.capitalize())

# 9) მოცემული სტრინგია "gEoRGia". გადააკეთეთ ისე, რომ მხოლოდ პირველი ასო იყოს დიდი, დანარჩენი კი პატარა

word = "gEoRGia"
print(word.capitalize())

# 10) მოცემული სიაა: ["georgia", "aRMENIA", "greeCE"]. ყველა ელემენტს ჯერ გაუკეთეთ lower, შემდეგ capitalize და დაბეჭდეთ

countries = ["georgia", "aRMENIA", "greeCE"]
for i in countries:
    print(i.lower().capitalize())

# 11) შემოიტანეთ სიტყვა input-ით და მოძებნეთ ასო a-ს პირველი პოზიცია

word = input("Enter a word: ")
print(word.find('a'))

# 12) მოცემული სტრინგია "I visited Georgia, Armenia and Greece". მოძებნეთ Armenia და დაბეჭდეთ მისი პოზიცია

text = "I visited Georgia, Armenia and Greece"
print(text.find("Armenia"))

# 13) შექმენით სტრინგი და შემოიტანეთ საძიებელი სიტყვა input-ით. თუ სიტყვა მოიძებნება find-ით, დაბეჭდეთ პოზიცია, სხვა შემთხვევაში კი დაბეჭდეთ word not found

text = "Real Madrid is the best football club"
word = input("Enter a word: ")

if text.find(word) != -1:
    print(text.find(word))
else:
    print("Word not found!")