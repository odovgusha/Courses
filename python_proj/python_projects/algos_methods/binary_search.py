from random import randint
import sys

# A = list()



def BinarySearch(A,k):
    # A.sort()
    # print(A)
    l = 0
    r = len(A)-1
    # print(k,"before while")
    while l <= r:
        # print(l)
        m = int((l+r)/2)
        # print(m)
        # print(A[m], m, k,"outof")
        if A[m] == k:
            # print(A[m],"A[m]")
            # print(m)
            # return m
            # for 1 based indexation
            return m+1
        elif A[m] > k:
            # print("bigger")
            r = m - 1
            # print(r)
        else:
            # print("smaller")
            l = m + 1
            # print(l)
    # print(-1)
    return -1


#     A = [randint(0, 20) for p in range(0, 1000)]
#     k = 10
#     print(k)
#     A_srt = A.sort()
#     print(A_srt)
#     ans = BinarySearch(A_srt, k)
#     print(ans)





def main():

    # A = list([randint(0, 20) for p in range(0, 1000)])


    setup = list()
    for line in sys.stdin:

        setup.append(tuple(map(int, (line.split()))))


    # print(setup)
    # print(setup[0][1:])
    # print(setup[1])
    # print("test")
    # t_list = [1, 5, 8, 12, 13]
    # k_list = [8, 1, 23, 1, 11]

    t_list = list(setup[0][1:])
    k_list = list(setup[1][1:])


    # print(list(enumerate(t_list)))
    # tup_list = list(enumerate(t_list))
    # print(tup_list)
    # tup_list = sorted(tup_list, key=lambda x: x[1])
    # print(tup_list)
    # t_list.sort()
    # print(t_list)
    ans_l = list()
    # ans_orig_ix = list()


    for i in range(0, len(k_list)):
        # print(k_list[i])
        test = k_list[i]
        ans_l.append(BinarySearch(t_list, k_list[i]))
        ans_l[i]
        # print(BinarySearch(t_list, k_list[i]), k_list[i])
        # ans_l.append(BinarySearch(t_list, setup[0][i]))
        # print(BinarySearch(t_list, setup[0][i]), setup[0][i])
    # print(setup[0])
    # print(t_list)
    print(' '.join(map(str, ans_l)))
    # print(ans_l)
    # print(tup_list)
    # for i in range(0,len(ans_l)):
    #     print(tup_list[i][0])
        # ans_orig_ix.append(ans_l[i][0])
    # print(ans_orig_ix)
    # print(A[0])
    # print(len(A))
    # print(type(A))
    # k = 15
    # print(k)
    # A_srt = list(A.sort())
    # A_srt = sorted(A)
    # print(type(A_srt))
    # print(list(A_srt[0]))
    # ans = BinarySearch(A_srt, k)

    # print(ans,A_srt[ans] ,"gep")




    #print(gcd(a, b))

if __name__ == "__main__":
    main()