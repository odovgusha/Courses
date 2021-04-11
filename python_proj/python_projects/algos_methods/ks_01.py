import sys
#print("test")




def printA(a):
    for row in a:
        for col in row:
            print("{:8.0f}".format(col), end=" ")
        print("")

#W, n = (10, 1)

#w_arr = [6,3,4,2]
#c_arr = [30,14,16,9]

#def KnapsackWithoutRepsBU(W,w_arr, c_arr):
def KnapsackWithoutRepsBU(W,w_arr):
    n = len(w_arr)
    #n = 1
    D = [[0 for i in range(n+1)] for j in range(W+1)]
    #print(D)
    for i in range(1,n+1):
        for w in range(1,W+1):
            #print(w,i)
            #if less than w = previous or zero
            D[w][i] = D[w][i-1]
            #print(w_arr[i-1],c_arr[i-1])
            #print(w_arr[i-1],w)
            #weight of the item <= cur slot number
            if w_arr[i-1] <= w:
                #print(w, i)
                #print(D[w][i])
                #print(D)
                #print(max(D[w][i], D[w - w_arr[i-1]][i-1] + c_arr[i-1]),"gepa max")
                #print((D[w][i], D[w - w_arr[i - 1]][i - 1] + c_arr[i - 1]), D[w - w_arr[i - 1]][i - 1],c_arr[i - 1] ,"gepa")
                #print((D[w][i], D[w - w_arr[i - 1]][i - 1] + c_arr[i - 1]),"gepa")
                #If you have price
                #D[w][i] = max(D[w][i], D[w - w_arr[i-1]][i-1] + c_arr[i-1])
                # If you have only the weight
                D[w][i] = max(D[w][i], D[w - w_arr[i - 1]][i - 1] + w_arr[i - 1])

                #printA((D))
                #print(D[w][i])
    #only last number
    return D[w][i]
    #return D

#print(KnapsackWithoutRepsBU(W,w_arr, c_arr))
#D = KnapsackWithoutRepsBU(W,w_arr, c_arr)
#print(D[4][1])



list_of_lists = list()
for line in sys.stdin:
    list_of_lists.append((line.split()))

#print(list_of_lists)
#print(list_of_lists)
bag_size = list(map(int, list_of_lists[0]))[0]
weights = list(map(int, list_of_lists[1]))
#print(bag_size)
#print(weights)
D = KnapsackWithoutRepsBU(bag_size,weights)
print(D)
#print("Done")
#LISBottomUp(numb_seq)

#ans, D, prev = LISBottomUp(numb_seq)
#print(ans)