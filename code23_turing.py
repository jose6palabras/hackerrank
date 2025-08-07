x_list_t = []
def counter(x_list):
    count_0 = 0
    count_1 = 0
    if len(x_list) != 0:
        for i in x_list:
            if i == 0:
                count_0 = count_0 + 1
            elif i == 1:
                count_1 = count_1 + 1
            else:
                print("Error en lista")
                break
        #print(count_0, count_1)
        return count_0, count_1, len(x_list)
    else:
        return 0, 0, 0

        
def compare(tuplx):
    if tuplx[0] == tuplx[1]:
        print(tuplx[2])
    elif tuplx[0]==0 or tuplx[1]==0:
        print(1)
    elif tuplx[0] < tuplx[1]:
        print(2*tuplx[0] + 1)
    elif tuplx[1] < tuplx[0]:
        print(2*tuplx[1] + 1)
    else:
        2

compare(counter(x_list_t))
