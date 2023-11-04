name = input()
dic = {}
for i in name:
    count = name.count(i)
    dic.update({i:count})
sorted_n_dic = dict(sorted(dic.items(), key=lambda x:x[0]))
sorted_dic = dict(sorted(sorted_n_dic.items(), key=lambda x:x[1], reverse=True))
j = 0
for i in sorted_dic.items():
    print(*i)
    j +=1
    if j == 3:
        break