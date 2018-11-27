n=int(input())
dicto={}
for i in range(0,n):
    bnm = input().split()
    name = (bnm[0])
    number = int(bnm[1])
    dicto[name]=number
while True:
    line=input()
    if line in dicto:
        print("{}={}".format(line,dicto[line]))
    else:
        print("Not found ")        




