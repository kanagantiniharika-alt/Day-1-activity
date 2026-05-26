text = input("Enter string: ")

result = ""

for ch in text:
    found = False

    for r in result:
        if ch == r:
            found = True
            break

    if found == False:
        result = result + ch

print("After removing duplicates:", result)