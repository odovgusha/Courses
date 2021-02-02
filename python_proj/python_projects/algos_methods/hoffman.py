import sys

def freq(test_str):

    str_dict = {}

    for i in range(0, len(test_str)):
        if test_str[i] in str_dict:
            str_dict[test_str[i]] += 1
        else:
            str_dict[test_str[i]] = 1
    return str_dict

def hmann(H):

    n = len(H)
    Hb = dict.fromkeys(H, '')
    Fl = list()
    # print(len(H))
    if len(H) == 1:
        # print(next(iter(H)),"gepa")
        Hb[list(Hb.keys())[0]] += '0'
    elif len(H) == 2:
        # print(next(iter(H)),"gepa")
        Hb[list(Hb.keys())[0]] += '0'
        Hb[list(Hb.keys())[1]] += '1'
    else:
        for k in range((n + 1), (2 * n - 1)):


            while len(H) > 1:
                # print(H)


                ifi = min(H, key=H.get)
                ifi_n = H[min(H, key=H.get)]
                del H[min(H, key=H.get)]
                jfj = min(H, key=H.get)
                jfj_n = H[min(H, key=H.get)]
                del H[min(H, key=H.get)]
                H[ifi + jfj] = ifi_n + jfj_n
                Fl.append((ifi, ifi_n, 1))
                Fl.append((jfj, jfj_n, 0))
                Fl.append((ifi + jfj, ifi_n + jfj_n))
                # print("min1: "+ifi, "min2: "+jfj)
                for i in ifi:
                    Hb[i] = '0' + Hb[i]
                    # Hb[i] += '0'
                for j in jfj:
                    Hb[j] = '1' + Hb[j]
                    # Hb[j] += '1'
                # print(Hb)



    return Hb


def encode(test_str, Hb):

    code_str = ""
    for c in test_str:
        code_str += Hb[c]

    return code_str




#1653264 3918848

#3918848 1653264
#3918848 % 1653264
def main():
    text = str(sys.stdin.readline()).rstrip()
    # print(text)
    # print(text)
    char_freq = freq(text)
    Hb_ans = hmann(char_freq)
    bin_str = encode(text, Hb_ans)
    # print(Hb_ans, bin_str, len(bin_str))
    print(len(Hb_ans), len(bin_str))
    # print(Hb_ans)
    for k, v in Hb_ans.items():
        print(k+":", v)
    print(bin_str)

    #print(gcd(a, b))

if __name__ == "__main__":
    main()


"""

test_str = "abacabad"
str_dict = {}


for i in range(0,len(test_str)):
    if test_str[i] in str_dict:
        str_dict[test_str[i]] += 1
    else:
        str_dict[test_str[i]] = 1
H = str_dict

# H = {"a":12,"b":3,"c":5,"d":6,"e":2,"f":7,"g":10,"k":4}
Hb = dict.fromkeys(H, '')
Fl = list()
for k in range((n + 1), (2 * n - 1)):
    while len(H) > 1:
        ifi = min(H, key=H.get)
        ifi_n = H[min(H, key=H.get)]
        del H[min(H, key=H.get)]
        jfj = min(H, key=H.get)
        jfj_n = H[min(H, key=H.get)]
        del H[min(H, key=H.get)]
        H[ifi + jfj] = ifi_n + jfj_n
        Fl.append((ifi, ifi_n, 1))
        Fl.append((jfj, jfj_n, 0))
        Fl.append((ifi + jfj, ifi_n + jfj_n))
        for i in ifi:
            Hb[i] += '0'
        for j in jfj:
            Hb[j] += '1'

        print(H)

#     print (H, ifi + jfj, ifi_n+jfj_n)
#     F2.append(ifi + jfj)
#     H.update(k,F[k])

code_str = ""
for c in test_str:
    code_str += Hb[c]


print(len(Hb), len(code_str))
"""