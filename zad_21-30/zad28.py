run = True
while run:
    word = input("wprowadź słowo\n")
    if len(word)<2:
        print("słowo musi być przynajmniej dwuliterowe!!")
    else:
        print("druda litera wyrazu to:", word[1])
        run=False

