import random

greaterThan = float(input("Your number will be greater than: "))
lessThan = float(input("Your number will be less than: "))
digits = int(input("Your number will that many decimal digits: "))
count = int(input("How many random numbers to generate: "))

for i in range(0,count):
    rounded_number = round(random.uniform(greaterThan, lessThan), digits)
    print(rounded_number)
