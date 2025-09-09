# Exercise 1
Donutsnumber = input("How many donuts do you have? ")
Donuts = int(Donutsnumber)
Dozens = Donuts // 12
print("You can only make", Dozens, "dozens with", Donuts, "donuts.")

# Exercise 2
a = input("Enter a number: ")
b = input("Enter another number: ")
A = int(a)
B = int(b)
residue = A % B
print("The residue of", A, "divided by", B, "is", residue)

# Exercise 3
# Write some code that asks the user a number of seconds
Seconds = input("Enter a number of seconds: ")
S = int(Seconds)
hours = S // 3600
minutes = (S % 3600) // 60
seconds = S % 60
print(S, "seconds is", hours, "hours,", minutes, "minutes and", seconds, "seconds.")



