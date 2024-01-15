word = input()
upper_case = []

for i in range(0, len(word)):
    if word[i].isupper():
        upper_case.append(i)
print(upper_case)
