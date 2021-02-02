import sys


# def decode(test_dict, bin_str):
#     decoded_str = ""
#     bin_char = ""
#     for c in bin_str:
#         # print(c, "test")
#         # print(c == "1")
#         if c == "1":
#             bin_char += "1"
#         else:
#             bin_char += "0"
#             decoded_str += test_dict[bin_char]
#             # print(decoded_str)
#             # print(bin_char)
#             bin_char = ""
#     if bin_char != "":
#         decoded_str += test_dict[bin_char]
#
#     return decoded_str
def decode(test_dict, bin_str):
    decoded_str = ""
    bin_char = ""
    for c in bin_str:
        # print(c, "test")
        # print(c == "1")
        bin_char += c
        if bin_char in test_dict:
            #more elegant solution with error catcher
            #learn error catchers
            decoded_str += test_dict[bin_char]
            bin_char = ""
        else:
            continue

    return decoded_str



#1653264 3918848

#3918848 1653264
#3918848 % 1653264
def main():
    setup = list()
    for line in sys.stdin:
        # print(line.split()[0], line.split()[1])
        # print(tuple(map(str, (,line.split()[1]))))
        # print(list(line.split()[0].strip(":"), line.split()[1]))
        # print((tuple(map(str, (line.split())))[0]).strip(":"))
        setup.append(tuple(map(str, (line.split()))))
    # print(setup)
    encode_dict = (dict([(t[1], t[0].strip(":")) for t in setup[1:-1]]))
    # encode_dict = dict(setup[1:-1])
    code = (setup[-1][0])
    # print(code)
    # print(setup[1:-1])
    # print(encode_dict)
    decoded_str = decode(encode_dict, code)
    print(decoded_str)


    #print(gcd(a, b))

if __name__ == "__main__":
    main()