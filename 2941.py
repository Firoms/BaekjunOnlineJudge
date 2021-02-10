a = input()
length = 0
li = ["=", "-", "j"]
for i in range(len(a)):
    if a[i] in li:
        length -= 1
        try:
            if a[i] == "=" and a[i - 2] == "d" and a[i - 1] == "z":
                length -= 1
        except:
            pass
        try:
            if a[i] == "j":
                if a[i - 1] == "l" or a[i - 1] == "n":
                    pass
                else:
                    length += 1
        except:
            pass
    length += 1
print(length)
