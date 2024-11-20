word = str(input("Enter word: "))
l = len(word)

j = int(l/2)
k = 0
for i in range(j):
    if word[i] == word[l-1-i]:
        k+=1
    else:
        break
if k == j:
    print(word, " is palindrom")
else:
    print(word, " is not polindrom")
