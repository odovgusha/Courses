def gcd(a, b):

    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd((a % b), b)
    if b >= a:
        return gcd(a, (b % a))


def computeGCD(x, y):
    while (y):
        x, y = y, x % y

    return x

#1653264 3918848

#3918848 1653264
#3918848 % 1653264
def main():
    a, b = map(int, input().split())
    print(computeGCD(a, b))
    #print(gcd(a, b))

if __name__ == "__main__":
    main()