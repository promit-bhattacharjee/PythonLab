A, B = map(int, input().split())
carry = 0

while A > 0 or B > 0:
    digit_A = A % 10
    digit_B = B % 10

    if digit_A + digit_B + carry >= 10:
        print("Yes")
        break

    carry = (digit_A + digit_B + carry) // 10
    A //= 10
    B //= 10
else:
    print("No")
