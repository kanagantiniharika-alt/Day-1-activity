num = int(input("Enter number: "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print("Palindrome Number")
else:
    print("Not Palindrome Number")