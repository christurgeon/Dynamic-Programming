import random
import math



def longestPalindrome(list):
    revlist = list[::-1]
    M = len(list)
    N = len(list)
    table = [ [0]*(N+1) for i in range(M+1) ]

    # Build table from the top down
    # table[i][j] has length of longest palindrome subsequence
    # list[0..i-1] and revlist[0..j-1]
    for i in range(N+1):
        for j in range(N+1):
            if (i==0 or j==0):
                table[i][j] = 0
            elif (list[i-1] == revlist[j-1]):
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])

    # Following code is used to print palindrome
    # Start from bottom right corner and store characters in
    # lcs to be returned
    index = table[M][N];
    lcs = ["\n "] * (index+1)
    i,j = M,N
    while (i > 0 and j > 0):
        # If current character in list and revlist
        # are same, then that char is in palindrome
        if (list[i-1] == revlist[j-1]):
            # Put current character in result
            lcs[index-1] = list[i-1]
            i -= 1
            j -= 1
            index -= 1
        # Look at larger two to go in direction of greater value
        elif (table[i-1][j] > table[i][j-1]):
            i -= 1
        else:
            j -= 1

    returnString = ""
    for x in range(len(lcs)):
        returnString += str(lcs[x]) + " "
    return returnString



if __name__ == "__main__":
    L1 = [9, 14, 9, 5, 10, 6, 15, 6, 13, 9]
    L2 = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
    L3 = [3, 5, 5, 2, 5, 5, 3]
    L4 = [3, 5, 5, 3]
    L5 = [random.randint(1, 100) for x in range(1000)]
    print("Input:", L1, "\nOutput:",longestPalindrome(L1))
    print("Input:", L2, "\nOutput:",longestPalindrome(L2))
    print("Input:", L3, "\nOutput:",longestPalindrome(L3))
    print("Input:", L4, "\nOutput:",longestPalindrome(L4))
    print(longestPalindrome(L5))
