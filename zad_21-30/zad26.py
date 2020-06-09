word = input("wprowadź słowo")
word2 =""
for i in range(len(word)):
    word2 = word2+word[-i-1]

if word == word2:
    print("słowo jest palindromem.")
else:
    print("słowo nie jest palindromem.")