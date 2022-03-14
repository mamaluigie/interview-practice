def countx(s):
    if s == "":
        return 0
    if s[0] == 'x':
        return countx(s[1:]) + 1
    else:
        return countx(s[1:])


print(countx("xhixx"))
