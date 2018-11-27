n,m = map(int,input().strip().split())
pattern = [('.|.'*(2*i+1)).center(m,'-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m,'-')]+ pattern[::-1]))