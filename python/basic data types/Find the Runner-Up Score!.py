if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    sort = arr.sort()
    maxi = max(arr)
    coun = arr.count(maxi)
    for i in range(0, coun):
        arr.remove(maxi)
    print(max(arr))


