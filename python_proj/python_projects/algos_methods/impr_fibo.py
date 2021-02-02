import time



# n = int(input())
# lastNum = n
# F_arr = [0] * (lastNum+1)
# F_arr[0] = 0
# F_arr[1] = 1
#
# for n in range(2, lastNum+1):
#     F_arr[n] = F_arr[n - 1] + F_arr[n - 2]
#
#
# print(F_arr[lastNum])

def fib_mod(n, m):

    lastNum = n
    F_arr = [0] * (lastNum + 1)
    mod_arr = [0%m, 1%m]
    F_arr[0] = 0
    F_arr[1] = 1
    period = 1
    if lastNum < 2:
        print(lastNum)

    for n in range(2, lastNum + 1):
        F_arr[n] = F_arr[n - 1] + F_arr[n - 2]
        mod_arr.append(F_arr[n]%m)
        # print(mod_arr[n])
        if mod_arr[n] == 1 and mod_arr[n-1] == 0:
            period = len(mod_arr) - 2
            break


    # return period
    return mod_arr[n%period]



def fib_digit(n):
    lastNum = n

    F_arr = [0] * (lastNum + 1)
    F_arr[0] = 0
    F_arr[1] = 1

    for n in range(2, lastNum + 1):
        # F_arr[n] = F_arr[n - 1] + F_arr[n - 2]
        F_arr[n] = (F_arr[n - 1] + F_arr[n - 2]) % 10
    return F_arr[lastNum]



def fib(n):
    lastNum = n

    F_arr = [0] * (lastNum + 1)
    F_arr[0] = 0
    F_arr[1] = 1

    for n in range(2, lastNum + 1):
        F_arr[n] = F_arr[n - 1] + F_arr[n - 2]
        # F_arr[n] = (F_arr[n - 1] + F_arr[n - 2]) % 10
    return F_arr[lastNum]

def fib_arr(n):
    lastNum = n

    F_arr = [0] * (lastNum + 1)
    F_arr[0] = 0
    F_arr[1] = 1

    for n in range(2, lastNum + 1):
        F_arr[n] = F_arr[n - 1] + F_arr[n - 2]
        # F_arr[n] = (F_arr[n - 1] + F_arr[n - 2]) % 10
    return F_arr


def main():
    # n = int(input())
    n, m = map(int, input().split())
    # start_time = time.time()
    print(fib_mod(n, m))
    # for i in fib_arr(n):
    #     print(i%4)
    # print(fib_arr(n))
    # print(fib_digit(n))
    # print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()









