import pdb
def changePi(s):
    if s == "" or len(s) < 2:
        return s
    if s[:2].lower() == "pi":
        return "3.14" + changePi(s[2:])
    else:
        return s[0] + changePi(s[1:])

print(changePi("lmaopilolpi"))
