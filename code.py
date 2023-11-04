if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    x_cdx = [i for i in range(x+1)]
    y_cdx = [i for i in range(y+1)]
    z_cdx = [i for i in range(z+1)]
    cx = []
    for i in x_cdx:
        for j in y_cdx:
            for k in z_cdx:
                cdx = [i, j, k]
                cx.append(cdx)   
    c_list = [cx[i] for i in range(len(cx)) if sum(cx[i])!=n]
    print(c_list)
