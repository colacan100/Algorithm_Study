while True:
    n = int(input())
    n_list = list()
    if n==-1:
        break
    else:
        for i in range(1,n):
            if n%i==0:
                n_list.append(i)
        if n==sum(n_list):
            print(str(n) + ' = ' + " + ".join(str(j) for j in n_list))
        else:
            print(str(n)+' is NOT perfect.')