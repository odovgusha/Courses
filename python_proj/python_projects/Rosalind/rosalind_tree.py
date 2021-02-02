import sys
import itertools
import operator

# def test():





def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    in_list = list(reader)
    n_edges = in_list[0][0]
    # print(list(reader))
    n_vet = in_list[1:]
    # print(n_edges)
    flat_vet = list(itertools.chain(*n_vet))
    max_vet = (max(flat_vet))
    min_vet = (min(flat_vet))
    print(max_vet, min_vet)
    range_vet = list(range(min_vet, max_vet+1))
    # print(range_vet)
    dict_vet = dict((el, 0) for el in range_vet)
    for i in flat_vet:
        # print(i)
        dict_vet[i] += 1
    print(dict_vet)
    sorted_d = sorted(dict_vet.items(), key=operator.itemgetter(1))
    print(sorted_d)
    print(len(sorted_d))
    print(n_edges)
    print(len([k for k, v in dict_vet.items() if float(v) == 0]))
    # print(list(reader)[0])
    # marker(list(reader))


if __name__ == "__main__":
    main()