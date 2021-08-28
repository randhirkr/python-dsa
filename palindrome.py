strlist = ['redivider', 'deified', 'civic', 'radar', 'madam','examples',
           'reviver','racecar', 'referrer']

# strlist = ['refer','abc','madam', "safadsa"]

# function to check is string is palindrome
def isPalindrome(st):
    strlen = len(st)

   # rangelenth : No of times loop will run to check if string is palindrome
   # get rangelenth depending upon whether string len is odd/even
    if (strlen % 2) == 0:
        rangelen = strlen // 2
    else:
        rangelen = (strlen + 1) // 2

    n = len(st) - 1

    isMatching = False
    for i in range(rangelen):
        if st[i] == st[n - i]:
            isMatching = True
            continue
        else:
            isMatching = False
            break

    return isMatching


for s in strlist:
    is_palin = isPalindrome(s)
    if is_palin:
        print(s, 'is palindrome')
    else:
        print(s, 'is NOT palindrome')