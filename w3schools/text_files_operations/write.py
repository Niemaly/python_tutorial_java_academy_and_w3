f = open("demofile.txt", "r")
try:
    f.write("Lorum Ipsum2")
except Exception as e:
    print(e)
    print("Something went wrong when writing to the file")
finally:
    print(f.read())
    f.close()