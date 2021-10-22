def convert(num, base=10, n2b=True):
    binary = ""
    if n2b:
        if base==10:
            while num>=2:
                binary = str(num%2) + binary
                num = num//2
                print(str(num))
            if num == 1:
                binary = "1"+binary
    return binary

num = int(input("Num: "))
print(str(convert(num)))
