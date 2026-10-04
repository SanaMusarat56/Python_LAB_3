try:
    num = int(input("Number likho: "))
    print(10 / num)
except ZeroDivisionError:
    print("Zero se divide nahi kar sakte!")
except ValueError:
    print("Sirf number likho!")