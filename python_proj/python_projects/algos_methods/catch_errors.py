import sys

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError(str(x) + " is less than 0")
        return 
        

def main():
    a = int(str(sys.stdin.readline()).rstrip())
    #a = int(map(int, input().split())
    #print(a)
    #x = PositiveList([1,2,3])
    x.append(a)
    print(x)

#if __name__ == "__main__":
#    main()