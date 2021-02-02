import sys


def main():
    setup = list()
    for line in sys.stdin:
        setup.append(tuple(map(str, (line.split()))))
    #print(setup)
    num_comp = int(setup[0][0])
    #print(setup[num_comp+1][0])
    parents = {"obj" : []}

    for i in range(1, num_comp+1):
        if len(setup[i]) == 1:
            parents[str(setup[i][0])] = []
        else:
            if str(setup[i][0]) not in parents:
                parents[str(setup[i][0])] = []
            for j in range(2, len(setup[i])):
                parents[str(setup[i][j])].append(str(setup[i][0]))
    for parent in parents:
        parents[parent].append(parent)
        for child in parents[parent]:
            for baby in parents[child]:
                if baby not in parents[parent]:
                    parents[parent].append(baby)


    for i in range(num_comp + 2, len(setup)):
        #print(setup[i][1])
        if setup[i][1] in parents[str(setup[i][0])]:
            print("Yes")
        else:
            print("No")




    #print(parents)

if __name__ == "__main__":
        main()