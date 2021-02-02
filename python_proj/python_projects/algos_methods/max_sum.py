import math
import sys




def max_el_sum(num):
    # n = int(input("Please enter your int: "))
    # eq = f"X^2 + X - {n} = 0 "
    # if num < 6 or num > 3:
    #     x = math.sqrt((num))
    # else:

    # x = math.sqrt((num))


    x = (math.sqrt(1+(4*num*2))-1)/2


    r_x = int(x)

    sum_nat = ((r_x * r_x) + r_x) / 2

    nat_sum_arr = list(range(1, r_x + 1))

    arr_sum = nat_sum_arr
    arr_sum[-1] = int(arr_sum[-1] + (num - sum_nat))


    # print(len(arr_sum))
    # print(*arr_sum, sep=' ')

    return (arr_sum)





def main():
    inp_num = int(sys.stdin.readline())
    sum_arr = max_el_sum(inp_num)
    print(len(sum_arr))
    print(*sum_arr, sep=' ')


if __name__ == "__main__":
    main()
