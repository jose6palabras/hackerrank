if __name__ == '__main__':
    dic = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        dic.update({name:score})
    sorted_n_dic = dict(sorted(dic.items(), key=lambda x:x[0]))
    sorted_dic = dict(sorted(sorted_n_dic.items(), key=lambda x:x[1]))
    values = list(sorted_dic.values())
    keys = list(sorted_dic.keys())
    max_n = min(values)
    for i in range(1, len(keys)):
        if values[i] > max_n:
            print(keys[i])
            if i+1 < len(keys):
                if values[i] != values[i+1]:
                    break
            else:
                break