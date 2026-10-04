try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print(file.read())
    file.close()
finally:
    print("End of the program")