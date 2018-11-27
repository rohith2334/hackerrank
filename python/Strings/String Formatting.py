def print_formatted(n):
    width = len('{0:b}'.format(n))
    for i in range(1,n+1):
        print("{0:{1}d} {0:{1}o} {0:{1}X} {0:{1}b}".format(i,width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)