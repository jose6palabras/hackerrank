n_max = int(input())
word_dic = {}
for i in range(0, n_max):
    word = input()
    word_dic[word] = word_dic.get(word, 0) + 1
print(len(word_dic))
print(*word_dic.values())