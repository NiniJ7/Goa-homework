# 2) დაწერე ფუნქცია, რომელიც ბეჭდავს "Hello, world!"

def greeting():
    print("Hello, world!")

greeting()

# 3) დაწერე ფუნქცია, რომელიც იღებს სახელს და ბეჭდავს "Hello, [სახელი]!"

def greet(name):
    print(f"Hello, {name}!")

greet("R")

# 4) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს

def sum_numbers(a, b):
    return a + b

result = sum_numbers(1, 2)
print(result)

# 5) დაწერე ფუნქცია, რომელიც იღებს ერთ რიცხვს და აბრუნებს "Even" თუ ლუწია, ან "Odd" თუ კენტია

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 6) დაწერე ფუნქცია, რომელიც იღებს სიის ელემენტებს და აბრუნებს მათ საშუალოს

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# 7) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს ამ სტრიქონის სიგრძეს

def string_length(text):
    return len(text)

# 8) დაწერე ფუნქცია, რომელიც იღებს სიას და აბრუნებს მას შებრუნებულ მდგომარეობაში

def reverse_list(a):
    return a[::-1]

# 9) დაწერე ფუნქცია, რომელიც იღებს სტრიქონს და აბრუნებს მას დიდ ასოებად გადაყვანილს

def uppercase(text):
    return text.upper()

# 10) დაწერე ფუნქცია, რომელიც იღებს ორ რიცხვს და აბრუნებს მათ შორის უმეტესს

def max(a, b):
    if a > b:
        return a
    else:
        return b

# 11) დაწერე ფუნქცია, რომელიც იღებს რიცხვს და აბრუნებს True თუ ის უარყოფითია, False თუ არა

def negative(number):
    return number < 0

