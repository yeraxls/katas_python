def isPalindrome(x: int) -> bool:
    num = str(x)
    p = 0
    p2 = len(num) - 1
    while(p < p2):
        if num[p] != num[p2]:
            return False
        p +=1
        p2 -=1
    return True



result = isPalindrome(50605)
print(result)
# https://leetcode.com/problems/palindrome-number/discuss/3651712/2-method-s-c-java-python-beginner-friendly/