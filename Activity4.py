text = input("Enter string: ")

longest = ""

for i in range(len(text)):
    temp = ""

    for j in range(i, len(text)):
        if text[j] not in temp:
            temp = temp + text[j]
        else:
            break

    if len(temp) > len(longest):
        longest = temp

print("Longest substring:", longest)
print("Length:", len(longest))