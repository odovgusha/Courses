import sys

def LISBottomUp(A):
    D = [1] * len(A)
    prev = [-1] * len(A)
    # print(D)
    for i in range(0, len(A)):
        for j in range(0, i):
            if A[j] >= A[i]  and (D[j] + 1) > D[i]:
            #if A[j] < A[i]  and (D[j] + 1) > D[i]:
                D[i] = D[j] + 1
                prev[i] = j
                # prev[i] = j + 1
    ans = 0
    for i in range(0, len(A)):
        ans = max(ans, D[i])
    return (ans, D, prev)

def LISBottomUp_Lans(A, D, ans):
    k = ans
    L_ans = [0] * ans
    for i in range(len(D) - 1, -1, -1):
        if D[i] == k:
            #print(D[i])
            L_ans[k-1] = A[i]
            k -= 1
    return L_ans



list_of_lists = []


for line in sys.stdin:
    list_of_lists.append((line.split()))

numb_seq = list(map(int, list_of_lists[1]))

ans, D, prev = LISBottomUp(numb_seq)
print(ans)

k = ans
L_ans = [0] * ans
for i in range(len(D) - 1, -1, -1):
    if D[i] == k:
        # print(D[i])
        L_ans[k - 1] = i + 1
        #L_ans[k-1] = numb_seq[i]
        k -= 1
#print(L_ans)
print (' '.join(map(str, L_ans)))
