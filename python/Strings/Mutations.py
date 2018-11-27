def mutate_string(string, position, character):
    l1=list(string)
    l1[position]=character
    strin=''.join(l1)
    return strin

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)