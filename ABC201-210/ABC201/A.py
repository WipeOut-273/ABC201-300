a,b,c=map(int,input().split())
print('Yes' if a*2==b+c or b*2==c+a or c*2==a+b else 'No')