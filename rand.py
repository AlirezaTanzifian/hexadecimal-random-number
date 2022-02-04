import random
chars = "0123456789ABCDEF"
length = 8
num = int(input("Please enter the number you want: "))
for i in range(num):
    res = "".join(random.choices(chars , k = length ))
    print(f"0x{res}")
input("Press any key to exit...")