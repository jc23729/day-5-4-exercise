#Write your code below this row 👇

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("Fizzbuzz")
    #Divisible by 3
  elif number % 3 == 0:
    print("Fizz")
    #Divisible by 5
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)