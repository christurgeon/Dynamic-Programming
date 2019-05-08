def greedyAlg(data, W):
    data.sort(key=lambda l: float(l[1]/l[0]), reverse=True)
    retL = []
    currW = i = 0
    while (currW < W and i < len(data)):
        if (data[i][0]+currW < W):
            retL.append(data[i])
            currW += data[i][0]
        i += 1
    return retL


def dynamicAlg(data, W):
    # (n+1) by (W+1) 2D list
    data = [[i[1], i[0]] for i in data]
    table = [[0]*(W+1) for j in range(len(data)+1)]
    for i, (value, weight) in enumerate(data, 1): # skip index 1, case where none are chosen
        for cap in range(W+1):
            # Weight of current item > running capacity so it cant be added
            if weight > cap:
                table[i][cap] = table[i-1][cap]
            else:
                # Running capacity vs. adding next value if it meets weight constraint
                table[i][cap] = max( (table[i-1][cap]),(table[i-1][cap-weight]+value) )

    # Loop through the table and reconstruct best items
    retL = []
    j = W
    for i in reversed( range(1, len(data)) ):
        if (table[i][j] != table[i-1][j]):
            retL.append(data[i-1])
            j -= data[i-1][1]

    # Reverse order so that it is same as order given
    retL.reverse()
    for item in retL:
        print("[",item[1]," ",item[0],"]",sep="")
    print("")
    return retL



if __name__ == "__main__":
    data = [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97],
            [103, 97], [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104],
            [109, 106], [110, 107], [111, 108], [113, 107], [114, 110]]

    print("GREEDY & WEIGHT = 100:", greedyAlg(data, 100))
    print("GREEDY & WEIGHT = 200:", greedyAlg(data, 200))
    print("GREEDY & WEIGHT = 300:", greedyAlg(data, 300))
    print("")
    print("DYNAMIC, 100:")
    dynamicAlg(data, 100)
    print("DYNAMIC, 200:")
    dynamicAlg(data, 200)
    print("DYNAMIC, 300:")
    dynamicAlg(data, 300)
