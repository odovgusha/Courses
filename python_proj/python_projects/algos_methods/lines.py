import sys

def marker(lines):

    lines_l = lines[1::]
    # sorted_dict = sorted(lines, key=lambda i: i[1], reverse=True)
    sorted_lines = sorted(lines_l, key=lambda i: i[1], reverse=False)
    # print(sorted_lines)
    # print(sorted_lines)
    # print(sorted_lines[0])
    # print(sorted_lines[1][1])
    # print(sorted_lines)
    # print(sorted_lines.remove(sorted_lines[2]))

    # print(sorted_lines)
    sol_lines = sorted_lines
    current_line = tuple()
    temp_lines = list()
    points = list()

    # print(len(sol_lines), "len_lines1")
    while len(sol_lines) != 0:
        # print("test")
        pos = sol_lines[0][1]
        points.append(pos)
        # print(pos)
        # sol_lines.remove(sol_lines[0])

        #
        # print(i, "zero")
        # print(len(sol_lines), "len_lines2")
        # if len(sol_lines) == 0:
        #     print("test3")
            # break
        i = 0
        # print(len(sol_lines), "start")
        # print(pos, "st")
        while pos >= sol_lines[i][0]:
        #     # print(i, "one")
        #     # print(sol_lines, "sol_lines")
            sol_lines.remove(sol_lines[i])
        #     # print("test2")
            if len(sol_lines) == 0:
                # print("test3")
                break
            # print(sol_lines)
            # print(i)
            # print(len(sol_lines), "end")
        #     # print("i+=1")
        #     # print(pos, "pos")
        #     # print(sol_lines)


    return points


    # print(len(points))
    # print(points)







    # print(sol_lines)
    # for l in range(0,le):
    #     print(lines)
    #     sol_lines.remove(lines)

# for i in range(1, len(sorted_lines)-1):
#         if sorted_lines[0][1] >= sorted_lines[i][0]:
#             print(sorted_lines[i])
            # sorted_lines.remove(sorted_lines[i])


def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    # print(list(reader))
    # marker(list(reader))
    out_point = marker(list(reader))
    print(len(out_point))
    print(*out_point, sep=' ')




if __name__ == "__main__":
    main()
"""
def marker(lines):

    lines_l = lines[1::]
    # sorted_dict = sorted(lines, key=lambda i: i[1], reverse=True)
    sorted_lines = sorted(lines_l, key=lambda i: i[1], reverse=False)
    # print(sorted_lines)
    # print(sorted_lines[0])
    # print(sorted_lines[1][1])
    # print(sorted_lines)
    # print(sorted_lines.remove(sorted_lines[2]))

    # print(sorted_lines)
    sol_lines = sorted_lines
    current_line = tuple()
    temp_lines = list()
    points = list()

    # print(len(sol_lines), "len_lines1")
    while len(sol_lines) > 0:
        # print("test")
        pos = sol_lines[0][1]
        points.append(pos)
        # print(pos)
        sol_lines.remove(sol_lines[0])

        i = 0
        # print(i, "zero")
        # print(len(sol_lines), "len_lines2")
        if len(sol_lines) == 0:
            # print("test3")
            break
        while pos >= sol_lines[i][0]:
            # print(i, "one")
            # print(sol_lines, "sol_lines")
            sol_lines.remove(sol_lines[i])
            # print("test2")
            if len(sol_lines) > 1:
                i += 1
            # print("i+=1")
            # print(pos, "pos")
            # print(sol_lines)
            if len(sol_lines) == 0:
                # print("test3")
                break

    return points


    # print(len(points))
    # print(points)
"""