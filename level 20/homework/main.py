# 2) შექმენით სია fruits = [ვაშლი, ბანანი, ატამი, მსხალი, ალუბალი] და დაბეჭდეთ მესამე ელემენტი

fruits = ["Apple", "Banana", "Peach", "Pear", "Cherry"]
print(fruits[2])

# 3) შექმენით სია numbers = [10, 20, 30, 40, 50], შეცვალეთ მეორე ელემენტი 25-ით და დაბეჭდეთ განახლებული სია

numbers = [10,20,30,40,50]
numbers[1] =  25
print("განახლებული სია: ", numbers)

# 4) მომხმარებლებს შეაყვანინეთ ინდექსი (0-დან 4-მდე) და დაბეჭდეთ შესაბამისი ელემენტი სიიდან colors = [წითელი, მწვანე, ლურჯი, ყვითელი, იასამნისფერი]

colors = ["red", "green", "blue", "yellow", "purple"]
my_index = int(input("Enter an index from 0 to 4: "))
print("Your color is: ", colors[my_index])

# 5) შექმენით სია animals = [ძაღლი, კატა, სპილო, ვეფხვი, ლომი], შეცვალეთ ბოლო ელემენტი გემით და დაბეჭდეთ სია

animals = ["dog", "cat", "elephant", "tiger", "lion",]
animals[4] = "ship"
print("განახლებული სია: ", animals)

# 6) მომხმარებლებს შეაყვანინეთ ინდექსი და ახალი ფერი, შეცვალეთ ამ ინდექსზე არსებული ფერი სიაში colors = [თეთრი, შავი, ნარინჯისფერი, ვარდისფერი] და დაბეჭდეთ განახლებული სია

colors = ["white", "black", "orange", "pink"]
index = int(input("Enter an index from 0 to 3: "))
new_color = input("Enter a new color: ")
colors[index] = new_color
print("განახლებული სია: ", colors)
