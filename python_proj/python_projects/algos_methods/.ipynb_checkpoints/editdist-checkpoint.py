def EditDistBU(A,B):
    n = len(A)
    m = len(B)
    D = [[0 for i in range(n)] for j in range(m)]
    for i in range(0,n):
        D[i,0] = i
    for j in range(0,m):
        D[0,j] = j
    for i in range(1,n):
        for j in range(1,m):
            c = diff()
            D[i,j] = min(D[i-1,j]+1,D[i,j-1]+1,D[i-1,j-1]+c)
    return D[n,m]
    



def main():
    a, b = map(int, input().split())
    print(EditDistBU(a, b))
    #print(gcd(a, b))

if __name__ == "__main__":
    main()