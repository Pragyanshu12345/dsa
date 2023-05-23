""" CODE FOR THE STADNARD KEYPAD PROBLEM"""
Phone = ["", "", "ac", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
final = []
answer = []
DIGIT = "23"


def keypad(digits, i, phone, finalans, ans):
    """CHECKING FOR ALL POSSIBLE COMBINATION"""
    if i >= len(digits):
        ans.append(''.join(finalans))
        return
    curr= int(digits[i])
    val = phone[curr]
    k = len(val)
    for j in range(k):
        finalans.append(val[j])
        keypad(digits, i+1, phone, finalans.copy(), ans)
        finalans.pop()


keypad(DIGIT, 0, Phone, final, answer)
print(answer)
