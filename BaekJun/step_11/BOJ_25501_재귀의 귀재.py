# 함수 밖에서 변수를 설정하여 함수 안에서 값을 변경하려 하면 오류가 발생
# 하지만 함수 밖에서 리스트 즉, 참조 주소를 설정해 함수 안에서 변경하려고 하면
# 함수 안에서 주소를 참조하는 것이므로 오류가 발생 X

def recursion(s, l, r):
    cnt[0] += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(input())

for tc in range(1, t+1):
    cnt = [0]
    words = input()
    print(isPalindrome(words), cnt[0])