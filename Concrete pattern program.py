num = int(input('Enter number : '))
n = num
for i in range(1,2 * num):
    # num = n
    for j in range(1, (2 * n)) :
        num = n
        if j >= i and j <= 2*n-i-1 :
            print(num-i+1, end = '  ')
        elif j >= 2*n - i and j <= i :
            print(i-num+1, end = '  ')
        elif j < i:
            print(num - j + 1, end = '  ')
        elif j >= 2*num - i:
            print(j-num+1, end = '  ')
        else :
            print(num, end = '  ')
    print()
