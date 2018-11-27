def merge_the_tools(s, k):
    # your code goes here
    temp = []
    count = 1
    for i in range(len(s)):
        if s[i] not in temp:
            temp.append(s[i])
        if count == k:
            print(''.join(temp))
            temp = []
            count = 1
        else:
            count += 1


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)