PrimeSum = 2

for TestNum in range(3, 2000000):
    for Divisor in range(2, TestNum):
        if TestNum % Divisor == 0:
            break
        elif Divisor > TestNum / Divisor:
            PrimeSum += TestNum
            print(TestNum)
            print(PrimeSum)
            break

print(PrimeSum)
