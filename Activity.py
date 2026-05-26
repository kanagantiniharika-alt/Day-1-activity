def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


num = int(input("Enter number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    total = total + factorial(digit)
    temp = temp // 10

if total == num:
    print("Strong Number")
else:
    print("Not Strong Number")