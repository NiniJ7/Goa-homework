# 2) შექმენით სია სადაც ჩამოწერეთ 4 ბოსტნეულს, შემდეგ თქვენთვის ყველაზე 2 არასასურველი ამ სიიდან ჩაანცვლეთ ახალი ელემენტებით

vegetables = ["Potato", "Cucumber", "Onion", "Broccoli", "Pepper"]

vegetables[3] = "Tomato"
vegetables[4] = "Eggplant"

print(vegetables)

#3) მომხმარებელს შემოატანინეთ რიცხვი 0-იდან 4-მდე და შეინახეთ ის "user_choice"-ის ცვლადში, შემდეგ ბოსტნეულსი სიიდან დაუბეჭდეთ ის ელემენტი რომელიც მომხმარებელმა აირჩია, ესეიგი იმ user_choice ინდექსზე მყოფი ელემენტი სიაში

user_choice = int(input("Enter the number(0 - 4): "))
vegetables = ["Potato", "Cucumber", "Onion", "Broccoli", "Pepper"]
print("Your vegetable is: ", vegetables[user_choice])

# 4) ახსენით რას ნიშნავს რომ list და string არის დალაგებული მიმდევრობები, კომენტარებით დაწერეთ მათ თვისებებს შორის განსხვავებები. მოიყვანეთ მაგალითები

# string - მას ვწერთ მხოლოდ სიმბოლოებით (""), არის უცვლელი ანუ immutable, 
# list - მასში ვწერთ ნებისმიერ ტიპს(რიცხვი,სიმბოლო,boolean), არის mutable განსხვავებით სტრინგისგან

# 5) ახსენით რა არის slicing
# slicing - არის ტექნიკა, რომელიც საშუალებას გვაძლევს დალაგებული ობიექტებიდან (string, list) ავიღოთ კონკრეტული ნაწილი ინდექსების დიაპაზონის გამოყენებით

# 6) შექმენით სია რომელშიც ჩამოწერეთ რიცხვებს 1-იდან 20-ის ჩათვლით. slicing-ის საშვალებით გამოიტანეთ რიხცები 5-იდან 10-მდე

numbers = list(range(1, 21))
print(numbers[4:10])

# 7) შექმენით სია ციური სხეულებზე სიტყვებით და შემდეგ გამოიტანეთ მხოლოდ ის ელემენტები, რომლებიც ლუწ ინდექსებზე დგანან

sky_objects = ["Moon", "Sun", "Stars", "Planets",  "Asteroids", "Commets"]
print(sky_objects[0::2])

# 8) შექმენით სია 0-დან 15-მდე რიცხვებით. გამოიტანეთ მხოლოდ ის რიცხვები, რომლებიც კენტ ინდექსებზე დგანან

numbers = list(range(0,16))
print(numbers[1::2])

# 9) შექმენით string რომელშიც შეინახავთ თქვენს სახელსა და გვარს, შემდეგ ცალ ცალკე გამოიტანეთ ამ სტრინგიდან ჯერ სახელი და შემდეგ გვარი slicing-ის საშვალებით

name = "Nini Jorbenadze"
print(name[0:4])
print(name[5:])

# 10) მომხმარებელს შემოატანინეთ სიტყვა, შემდეგ if-ით შეამოწმეთ ეს სიტყვა თუ თავისი თავის ტოლია როდესაც შემოაბრუნებთ (slicing-ის დახმარებით), თუ ასეა დაბეჭდეთ რომ განსაკუთრებული (ასეთ სიტყვებს palindrome ჰქვია) სიტყვაა, სხვა შემთხვევაში კი დაბეჭდეთ რომ ჩვეულებრივი სიტყვაა

word = input("Enter word: ")
reversed_word = word[::-1]
if word == reversed_word:
    print("ეს სიტყვა არის განსაკუთრებული(palindrome)")
else:
    print("ეს ჩვეულებრივი სიტყვაა")


# 11) შექმენით სიტყვების სია, შემდეგ მის შემობრუნებულ ვერსიას გადაუარეთ for ციკლით, დაბეჭდეთ ყოველი მეორე ელემენტი (რომ გაიგოთ ყოველი მეორე აიღეთ ცვლადი რომელიც თავიდან 0 იქნება, ყოველ გამეორებაზე კი გაზრდით ერთით და შეამოწმეთ ლუწია თუ კენტი)

words = ["ball", "boat", "hand", "head", "doll", "country", "world"]
reversed_words = words[::-1]

counter = 0
for word in reversed_words:
    if counter % 2 == 0:
        print(word)
        counter += 1


# 12) მომხმარებელს შემოატანინეთ სიტყვა და დაბეჭდეთ ის შებრუნებულად

word = input("Enter word: ")
reversed_word = word[::-1]
print(reversed_word)


# 13) შექმენით ცვლადი რომელშიც შეინახავთ თქვენთვის სასურველ string-ს, უნდა იყოს მინიმუმ 20 სიმბოლო, შემდეგ slicing-ის საშვალებით დაბეჭდეთ ეს string ხუთგვარად შემდეგი პირობებით:

string = "Football is the best sport"

print("Fist 5 symbols: ", string[:5])
print("Last 4 symbols: ", string[-4:])
print("From 4th to 10th symbols: ", string[3:10])
print("Reverse whole string: ", string[::-1])
print("String on every 2nd symbol: ", string[::2])