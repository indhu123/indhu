import math
n = int(input())
decimal = 0
remainder = 0
i = 0
while (n!=0):
    remainder = n%10
    n = int(n / 10)
    decimal = decimal + remainder*math.pow(2,i)
    i = i + 1
print(int(decimal))
