my_tuple = ("Adam", "Wiesław", "Grażyna", "Janusz", "Sebastian")

iterator = iter(my_tuple)
for i in range(len(my_tuple)):
    print(iterator.__next__())