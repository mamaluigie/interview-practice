import pdb
def palindrome(st):
    # pdb.set_trace()
    if len(st) == 0 or len(st) == 1:
        return True
    if st[0] == st[-1]:
        return palindrome(st[1:-1])
    else:
        return False

print(palindrome("racecar"))