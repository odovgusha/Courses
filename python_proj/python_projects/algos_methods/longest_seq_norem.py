import sys
print("test")

# A = list([1,2,3,4,5,6])
#A = list([7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1])
#A = list([1,2,3,7,8,5,4,2,9])
#A = list([3,3,3,3,3,6,6,6,6,9,9,9])


def LISBottomUp(A):
    D = [1] * len(A)
    prev = [-1] * len(A)
    # print(D)
    for i in range(0, len(A)):
        for j in range(0, i):
            if A[j] <= A[i] and A[i] % A[j] == 0 and (D[j] + 1) > D[i]:
            #if A[j] < A[i]  and (D[j] + 1) > D[i]:
                D[i] = D[j] + 1
                prev[i] = j
                # prev[i] = j + 1
    ans = 0
    for i in range(0, len(A)):
        ans = max(ans, D[i])
    return (ans, D, prev)



# print(list(range(10,-1,-1)))
#print(A)
#print(D)
def LISBottomUp_Lans(A, D, ans):
    k = ans
    L_ans = [0] * ans
    for i in range(len(D) - 1, -1, -1):
        if D[i] == k:
            #print(D[i])
            L_ans[k-1] = A[i]
            k -= 1
    return L_ans

#print(L_ans)
#print(A)
#print(D)
#A = list([3,6,7,12])
#ans, D, prev = LISBottomUp(A)
#print(LISBottomUp_Lans(A, D, ans),"answer")


# print(list(range(0,10)))
#L = list(range(0, ans))
#k = 1
#for i in list(range(1, len(A))):
#    if D[i] > D[k]:
#        k = i
#print(k)
#j = ans - 1
#while k > -1:
#    L[j] = k
#    j = j - 1
#    k = prev[k]


list_of_lists = []


for line in sys.stdin:
    list_of_lists.append((line.split()))

#print(list_of_lists)
numb_seq = list(map(int, list_of_lists[1]))
#print(numb_seq)
#print("Done")
#LISBottomUp(numb_seq)

ans, D, prev = LISBottomUp(numb_seq)
print(ans)